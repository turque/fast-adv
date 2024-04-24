from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_current_athlete, get_password_hash
from app.db.session import get_session
from app.models import Athlete
from app.schemas import AthleteList, AthletePublic, AthleteSchema, Message

router = APIRouter()

Session = Annotated[Session, Depends(get_session)]
CurrentAthlete = Annotated[Athlete, Depends(get_current_athlete)]


@router.post('/', response_model=AthletePublic, status_code=201)
def create_athlete(
    athlete: AthleteSchema,
    db: Session,
    current_athlete: CurrentAthlete,
):
    db_athlete = db.scalar(
        select(Athlete).where(Athlete.email == athlete.email)
    )

    if db_athlete:
        raise HTTPException(
            status_code=400, detail='Username already registered'
        )

    hashed_password = get_password_hash(athlete.password)

    db_athlete = Athlete(
        name=athlete.name, password=hashed_password, email=athlete.email
    )
    db.add(db_athlete)
    db.commit()
    db.refresh(db_athlete)

    return db_athlete


@router.get('/', response_model=AthleteList)
def read_athletes(
    db: Session,
    current_athlete: CurrentAthlete,
    skip: int = 0,
    limit: int = 100,
):
    athletes = db.scalars(select(Athlete).offset(skip).limit(limit)).all()
    return {'athletes': athletes}


@router.put('/{athlete_id}', response_model=AthletePublic)
def update_athlete(
    athlete_id: int,
    athlete: AthleteSchema,
    db: Session,
    current_athlete: CurrentAthlete,
):
    if current_athlete.id != athlete_id:
        raise HTTPException(status_code=400, detail='Not enough permissions')

    current_athlete.name = athlete.name
    current_athlete.password = athlete.password
    current_athlete.email = athlete.email
    db.commit()
    db.refresh(current_athlete)

    return current_athlete


@router.delete('/{athlete_id}', response_model=Message)
def delete_athlete(
    athlete_id: int,
    db: Session,
    current_athlete: CurrentAthlete,
):
    if current_athlete.id != athlete_id:
        raise HTTPException(status_code=400, detail='Not enough permissions')

    db.delete(current_athlete)
    db.commit()

    return {'detail': 'Athlete deleted'}

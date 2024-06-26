from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.security import get_current_athlete, get_password_hash
from app.db.session import get_session

router = APIRouter()
Session = Annotated[Session, Depends(get_session)]
CurrentAthlete = Annotated[models.Athlete, Depends(get_current_athlete)]


@router.post('/', response_model=schemas.Athlete, status_code=201)
def create_athlete(
    athlete_in: schemas.AthleteCreate,
    db: Session,
    current_athlete: CurrentAthlete,
) -> Any:
    """
    Create new athlete.
    """
    athlete_in_db = crud.athlete.get_by_email(
        db=db, athlete_email=current_athlete.email
    )

    if athlete_in_db:
        raise HTTPException(status_code=400, detail='User already registered')

    athlete = crud.athlete.create(db=db, obj_in=athlete_in)

    return athlete


@router.put('/{id}', response_model=schemas.Message, status_code=200)
def update_athlete(
    id: int,
    athlete_in: schemas.AthleteUpdate,
    db: Session,
    current_athlete: CurrentAthlete,
):
    if current_athlete.id != id:
        raise HTTPException(status_code=400, detail='Not enough permissions')

    crud.athlete.update(db=db, db_obj=current_athlete, obj_in=athlete_in)

    return {'detail': 'Athlete updated'}


@router.delete('/', response_model=schemas.Message)
def delete_athlete(
    db: Session,
    current_athlete: CurrentAthlete,
):
    crud.athlete.remove(db=db, id=current_athlete.id)

    return {'detail': 'Athlete deleted'}

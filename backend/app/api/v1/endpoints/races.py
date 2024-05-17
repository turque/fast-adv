from typing import Annotated, Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.security import get_current_athlete
from app.db.session import get_session

router = APIRouter()
Session = Annotated[Session, Depends(get_session)]
CurrentAthlete = Annotated[models.Athlete, Depends(get_current_athlete)]


@router.get('/', response_model=List[schemas.Race])
def read_races(
    db: Session,
    current_athlete: CurrentAthlete,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve races.
    """
    races = crud.race.get_multi_by_athlete(
        db=db, athlete_id=current_athlete.id, skip=skip, limit=limit
    )
    return races


@router.get('/{id}')
def read_race_by_id(
    current_athlete: CurrentAthlete,
    id: int,
    db: Session,
) -> schemas.Race:
    """
    Get item by ID.
    """
    race = crud.race.get(db=db, id=id)
    return race


@router.post('/', response_model=schemas.Race, status_code=201)
def create_race(
    race_in: schemas.RaceCreate,
    current_athlete: CurrentAthlete,
    db: Session,
) -> Any:
    """
    Create new race.
    """
    race = crud.race.create(
        db=db, race_in=race_in, athlete_id=current_athlete.id
    )
    return race


@router.put('/{id}', response_model=schemas.Race)
def update_race(
    current_athlete: CurrentAthlete,
    id: int,
    db: Session,
    race_in: schemas.RaceUpdate,
) -> Any:
    """
    Update an race.
    """
    race = crud.race.get(db=db, id=id)
    if not race:
        raise HTTPException(status_code=404, detail='Race not found')
    if race.athlete_id != current_athlete.id:
        raise HTTPException(status_code=400, detail='Not enough permissions')
    race = crud.race.update(db=db, db_obj=race, obj_in=race_in)
    return race


@router.delete('/{id}', response_model=schemas.Race)
def delete_race(
    *, current_athlete: CurrentAthlete, id: int, db: Session
) -> Any:
    """
    Delete an item.
    """
    race = crud.race.get(db=db, id=id)
    if not race:
        raise HTTPException(status_code=404, detail='Item not found')
    if race.athlete_id != current_athlete.id:
        raise HTTPException(status_code=400, detail='Not enough permissions')
    race = crud.race.remove(db=db, id=id)
    return race

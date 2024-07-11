from typing import Annotated, Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.security import get_current_athlete
from app.db.session import get_session

router = APIRouter()
Session = Annotated[Session, Depends(get_session)]
CurrentAthlete = Annotated[models.Athlete, Depends(get_current_athlete)]


@router.post('/', response_model=schemas.Team, status_code=201)
def create_team(
    team_in: schemas.TeamCreate,
    current_athlete: CurrentAthlete,
    db: Session,
) -> Any:
    """
    Create new team.
    """
    team = crud.team.create(
        db=db, team_in=team_in, athlete_id=current_athlete.id
    )
    return team


@router.get('/', response_model=List[schemas.Team])
def read_athletes(
    db: Session,
    current_athlete: CurrentAthlete,
    skip: int = 0,
    limit: int = 100,
):

    teams = crud.team.get_multi_by_athlete(
        db=db, athlete_id=current_athlete.id, skip=skip, limit=limit
    )
    return teams


# @router.get('/{id}', response_model=schemas.Team)
# def read_team_by_id(
#     db: Session,
#     current_athlete: CurrentAthlete,
#     id: int,
# ) -> schemas.Team:
#     """
#     Get item by ID.
#     """
#     team = crud.team.get(db=db, id=id)
#     return team

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_session
from app.models import Team, User
from app.schemas import TeamList, TeamPublic, TeamSchema

CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter(prefix='/teams', tags=['teams'])


@router.post('/', response_model=TeamPublic)
def create_team(
    team: TeamSchema,
    user: CurrentUser,
    db: Session = Depends(get_session),
):
    db_team: Team = Team(
        name=team.name,
        team_members=team.team_members,
        owner_id=user.id,
        race_id=team.race_id,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)

    return db_team


@router.get('/', response_model=TeamList)
def read_users(
    user: CurrentUser,
    db: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
):
    teams = db.scalars(
        select(Team).where(Team.owner_id == user.id).offset(skip).limit(limit)
    ).all()
    return {'teams': teams}

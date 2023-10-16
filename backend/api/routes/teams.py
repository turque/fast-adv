from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_session
from api.models import Team, User
from api.schemas import TeamPublic, TeamSchema
from api.security import get_current_user

CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter(prefix='/teams', tags=['teams'])


@router.post('/', response_model=TeamPublic)
def create_team(
    team: TeamSchema,
    user: CurrentUser,
    session: Session = Depends(get_session),
):
    db_team: Team = Team(
        name=team.name,
        team_members=team.team_members,
        owner_id=user.id,
    )
    session.add(db_team)
    session.commit()
    session.refresh(db_team)

    return db_team

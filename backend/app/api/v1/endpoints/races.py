from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_session
from app.models import Race, User
from app.schemas import RaceList, RacePublic, RaceSchema

CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter()


@router.post('/', response_model=RacePublic)
def create_team(
    race: RaceSchema,
    user: CurrentUser,
    db: Session = Depends(get_session),
):
    db_race: Race = Race(
        **race,
        user_id=user.id,
    )
    db.add(db_race)
    db.commit()
    db.refresh(db_race)

    return db_race


@router.get('/', response_model=RaceList)
def read_users(
    user: CurrentUser,
    db: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
):
    races = db.scalars(
        select(Race).where(Race.user_id == user.id).offset(skip).limit(limit)
    ).all()
    return {'races': races}

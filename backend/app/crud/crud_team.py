from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Team
from app.schemas.team import TeamCreate, TeamUpdate


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    def create(
        self, db: Session, *, team_in: TeamCreate, athlete_id: int
    ) -> Team:
        db_team = Team(**team_in.model_dump(), owner_id=athlete_id)
        db.add(db_team)
        db.commit()
        db.refresh(db_team)
        return db_team

    def get_multi_by_athlete(
        self, db: Session, *, athlete_id: int, skip: int = 0, limit: int = 100
    ) -> List[Team]:
        return db.scalars(
            select(Team)
            .where(Team.owner_id == athlete_id)
            .offset(skip)
            .limit(limit)
        ).all()

    def get_by_id_and_owner(
        self, db: Session, *, team_id: int, athlete_id
    ) -> Team:
        return db.scalar(
            select(Team).where(Team.id == team_id, Team.owner_id == athlete_id)
        )


team = CRUDTeam(Team)

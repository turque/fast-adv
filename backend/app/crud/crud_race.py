from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Race
from app.schemas.race import RaceCreate, RaceUpdate


class CRUDRace(CRUDBase[Race, RaceCreate, RaceUpdate]):
    def create(
        self, db: Session, *, race_in: RaceCreate, user_id: int
    ) -> Race:
        db_race = Race(**race_in.model_dump(), user_id=user_id)
        db.add(db_race)
        db.commit()
        db.refresh(db_race)
        return db_race

    def get_multi_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Race]:
        return db.scalars(
            select(Race)
            .where(Race.user_id == user_id)
            .offset(skip)
            .limit(limit)
        ).all()

    def get_by_id(self, db: Session, *, race_id) -> Race:
        return db.scalars(select(Race).where(Race.id == race_id))


race = CRUDRace(Race)

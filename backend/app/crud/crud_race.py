from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Race
from app.schemas.race import RaceCreate, RaceUpdate


class CRUDRace(CRUDBase[Race, RaceCreate, RaceUpdate]):
    def create(
        self, db: Session, *, race_in: RaceCreate, athlete_id: int
    ) -> Race:
        db_race = Race(**race_in.model_dump(), athlete_id=athlete_id)
        db.add(db_race)
        db.commit()
        db.refresh(db_race)
        return db_race

    def get_multi_by_athlete(
        self, db: Session, *, athlete_id: int, skip: int = 0, limit: int = 100
    ) -> List[Race]:
        return db.scalars(
            select(Race)
            .where(Race.athlete_id == athlete_id)
            .offset(skip)
            .limit(limit)
        ).all()

    def get_by_id(self, db: Session, *, race_id: int) -> Race:
        return db.scalars(select(Race).where(Race.id == race_id))

    def get_by_id_and_onwer(
        self, db: Session, *, race_id: int, athlete_id: int
    ) -> Race:
        return db.scalars(
            select(Race).where(
                Race.id == race_id, Race.athlete_id == athlete_id
            )
        )


race = CRUDRace(Race)

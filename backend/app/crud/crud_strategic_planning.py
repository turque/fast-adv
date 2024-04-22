from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import StrategicPlanning
from app.schemas import StrategicPlanningCreate, StrategicPlanningUpdate


class CRUDStrategicPlanning(
    CRUDBase[
        StrategicPlanning, StrategicPlanningCreate, StrategicPlanningUpdate
    ]
):
    def create(
        self,
        db: Session,
        *,
        strategic_in: StrategicPlanningCreate,
        athlete_id: int,
        race_id: int
    ) -> StrategicPlanning:
        db_strategic = StrategicPlanning(
            **strategic_in.model_dump(), athlete_id=athlete_id, race_id=race_id
        )
        db.add(db_strategic)
        db.commit()
        db.refresh(db_strategic)
        return db_strategic

    def get_multi_by_race(
        self, db: Session, *, race_id: int, skip: int = 0, limit: int = 100
    ) -> List[StrategicPlanning]:
        return db.scalars(
            select(StrategicPlanning)
            .where(StrategicPlanning.race_id == race_id)
            .offset(skip)
            .limit(limit)
        ).all()

    def get_by_athlete(
        self,
        db: Session,
        race_id: int,
        athlete_id: int,
        skip: int = 0,
        limit: int = 100,
    ) -> StrategicPlanning:
        return db.scalars(
            select(StrategicPlanning)
            .where(
                StrategicPlanning.race_id == race_id,
                StrategicPlanning.athlete_id == athlete_id,
            )
            .offset(skip)
            .limit(limit)
        ).one_or_none()


strategic = CRUDStrategicPlanning(StrategicPlanning)

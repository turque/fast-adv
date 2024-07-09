from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.crud.base import CRUDBase
from app.models import Athlete
from app.schemas.athlete import AthleteCreate, AthleteUpdate


class CRUDAthlete(CRUDBase[Athlete, AthleteCreate, AthleteUpdate]):
    def create(self, db: Session, *, obj_in: AthleteCreate) -> Athlete:
        if obj_in.password is not None:
            obj_in.password = get_password_hash(obj_in.password)
        return super().create(db, obj_in=obj_in)

    def update(
        self, db: Session, *, db_obj: Athlete, obj_in: AthleteUpdate
    ) -> Athlete:
        if obj_in.password is not None:
            obj_in.password = get_password_hash(obj_in.password)
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def get_by_id(self, db: Session, *, athlete_id: int) -> Athlete:
        return db.scalars(select(Athlete).where(Athlete.id == athlete_id))

    def get_by_email(self, db: Session, *, athlete_email: str) -> Athlete:
        return db.scalars(
            select(Athlete).where(Athlete.email == athlete_email)
        )


athlete = CRUDAthlete(Athlete)

from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

from .enums import ModalityEnun

if TYPE_CHECKING:
    from .race import Race  # noqa: F401


class TimeLine(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    modality: Mapped[str] = mapped_column(Enum(ModalityEnun))

    race_id: Mapped[int] = mapped_column(ForeignKey('race.id'))

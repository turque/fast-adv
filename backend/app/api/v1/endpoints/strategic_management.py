from typing import Annotated, Any, List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.security import get_current_user
from app.db.session import get_session

router = APIRouter()
Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[models.User, Depends(get_current_user)]


@router.get('/{id}', response_model=List[schemas.Swot])
def read_races(
    db: Session,
    current_user: CurrentUser,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve races.
    """
    races = crud.race.get_multi_by_user(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )
    return races
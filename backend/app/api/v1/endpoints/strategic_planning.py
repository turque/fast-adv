from typing import Annotated, Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.security import get_current_user
from app.db.session import get_session

router = APIRouter()
Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[models.User, Depends(get_current_user)]


@router.get('/{race_id}', response_model=List[schemas.StrategicPlanning])
def read_strategic_planning_by_race(
    db: Session,
    current_user: CurrentUser,
    race_id: int,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve strategic planning by race.
    """
    strategics = crud.strategic.get_multi_by_race(
        db=db, race_id=race_id, skip=skip, limit=limit
    )

    return strategics


@router.post('/', response_model=schemas.StrategicPlanning, status_code=201)
def create_strategic_planning(
    strategic_in: schemas.StrategicPlanningCreate,
    current_user: CurrentUser,
    race_id: int,
    db: Session,
) -> Any:
    """
    Create new race strategic planning.
    """
    db_strategic = crud.strategic.get_by_user(
        db=db, race_id=race_id, user_id=current_user.id
    )

    if db_strategic:
        raise HTTPException(
            status_code=400,
            detail=(
                'User has already registered strategic planning for this race'
            ),
        )

    strategic = crud.strategic.create(
        db=db,
        strategic_in=strategic_in,
        user_id=current_user.id,
        race_id=race_id,
    )
    return strategic


@router.put('/{id}', response_model=schemas.StrategicPlanning)
def update_strategic_planning(
    current_user: CurrentUser,
    id: int,
    db: Session,
    strategic_in: schemas.StrategicPlanningUpdate,
) -> Any:
    """
    Update an race.
    """
    strategic = crud.strategic.get(db=db, id=id)
    if not strategic:
        raise HTTPException(
            status_code=404, detail='Strategic planning not found'
        )
    if strategic.user_id != current_user.id:
        raise HTTPException(status_code=400, detail='Not enough permissions')
    strategic = crud.strategic.update(
        db=db, db_obj=strategic, obj_in=strategic_in
    )
    return strategic

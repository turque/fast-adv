from typing import Annotated

from fastapi import APIRouter, Depends
from api.security import get_current_user
from api.models import User

CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter(prefix='/invite', tags=['teams'])

@router.post('/create', response_model=TeamPublic)
def create_team(
        user: CurrentUser,
    session: Session = Depends(get_session),
):
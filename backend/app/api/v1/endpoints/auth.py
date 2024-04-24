from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    get_current_athlete,
    verify_password,
)
from app.db.session import get_session
from app.models.athlete import Athlete
from app.schemas import Token

router = APIRouter()

OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
Session = Annotated[Session, Depends(get_session)]
CurrentAthlete = Annotated[Athlete, Depends(get_current_athlete)]


@router.post('/token', response_model=Token)
def login_for_access_token(form_data: OAuth2Form, session: Session):
    athlete = session.scalar(
        select(Athlete).where(Athlete.email == form_data.username)
    )

    if not athlete:
        raise HTTPException(
            status_code=400, detail='Incorrect email or password'
        )

    if not verify_password(form_data.password, athlete.password):
        raise HTTPException(
            status_code=400, detail='Incorrect email or password'
        )

    access_token = create_access_token(data={'sub': athlete.email})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/refresh_token', response_model=Token)
def refresh_access_token(athlete: CurrentAthlete):
    new_access_token = create_access_token(data={'sub': athlete.email})

    return {'access_token': new_access_token, 'token_type': 'bearer'}

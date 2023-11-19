from typing import Annotated, Any

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_session
from app.models import User
from app.schemas import Message
from app.utils.email import send_test_email

router = APIRouter()

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/test-email/', response_model=Message, status_code=201)
def test_email(
    email_to: EmailStr,
    user: CurrentUser,
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {'detail': 'Test email sent'}

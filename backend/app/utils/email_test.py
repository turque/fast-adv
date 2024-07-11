from app.core.settings import settings
from app.services.email import send_email


def send_test_email(email_to: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f'{project_name} - Test email'
    send_email(
        email_to,
        'Email tester',
        subject,
        settings.TEMPLATE_TEST,
        project_name=settings.PROJECT_NAME,
        email=email_to,
    )

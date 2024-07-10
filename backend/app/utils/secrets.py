import secrets
import string


def generate_password(length: int = 20) -> str:

    if not isinstance(length, int) or length < 8:
        raise ValueError('The password must be at least 8 characters long')

    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))


def generate_urlsafe() -> str:
    return secrets.token_urlsafe()

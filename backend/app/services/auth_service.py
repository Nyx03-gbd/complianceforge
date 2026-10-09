import hashlib
import secrets
from datetime import datetime, timedelta, timezone

import bcrypt
from jose import jwt

from app.config import settings


ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60
VERIFICATION_TOKEN_HOURS = 24
RESET_TOKEN_MINUTES = 30


PASSWORD_POLICY_MESSAGE = (
    "Le mot de passe doit contenir au moins "
    "8 caractères, une lettre, un chiffre "
    "et un caractère spécial."
)


def validate_password_policy(password: str) -> None:
    import re

    if len(password) < 8:
        raise ValueError(PASSWORD_POLICY_MESSAGE)

    if not re.search(r"[A-Za-z]", password):
        raise ValueError(PASSWORD_POLICY_MESSAGE)

    if not re.search(r"[0-9]", password):
        raise ValueError(PASSWORD_POLICY_MESSAGE)

    if not re.search(r"[^A-Za-z0-9]", password):
        raise ValueError(PASSWORD_POLICY_MESSAGE)


def validate_email_policy(email: str) -> str:
    import re

    email = email.strip()

    if email != email.lower():
        raise ValueError(
            "L'adresse e-mail doit être entièrement en minuscules."
        )

    if not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        email
    ):
        raise ValueError(
            "L'adresse e-mail doit être valide et contenir @."
        )

    return email


def hash_password(password: str) -> str:
    validate_password_policy(password)

    password_bytes = password.encode("utf-8")

    if len(password_bytes) > 72:
        raise ValueError(
            "Le mot de passe ne doit pas dépasser 72 octets."
        )

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(
        password_bytes,
        salt,
    ).decode("utf-8")


def verify_password(
    plain_password: str,
    password_hash: str,
) -> bool:
    password_bytes = plain_password.encode("utf-8")

    if len(password_bytes) > 72:
        return False

    return bcrypt.checkpw(
        password_bytes,
        password_hash.encode("utf-8"),
    )


def generate_token() -> str:
    return secrets.token_urlsafe(48)


def hash_token(token: str) -> str:
    return hashlib.sha256(
        token.encode("utf-8")
    ).hexdigest()


def create_access_token(user_id: str) -> str:
    now = datetime.now(timezone.utc)

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        ),
        "type": "access",
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=[ALGORITHM],
    )


def verification_expiration() -> datetime:
    return datetime.utcnow() + timedelta(
        hours=VERIFICATION_TOKEN_HOURS
    )


def reset_expiration() -> datetime:
    return datetime.utcnow() + timedelta(
        minutes=RESET_TOKEN_MINUTES
    )

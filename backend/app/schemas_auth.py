from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


def validate_lowercase_email(value: EmailStr) -> str:
    email = str(value).strip()

    if email != email.lower():
        raise ValueError(
            "L'adresse e-mail doit être entièrement en minuscules."
        )

    return email


class RegisterRequest(BaseModel):
    nom: str = Field(min_length=1, max_length=120)
    prenoms: Optional[str] = Field(default=None, max_length=160)
    email: EmailStr
    mot_de_passe: str = Field(min_length=8, max_length=128)
    fonction: Optional[str] = Field(default=None, max_length=160)
    organisation_id: Optional[str] = None

    _validate_email = field_validator("email")(
        validate_lowercase_email
    )


class LoginRequest(BaseModel):
    email: EmailStr
    mot_de_passe: str

    _validate_email = field_validator("email")(
        validate_lowercase_email
    )


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: str
    nom: str
    prenoms: Optional[str]
    email: str
    fonction: Optional[str]
    role: str
    organisation_id: Optional[str]
    email_verifie: bool


class MessageResponse(BaseModel):
    message: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr

    _validate_email = field_validator("email")(
        validate_lowercase_email
    )


class ResetPasswordRequest(BaseModel):
    token: str
    nouveau_mot_de_passe: str = Field(
        min_length=8,
        max_length=128
    )


class ChangePasswordRequest(BaseModel):
    ancien_mot_de_passe: str
    nouveau_mot_de_passe: str = Field(
        min_length=8,
        max_length=128
    )


class SecurityLogItem(BaseModel):
    id: str
    evenement: str
    description: str
    adresse_ip: str | None = None
    user_agent: str | None = None
    date_evenement: datetime

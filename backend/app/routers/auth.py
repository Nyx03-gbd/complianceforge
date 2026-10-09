import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Utilisateur, RoleUtilisateur, JournalSecurite
from app.schemas_auth import (
    ChangePasswordRequest,
    ForgotPasswordRequest,
    LoginRequest,
    MessageResponse,
    RegisterRequest,
    ResetPasswordRequest,
    SecurityLogItem,
    TokenResponse,
    UserResponse,
)
from app.services.auth_service import (
    create_access_token,
    decode_access_token,
    generate_token,
    hash_password,
    hash_token,
    reset_expiration,
    verification_expiration,
    verify_password,
)


router = APIRouter(
    prefix="/auth",
    tags=["authentification"],
)

logger = logging.getLogger("complianceforge.auth")

security = HTTPBearer()


def enregistrer_evenement_securite(
    db: Session,
    evenement: str,
    description: str,
    utilisateur_id=None,
    request=None,
):
    """
    Enregistre un événement de sécurité sans stocker
    de mot de passe, JWT ou token sensible.
    """

    adresse_ip = None
    user_agent = None

    if request is not None:
        adresse_ip = (
            request.client.host
            if request.client
            else None
        )

        user_agent = request.headers.get(
            "user-agent"
        )

    evenement_securite = JournalSecurite(
        utilisateur_id=utilisateur_id,
        evenement=evenement,
        description=description,
        adresse_ip=adresse_ip,
        user_agent=user_agent,
    )

    db.add(evenement_securite)
    db.commit()


@router.post(
    "/register",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db),
):
    email = data.email.lower().strip()

    existing = (
        db.query(Utilisateur)
        .filter(Utilisateur.email == email)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Cette adresse e-mail est déjà utilisée.",
        )

    verification_token = generate_token()

    try:
        password_hash = hash_password(
            data.mot_de_passe
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    user = Utilisateur(
        nom=data.nom.strip(),
        prenoms=(
            data.prenoms.strip()
            if data.prenoms
            else None
        ),
        email=email,
        fonction=(
            data.fonction.strip()
            if data.fonction
            else None
        ),
        organisation_id=data.organisation_id,
        role=RoleUtilisateur.metier,
        mot_de_passe_hash=password_hash,
        email_verifie=False,
        token_verification_hash=hash_token(
            verification_token
        ),
        token_verification_expire_at=
            verification_expiration(),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    logger.info(
        "Compte créé pour %s.",
        email,
    )

    # MODE DÉVELOPPEMENT UNIQUEMENT
    logger.warning(
        "TOKEN DE VERIFICATION DEV — "
        "email=%s token=%s",
        email,
        verification_token,
    )

    return MessageResponse(
        message=(
            "Compte créé. "
            "Vérifiez votre adresse e-mail "
            "pour activer votre compte."
        )
    )


@router.get(
    "/verify-email",
    response_model=MessageResponse,
)
def verify_email(
    token: str,
    db: Session = Depends(get_db),
):
    token_hash = hash_token(token)

    user = (
        db.query(Utilisateur)
        .filter(
            Utilisateur.token_verification_hash ==
            token_hash
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Token de vérification invalide.",
        )

    if user.email_verifie:
        return MessageResponse(
            message="Adresse e-mail déjà vérifiée."
        )

    if (
        not user.token_verification_expire_at
        or user.token_verification_expire_at
        < datetime.utcnow()
    ):
        raise HTTPException(
            status_code=400,
            detail="Le token de vérification a expiré.",
        )

    user.email_verifie = True
    user.token_verification_hash = None
    user.token_verification_expire_at = None

    enregistrer_evenement_securite(
        db=db,
        evenement="EMAIL_VERIFIE",
        description="Adresse e-mail vérifiée avec succès.",
        utilisateur_id=user.id,
    )

    db.commit()

    return MessageResponse(
        message=(
            "Adresse e-mail vérifiée. "
            "Vous pouvez maintenant vous connecter."
        )
    )


@router.post(
    "/resend-verification",
    response_model=MessageResponse,
)
def resend_verification(
    email: str,
    db: Session = Depends(get_db),
):
    email = email.lower().strip()

    user = (
        db.query(Utilisateur)
        .filter(Utilisateur.email == email)
        .first()
    )

    # Ne pas révéler si l'adresse existe.
    if not user:
        return MessageResponse(
            message=(
                "Si ce compte existe, "
                "un nouveau lien de vérification "
                "sera généré."
            )
        )

    if user.email_verifie:
        return MessageResponse(
            message="Cette adresse e-mail est déjà vérifiée."
        )

    verification_token = generate_token()

    user.token_verification_hash = hash_token(
        verification_token
    )
    user.token_verification_expire_at = (
        verification_expiration()
    )

    db.commit()

    logger.warning(
        "TOKEN DE VERIFICATION DEV — "
        "email=%s token=%s",
        email,
        verification_token,
    )

    return MessageResponse(
        message=(
            "Un nouveau lien de vérification "
            "a été généré."
        )
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    data: LoginRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    email = data.email.lower().strip()

    user = (
        db.query(Utilisateur)
        .filter(Utilisateur.email == email)
        .first()
    )

    if (
        not user
        or not verify_password(
            data.mot_de_passe,
            user.mot_de_passe_hash,
        )
    ):
        enregistrer_evenement_securite(
            db=db,
            evenement="ECHEC_CONNEXION",
            description="Tentative de connexion échouée.",
            utilisateur_id=(
                user.id
                if user
                else None
            ),
            request=request,
        )

        raise HTTPException(
            status_code=401,
            detail="Adresse e-mail ou mot de passe incorrect.",
        )

    if not user.email_verifie:
        raise HTTPException(
            status_code=403,
            detail=(
                "Votre adresse e-mail n'est pas encore "
                "vérifiée."
            ),
        )

    token = create_access_token(
        str(user.id)
    )

    enregistrer_evenement_securite(
        db=db,
        evenement="CONNEXION_REUSSIE",
        description="Connexion réussie au compte.",
        utilisateur_id=user.id,
        request=request,
    )

    return TokenResponse(
        access_token=token,
    )


@router.get(
    "/me",
    response_model=UserResponse,
)
def current_user(
    credentials: HTTPAuthorizationCredentials =
        Depends(security),
    db: Session = Depends(get_db),
):
    try:

        payload = decode_access_token(
            credentials.credentials
        )

        user_id = payload.get("sub")

        if not user_id:
            raise ValueError("sub absent")

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Token invalide ou expiré.",
        )

    user = (
        db.query(Utilisateur)
        .filter(Utilisateur.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Utilisateur introuvable.",
        )

    return UserResponse(
        id=str(user.id),
        nom=user.nom,
        prenoms=user.prenoms,
        email=user.email,
        fonction=user.fonction,
        role=user.role.value,
        organisation_id=(
            str(user.organisation_id)
            if user.organisation_id
            else None
        ),
        email_verifie=user.email_verifie,
    )


@router.post(
    "/change-password",
    response_model=MessageResponse,
)
def change_password(
    data: ChangePasswordRequest,
    credentials: HTTPAuthorizationCredentials =
        Depends(security),
    db: Session = Depends(get_db),
):
    try:
        payload = decode_access_token(
            credentials.credentials
        )
        user_id = payload.get("sub")

        if not user_id:
            raise ValueError("sub absent")

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Token invalide ou expiré.",
        )

    user = (
        db.query(Utilisateur)
        .filter(Utilisateur.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Utilisateur introuvable.",
        )

    if not verify_password(
        data.ancien_mot_de_passe,
        user.mot_de_passe_hash,
    ):
        raise HTTPException(
            status_code=400,
            detail="L'ancien mot de passe est incorrect.",
        )

    if data.ancien_mot_de_passe == data.nouveau_mot_de_passe:
        raise HTTPException(
            status_code=400,
            detail=(
                "Le nouveau mot de passe doit être "
                "différent de l'ancien."
            ),
        )

    try:
        nouveau_hash = hash_password(
            data.nouveau_mot_de_passe
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    user.mot_de_passe_hash = nouveau_hash

    enregistrer_evenement_securite(
        db=db,
        evenement="CHANGEMENT_MOT_DE_PASSE",
        description="Mot de passe modifié avec succès.",
        utilisateur_id=user.id,
    )

    db.commit()

    return MessageResponse(
        message="Mot de passe modifié avec succès."
    )


@router.post(
    "/forgot-password",
    response_model=MessageResponse,
)
def forgot_password(
    data: ForgotPasswordRequest,
    db: Session = Depends(get_db),
):
    email = data.email.lower().strip()

    user = (
        db.query(Utilisateur)
        .filter(Utilisateur.email == email)
        .first()
    )

    if not user:
        return MessageResponse(
            message=(
                "Si cette adresse existe, "
                "un lien de réinitialisation "
                "sera généré."
            )
        )

    reset_token = generate_token()

    user.token_reset_hash = hash_token(
        reset_token
    )
    user.token_reset_expire_at = (
        reset_expiration()
    )

    enregistrer_evenement_securite(
        db=db,
        evenement="DEMANDE_RESET_MOT_DE_PASSE",
        description="Demande de réinitialisation du mot de passe.",
        utilisateur_id=user.id,
    )

    db.commit()

    # MODE DÉVELOPPEMENT UNIQUEMENT
    logger.warning(
        "TOKEN RESET DEV — "
        "email=%s token=%s",
        email,
        reset_token,
    )

    return MessageResponse(
        message=(
            "Si cette adresse existe, "
            "un lien de réinitialisation "
            "a été généré."
        )
    )


@router.post(
    "/reset-password",
    response_model=MessageResponse,
)
def reset_password(
    data: ResetPasswordRequest,
    db: Session = Depends(get_db),
):
    token_hash = hash_token(data.token)

    user = (
        db.query(Utilisateur)
        .filter(
            Utilisateur.token_reset_hash ==
            token_hash
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Token de réinitialisation invalide.",
        )

    if (
        not user.token_reset_expire_at
        or user.token_reset_expire_at
        < datetime.utcnow()
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Le token de réinitialisation "
                "a expiré."
            ),
        )

    try:
        nouveau_hash = hash_password(
            data.nouveau_mot_de_passe
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    user.mot_de_passe_hash = nouveau_hash

    user.token_reset_hash = None
    user.token_reset_expire_at = None

    enregistrer_evenement_securite(
        db=db,
        evenement="RESET_MOT_DE_PASSE",
        description="Mot de passe réinitialisé avec succès.",
        utilisateur_id=user.id,
    )

    db.commit()

    return MessageResponse(
        message="Mot de passe réinitialisé avec succès.",
    )


@router.get(
    "/security-log",
    response_model=list[SecurityLogItem],
)
def security_log(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    claims = decode_access_token(
        credentials.credentials
    )

    if not claims or not claims.get("sub"):
        raise HTTPException(
            status_code=401,
            detail="Session invalide ou expirée.",
        )

    user_id = claims["sub"]

    evenements = (
        db.query(JournalSecurite)
        .filter(
            JournalSecurite.utilisateur_id == user_id
        )
        .order_by(
            JournalSecurite.date_evenement.desc()
        )
        .limit(50)
        .all()
    )

    return [
        SecurityLogItem(
            id=str(event.id),
            evenement=event.evenement,
            description=event.description,
            adresse_ip=event.adresse_ip,
            user_agent=event.user_agent,
            date_evenement=event.date_evenement,
        )
        for event in evenements
    ]


@router.post(
    "/logout",
    response_model=MessageResponse,
)
def logout(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    request: Request = None,
    db: Session = Depends(get_db),
):
    claims = decode_access_token(
        credentials.credentials
    )

    if not claims or not claims.get("sub"):
        raise HTTPException(
            status_code=401,
            detail="Session invalide ou expirée.",
        )

    user_id = claims["sub"]

    enregistrer_evenement_securite(
        db=db,
        evenement="DECONNEXION",
        description="Déconnexion du compte.",
        utilisateur_id=user_id,
        request=request,
    )

    return MessageResponse(
        message="Déconnexion enregistrée."
    )

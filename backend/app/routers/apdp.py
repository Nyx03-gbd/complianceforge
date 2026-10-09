from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    Organisation,
    Traitement,
    ProfilResponsableAPDP,
    TraitementAPDP,
    PrincipesAPDP,
    SecuriteAPDP,
    DroitsPersonnesAPDP,
    TraitementsAnterieursAPDP,
)
from app.schemas import (
    ProfilResponsableAPDPCreate,
    ProfilResponsableAPDPOut,
    TraitementAPDPCreate,
    TraitementAPDPOut,
    PrincipesAPDPCreate,
    PrincipesAPDPOut,
    SecuriteAPDPCreate,
    SecuriteAPDPOut,
    DroitsPersonnesAPDPCreate,
    DroitsPersonnesAPDPOut,
    TraitementsAnterieursAPDPCreate,
    TraitementsAnterieursAPDPOut,
)


router = APIRouter(
    prefix="/apdp",
    tags=["APDP"],
)


# ============================================================
# PROFIL RESPONSABLE APDP
# ============================================================

@router.post(
    "/organisations/{organisation_id}/profil",
    response_model=ProfilResponsableAPDPOut,
)
def creer_profil_apdp(
    organisation_id: str,
    data: ProfilResponsableAPDPCreate,
    db: Session = Depends(get_db),
):
    organisation = db.query(Organisation).filter(
        Organisation.id == organisation_id
    ).first()

    if not organisation:
        raise HTTPException(
            status_code=404,
            detail="Organisation introuvable",
        )

    profil = db.query(ProfilResponsableAPDP).filter(
        ProfilResponsableAPDP.organisation_id == organisation_id
    ).first()

    if profil:
        raise HTTPException(
            status_code=409,
            detail="Un profil APDP existe déjà pour cette organisation",
        )

    profil = ProfilResponsableAPDP(
        organisation_id=organisation_id,
        **data.model_dump(exclude={"organisation_id"}),
    )

    db.add(profil)
    db.commit()
    db.refresh(profil)

    return profil


@router.get(
    "/organisations/{organisation_id}/profil",
    response_model=ProfilResponsableAPDPOut,
)
def obtenir_profil_apdp(
    organisation_id: str,
    db: Session = Depends(get_db),
):
    profil = db.query(ProfilResponsableAPDP).filter(
        ProfilResponsableAPDP.organisation_id == organisation_id
    ).first()

    if not profil:
        raise HTTPException(
            status_code=404,
            detail="Profil APDP introuvable",
        )

    return profil


# ============================================================
# INFORMATIONS DU TRAITEMENT APDP
# ============================================================

@router.post(
    "/traitements/{traitement_id}",
    response_model=TraitementAPDPOut,
)
def creer_traitement_apdp(
    traitement_id: str,
    data: TraitementAPDPCreate,
    db: Session = Depends(get_db),
):
    traitement = db.query(Traitement).filter(
        Traitement.id == traitement_id
    ).first()

    if not traitement:
        raise HTTPException(
            status_code=404,
            detail="Traitement introuvable",
        )

    existant = db.query(TraitementAPDP).filter(
        TraitementAPDP.traitement_id == traitement_id
    ).first()

    if existant:
        raise HTTPException(
            status_code=409,
            detail="Les informations APDP existent déjà pour ce traitement",
        )

    donnees = data.model_dump(exclude={"traitement_id"})

    apdp = TraitementAPDP(
        traitement_id=traitement_id,
        **donnees,
    )

    db.add(apdp)
    db.commit()
    db.refresh(apdp)

    return apdp


@router.get(
    "/traitements/{traitement_id}",
    response_model=TraitementAPDPOut,
)
def obtenir_traitement_apdp(
    traitement_id: str,
    db: Session = Depends(get_db),
):
    apdp = db.query(TraitementAPDP).filter(
        TraitementAPDP.traitement_id == traitement_id
    ).first()

    if not apdp:
        raise HTTPException(
            status_code=404,
            detail="Informations APDP introuvables",
        )

    return apdp


# ============================================================
# PRINCIPES
# ============================================================

@router.put(
    "/traitements/{traitement_id}/principes",
    response_model=PrincipesAPDPOut,
)
def enregistrer_principes(
    traitement_id: str,
    data: PrincipesAPDPCreate,
    db: Session = Depends(get_db),
):
    traitement = db.query(Traitement).filter(
        Traitement.id == traitement_id
    ).first()

    if not traitement:
        raise HTTPException(
            status_code=404,
            detail="Traitement introuvable",
        )

    principes = db.query(PrincipesAPDP).filter(
        PrincipesAPDP.traitement_id == traitement_id
    ).first()

    donnees = data.model_dump(exclude={"traitement_id"})

    if principes:
        for champ, valeur in donnees.items():
            setattr(principes, champ, valeur)
    else:
        principes = PrincipesAPDP(
            traitement_id=traitement_id,
            **donnees,
        )
        db.add(principes)

    db.commit()
    db.refresh(principes)

    return principes


@router.get(
    "/traitements/{traitement_id}/principes",
    response_model=PrincipesAPDPOut,
)
def obtenir_principes(
    traitement_id: str,
    db: Session = Depends(get_db),
):
    principes = db.query(PrincipesAPDP).filter(
        PrincipesAPDP.traitement_id == traitement_id
    ).first()

    if not principes:
        raise HTTPException(
            status_code=404,
            detail="Principes APDP introuvables",
        )

    return principes


# ============================================================
# SECURITE
# ============================================================

@router.put(
    "/traitements/{traitement_id}/securite",
    response_model=SecuriteAPDPOut,
)
def enregistrer_securite(
    traitement_id: str,
    data: SecuriteAPDPCreate,
    db: Session = Depends(get_db),
):
    traitement = db.query(Traitement).filter(
        Traitement.id == traitement_id
    ).first()

    if not traitement:
        raise HTTPException(
            status_code=404,
            detail="Traitement introuvable",
        )

    securite = db.query(SecuriteAPDP).filter(
        SecuriteAPDP.traitement_id == traitement_id
    ).first()

    donnees = data.model_dump(exclude={"traitement_id"})

    if securite:
        for champ, valeur in donnees.items():
            setattr(securite, champ, valeur)
    else:
        securite = SecuriteAPDP(
            traitement_id=traitement_id,
            **donnees,
        )
        db.add(securite)

    db.commit()
    db.refresh(securite)

    return securite


@router.get(
    "/traitements/{traitement_id}/securite",
    response_model=SecuriteAPDPOut,
)
def obtenir_securite(
    traitement_id: str,
    db: Session = Depends(get_db),
):
    securite = db.query(SecuriteAPDP).filter(
        SecuriteAPDP.traitement_id == traitement_id
    ).first()

    if not securite:
        raise HTTPException(
            status_code=404,
            detail="Informations de sécurité APDP introuvables",
        )

    return securite


# ============================================================
# DROITS DES PERSONNES
# ============================================================

@router.put(
    "/traitements/{traitement_id}/droits",
    response_model=DroitsPersonnesAPDPOut,
)
def enregistrer_droits(
    traitement_id: str,
    data: DroitsPersonnesAPDPCreate,
    db: Session = Depends(get_db),
):
    traitement = db.query(Traitement).filter(
        Traitement.id == traitement_id
    ).first()

    if not traitement:
        raise HTTPException(
            status_code=404,
            detail="Traitement introuvable",
        )

    droits = db.query(DroitsPersonnesAPDP).filter(
        DroitsPersonnesAPDP.traitement_id == traitement_id
    ).first()

    donnees = data.model_dump(exclude={"traitement_id"})

    if droits:
        for champ, valeur in donnees.items():
            setattr(droits, champ, valeur)
    else:
        droits = DroitsPersonnesAPDP(
            traitement_id=traitement_id,
            **donnees,
        )
        db.add(droits)

    db.commit()
    db.refresh(droits)

    return droits


@router.get(
    "/traitements/{traitement_id}/droits",
    response_model=DroitsPersonnesAPDPOut,
)
def obtenir_droits(
    traitement_id: str,
    db: Session = Depends(get_db),
):
    droits = db.query(DroitsPersonnesAPDP).filter(
        DroitsPersonnesAPDP.traitement_id == traitement_id
    ).first()

    if not droits:
        raise HTTPException(
            status_code=404,
            detail="Droits APDP introuvables",
        )

    return droits


# ============================================================
# TRAITEMENTS ANTERIEURS
# ============================================================

@router.put(
    "/traitements/{traitement_id}/anterieurs",
    response_model=TraitementsAnterieursAPDPOut,
)
def enregistrer_anterieurs(
    traitement_id: str,
    data: TraitementsAnterieursAPDPCreate,
    db: Session = Depends(get_db),
):
    traitement = db.query(Traitement).filter(
        Traitement.id == traitement_id
    ).first()

    if not traitement:
        raise HTTPException(
            status_code=404,
            detail="Traitement introuvable",
        )

    anterieurs = db.query(TraitementsAnterieursAPDP).filter(
        TraitementsAnterieursAPDP.traitement_id == traitement_id
    ).first()

    donnees = data.model_dump(exclude={"traitement_id"})

    if anterieurs:
        for champ, valeur in donnees.items():
            setattr(anterieurs, champ, valeur)
    else:
        anterieurs = TraitementsAnterieursAPDP(
            traitement_id=traitement_id,
            **donnees,
        )
        db.add(anterieurs)

    db.commit()
    db.refresh(anterieurs)

    return anterieurs


@router.get(
    "/traitements/{traitement_id}/anterieurs",
    response_model=TraitementsAnterieursAPDPOut,
)
def obtenir_anterieurs(
    traitement_id: str,
    db: Session = Depends(get_db),
):
    anterieurs = db.query(TraitementsAnterieursAPDP).filter(
        TraitementsAnterieursAPDP.traitement_id == traitement_id
    ).first()

    if not anterieurs:
        raise HTTPException(
            status_code=404,
            detail="Traitements antérieurs APDP introuvables",
        )

    return anterieurs

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/traitements", tags=["traitements"])


@router.post("", response_model=schemas.TraitementOut, status_code=201)
def creer_traitement(payload: schemas.TraitementCreate, db: Session = Depends(get_db)):
    traitement = models.Traitement(
        nom=payload.nom,
        organisation_id=payload.organisation_id,
        service_responsable=payload.service_responsable,
        finalite=payload.finalite,
        base_legale=payload.base_legale,
        justification_base_legale=payload.justification_base_legale,
        sensibilite_donnees=payload.sensibilite_donnees,
        niveau_mesures_securite=payload.niveau_mesures_securite,
        sous_traitance_transferts=payload.sous_traitance_transferts,
        exposition=payload.exposition,
        volume=payload.volume,
    )
    traitement.categories_donnees = [
        models.CategorieDonnee(categorie=c.categorie, sensible=c.sensible)
        for c in payload.categories_donnees
    ]
    db.add(traitement)
    db.commit()
    db.refresh(traitement)
    return traitement


@router.get("", response_model=list[schemas.TraitementOut])
def lister_traitements(organisation_id: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Traitement)
    if organisation_id:
        query = query.filter(models.Traitement.organisation_id == organisation_id)
    return query.order_by(models.Traitement.derniere_revision.desc()).all()


@router.get("/{traitement_id}", response_model=schemas.TraitementOut)
def lire_traitement(traitement_id: str, db: Session = Depends(get_db)):
    traitement = db.get(models.Traitement, traitement_id)
    if not traitement:
        raise HTTPException(status_code=404, detail="Traitement introuvable")
    return traitement


@router.patch("/{traitement_id}", response_model=schemas.TraitementOut)
def modifier_traitement(
    traitement_id: str, payload: schemas.TraitementUpdate, db: Session = Depends(get_db)
):
    traitement = db.get(models.Traitement, traitement_id)
    if not traitement:
        raise HTTPException(status_code=404, detail="Traitement introuvable")

    for champ, valeur in payload.model_dump(exclude_unset=True).items():
        setattr(traitement, champ, valeur)

    db.commit()
    db.refresh(traitement)
    return traitement


@router.delete("/{traitement_id}", status_code=204)
def supprimer_traitement(traitement_id: str, db: Session = Depends(get_db)):
    traitement = db.get(models.Traitement, traitement_id)
    if not traitement:
        raise HTTPException(status_code=404, detail="Traitement introuvable")
    db.delete(traitement)
    db.commit()

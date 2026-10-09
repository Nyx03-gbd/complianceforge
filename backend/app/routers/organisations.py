from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/organisations", tags=["organisations"])


@router.post("", response_model=schemas.OrganisationOut, status_code=201)
def creer_organisation(payload: schemas.OrganisationCreate, db: Session = Depends(get_db)):
    organisation = models.Organisation(**payload.model_dump())
    db.add(organisation)
    db.commit()
    db.refresh(organisation)
    return organisation


@router.get("", response_model=list[schemas.OrganisationOut])
def lister_organisations(db: Session = Depends(get_db)):
    return db.query(models.Organisation).order_by(models.Organisation.nom).all()


@router.get("/{organisation_id}", response_model=schemas.OrganisationOut)
def lire_organisation(organisation_id: str, db: Session = Depends(get_db)):
    organisation = db.get(models.Organisation, organisation_id)
    if not organisation:
        raise HTTPException(status_code=404, detail="Organisation introuvable")
    return organisation

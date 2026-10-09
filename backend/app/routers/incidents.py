from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db


router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post("", response_model=schemas.IncidentOut, status_code=201)
def creer_incident(
    payload: schemas.IncidentCreate,
    db: Session = Depends(get_db),
):
    organisation = db.get(models.Organisation, payload.organisation_id)
    if not organisation:
        raise HTTPException(
            status_code=404,
            detail="Organisation introuvable",
        )

    if payload.traitement_id:
        traitement = db.get(models.Traitement, payload.traitement_id)
        if not traitement:
            raise HTTPException(
                status_code=404,
                detail="Traitement introuvable",
            )

    echeance = payload.date_heure_constatation + timedelta(hours=72)

    incident = models.Incident(
        **payload.model_dump(),
        echeance_notification=echeance,
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


@router.get("", response_model=list[schemas.IncidentOut])
def lister_incidents(
    organisation_id: str | None = None,
    statut: models.StatutIncident | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(models.Incident)

    if organisation_id:
        query = query.filter(
            models.Incident.organisation_id == organisation_id
        )

    if statut:
        query = query.filter(
            models.Incident.statut == statut
        )

    return query.order_by(
        models.Incident.date_heure_constatation.desc()
    ).all()


@router.get("/{incident_id}", response_model=schemas.IncidentOut)
def lire_incident(
    incident_id: str,
    db: Session = Depends(get_db),
):
    incident = db.get(models.Incident, incident_id)

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident introuvable",
        )

    return incident


@router.patch("/{incident_id}", response_model=schemas.IncidentOut)
def modifier_incident(
    incident_id: str,
    payload: schemas.IncidentUpdate,
    db: Session = Depends(get_db),
):
    incident = db.get(models.Incident, incident_id)

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident introuvable",
        )

    modifications = payload.model_dump(exclude_unset=True)

    if "statut" in modifications:
        try:
            incident.statut = models.StatutIncident(modifications["statut"])
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Statut d'incident invalide",
            )

    if "date_notification" in modifications:
        date_notification = modifications["date_notification"]
        incident.date_notification = date_notification

        incident.notification_dans_les_delais = (
            date_notification <= incident.echeance_notification
        )

    db.commit()
    db.refresh(incident)

    return incident

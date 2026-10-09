from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    traitements,
    organisations,
    scores,
    apdp_documents,
    apdp,
    incidents,
    dashboard,
    apdp_generation,
    auth,
)

app = FastAPI(
    title="ComplianceForge API",
    description=(
        "Plateforme GRC-as-Code : automatisation du registre APDP, "
        "scoring de risque et notification de violation sous 72h."
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://complianceforge.test",
        "http://127.0.0.1:8080",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(organisations.router)
app.include_router(traitements.router)
app.include_router(scores.router)
app.include_router(apdp_documents.router)
app.include_router(apdp.router)
app.include_router(incidents.router)
app.include_router(dashboard.router)
app.include_router(apdp_generation.router)
app.include_router(auth.router)

@app.get("/health", tags=["système"])
def health_check():
    return {"status": "ok"}


# --- PDF générés : téléchargement depuis l'interface ---
from pathlib import Path as _Path
from fastapi.staticfiles import StaticFiles as _StaticFiles

_GENERATED = _Path(__file__).resolve().parent.parent / "generated"
(_GENERATED / "apdp").mkdir(parents=True, exist_ok=True)
app.mount("/generated", _StaticFiles(directory=str(_GENERATED)), name="generated")

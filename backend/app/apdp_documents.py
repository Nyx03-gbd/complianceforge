"""Référentiel des documents APDP utilisés par ComplianceForge."""

from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = BASE_DIR / "apdp_documents.json"


def load_registry() -> dict:
    with REGISTRY_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def get_document(document_id: str) -> dict:
    registry = load_registry()
    for document in registry["documents"]:
        if document["id"] == document_id:
            return document
    raise KeyError(f"Document APDP inconnu: {document_id}")


def list_documents(category: str | None = None) -> list[dict]:
    documents = load_registry()["documents"]
    if category is None:
        return documents
    return [d for d in documents if d["category"] == category]

"""
Moteur de scoring — Phase 4 du plan de construction.

Deux scores, jamais fusionnés :
  - Score de risque : le traitement est-il dangereux pour les personnes concernées ?
  - Score de conformité documentaire : le dossier est-il complet et bien rempli ?
    (reproduit la logique de l'Outil de vérification de l'APDP — poids par
    section, agrégés en un taux de conformité).

Ce module ne touche jamais à la base de données : il prend des données en
entrée (dicts simples) et retourne des résultats en dicts simples. Ça le rend
testable avec de simples appels de fonction, sans dépendance à FastAPI ou à
un traitement en base — voir tests_scoring.py.
"""

import json
from pathlib import Path
from dataclasses import dataclass

GRILLE_PATH = Path(__file__).parent / "grille_ponderation_v1.json"


def charger_grille(chemin: Path = GRILLE_PATH) -> dict:
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def calculer_score_conformite(traitement_data: dict, grille: dict | None = None) -> dict:
    grille = grille or charger_grille()
    sections = grille["sections"]

    detail_sections = {}
    poids_total = 0
    score_pondere_total = 0.0

    for nom_section, section in sections.items():
        poids_section = section["poids"]
        champs = section["champs"]
        poids_champs_total = sum(champs.values())
        points_obtenus = 0

        for champ, poids_champ in champs.items():
            valeur = traitement_data.get(champ)
            rempli = _champ_est_rempli(valeur)
            if rempli:
                points_obtenus += poids_champ

        taux_section = (points_obtenus / poids_champs_total * 100) if poids_champs_total else 0
        detail_sections[nom_section] = {
            "poids_section": poids_section,
            "taux_completion": round(taux_section, 1),
        }
        poids_total += poids_section
        score_pondere_total += taux_section * poids_section

    score_global = round(score_pondere_total / poids_total, 1) if poids_total else 0.0

    return {
        "score_global": score_global,
        "version_grille": grille.get("version", "inconnue"),
        "details": detail_sections,
    }


def _champ_est_rempli(valeur) -> bool:
    if valeur is None:
        return False
    if isinstance(valeur, str):
        return valeur.strip() != ""
    if isinstance(valeur, (list, dict)):
        return len(valeur) > 0
    return True


POIDS_RISQUE = {
    "sensibilite_donnees": 0.25,
    "niveau_mesures_securite": 0.25,
    "conformite_documentaire": 0.20,
    "sous_traitance_transferts": 0.15,
    "exposition": 0.10,
    "volume": 0.05,
}


@dataclass
class CriteresRisque:
    sensibilite_donnees: int
    niveau_mesures_securite: int
    sous_traitance_transferts: int
    exposition: int
    volume: int
    score_conformite: float


def _conformite_vers_niveau_risque(score_conformite: float) -> float:
    score_conformite = max(0.0, min(100.0, score_conformite))
    return 1 + 3 * (1 - score_conformite / 100)


def calculer_score_risque(criteres: CriteresRisque) -> dict:
    for champ in ("sensibilite_donnees", "niveau_mesures_securite",
                  "sous_traitance_transferts", "exposition", "volume"):
        valeur = getattr(criteres, champ)
        if not (1 <= valeur <= 4):
            raise ValueError(f"{champ} doit être entre 1 et 4 (reçu : {valeur})")

    conformite_documentaire = _conformite_vers_niveau_risque(criteres.score_conformite)

    composantes = {
        "sensibilite_donnees": criteres.sensibilite_donnees,
        "niveau_mesures_securite": criteres.niveau_mesures_securite,
        "conformite_documentaire": conformite_documentaire,
        "sous_traitance_transferts": criteres.sous_traitance_transferts,
        "exposition": criteres.exposition,
        "volume": criteres.volume,
    }

    somme_ponderee = sum(POIDS_RISQUE[c] * v for c, v in composantes.items())
    score_global = round(100 * somme_ponderee / 4, 1)

    return {
        "score_global": score_global,
        "niveau": _niveau_risque(score_global),
        "composantes": composantes,
    }


def _niveau_risque(score: float) -> str:
    if score <= 25:
        return "faible"
    if score <= 50:
        return "moyen"
    if score <= 75:
        return "eleve"
    return "critique"


def appliquer_score_fraicheur(score_risque: float, mois_depuis_derniere_revue: int) -> float:
    if mois_depuis_derniere_revue <= 12:
        return score_risque
    penalite = 1 + 0.1 * (mois_depuis_derniere_revue - 12) / 12
    return round(min(100.0, score_risque * penalite), 1)

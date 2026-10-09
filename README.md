# ComplianceForge

Plateforme GRC-as-Code : registre des traitements APDP, génération des formulaires APDP (PDF), scoring de conformité et de risque, suivi des incidents (notification de violation sous 72 h).

Équipe : Nyx

## Architecture
Interface web (HTML/CSS/JS) -> proxy HTTPS (Caddy) -> API FastAPI -> base PostgreSQL. API et base tournent dans des conteneurs Docker.

## Prérequis
Linux, Docker et Docker Compose, Caddy, Git.

## Installation
1. Cloner le dépôt : `git clone https://github.com/Nyx03-gbd/complianceforge.git && cd complianceforge-repo`
2. Créer la configuration : `cp .env.example .env`, puis remplacer les valeurs `CHANGE_ME` (même mot de passe dans `POSTGRES_PASSWORD` et dans `DATABASE_URL` ; générer `SECRET_KEY` avec `openssl rand -hex 32`).
3. Lancer l'API et la base : `docker compose up -d --build`
4. Créer les tables : `docker compose exec api alembic upgrade head`
   (alternative : `docker compose exec -T db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"' < database/schema.sql`)
5. Déclarer les noms locaux : `echo "127.0.0.1 complianceforge.test api.complianceforge.test" | sudo tee -a /etc/hosts`
6. Lancer le serveur HTTPS depuis la racine du dépôt : `sudo caddy run --config Caddyfile`, puis `sudo caddy trust` dans un autre terminal.
7. Ouvrir https://complianceforge.test et créer un compte depuis l'écran de connexion.

La documentation de l'API est disponible sur https://api.complianceforge.test/docs

## Structure
- `backend/` : API FastAPI, moteur de génération PDF, modèles, migrations (`alembic/`), formulaires APDP (`templates/`)
- `frontend/` : interface web
- `database/schema.sql` : schéma de la base
- `docker-compose.yml`, `Caddyfile`, `.env.example` : configuration

## Sources et licences
Les formulaires APDP sont les documents officiels de l'APDP du Bénin. Les dépendances open source sont listées dans `backend/requirements.txt`. Le code applicatif a été écrit par moi même.

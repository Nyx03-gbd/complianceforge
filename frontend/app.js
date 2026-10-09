/* État global APDP — doit être disponible avant tout rendu */
window.apdpUIState = window.apdpUIState || {};

/* =========================================================
   NAVIGATION OVERLAY — COMPLIANCEFORGE
   ========================================================= */

(function initComplianceForgeSidebar() {

    function init() {

        const sidebar =
            document.querySelector(".sidebar");

        const toggle =
            document.getElementById("sidebar-toggle");

        const overlay =
            document.getElementById("sidebar-overlay");

        if (!sidebar || !toggle || !overlay) {
            return;
        }

        function openSidebar() {

            sidebar.classList.add("sidebar-open");

            overlay.classList.add(
                "sidebar-overlay-visible"
            );

            toggle.classList.add(
                "sidebar-toggle-hidden"
            );

            toggle.setAttribute(
                "aria-expanded",
                "true"
            );

            overlay.setAttribute(
                "aria-hidden",
                "false"
            );
        }

        function closeSidebar() {

            sidebar.classList.remove(
                "sidebar-open"
            );

            overlay.classList.remove(
                "sidebar-overlay-visible"
            );

            toggle.classList.remove(
                "sidebar-toggle-hidden"
            );

            toggle.setAttribute(
                "aria-expanded",
                "false"
            );

            overlay.setAttribute(
                "aria-hidden",
                "true"
            );
        }

        toggle.addEventListener(
            "click",
            openSidebar
        );

        overlay.addEventListener(
            "click",
            closeSidebar
        );

        sidebar
            .querySelectorAll(".nav-item")
            .forEach(item => {

                item.addEventListener(
                    "click",
                    closeSidebar
                );

            });

        document.addEventListener(
            "keydown",
            event => {

                if (event.key === "Escape") {
                    closeSidebar();
                }

            }
        );
    }

    if (document.readyState === "loading") {

        document.addEventListener(
            "DOMContentLoaded",
            init
        );

    } else {

        init();

    }

})();






(function applyDashboardCardStyles() {

 if (document.getElementById("dashboard-clickable-cards-style")) {
 return;
 }

 const style = document.createElement("style");

 style.id = "dashboard-clickable-cards-style";

 style.textContent = `
 .dashboard-card-clickable {
 cursor: pointer;
 transition:
 transform 0.15s ease,
 box-shadow 0.15s ease,
 border-color 0.15s ease;
 }

 .dashboard-card-clickable:hover {
 transform: translateY(-2px);
 box-shadow: 0 6px 18px rgba(15, 23, 42, 0.10);
 border-color: #2563eb;
 }

 .dashboard-card-clickable:focus {
 outline: 2px solid #2563eb;
 outline-offset: 2px;
 }
 `;

 document.head.appendChild(style);

})();

const pages = {
 dashboard: {
 title: "🏠 Tableau de bord",
 subtitle: "Vue générale de votre conformité GRC",
 content: `
 <div class="welcome">
 <h2>Bienvenue dans ComplianceForge</h2>
 <p>Centralisez vos informations d'organisation, traitements, formalités APDP, risques et incidents.</p>
 </div>

 <section class="cards">
 <div
 class="card dashboard-card-clickable"
 onclick="navigate('organisation')"
 role="button"
 tabindex="0"
 title="Accéder à la page Organisation"
 >
 <div class="card-icon">🏢</div>
 <div>
 <span>Organisation</span>
 <strong id="organisation-count"></strong>
 </div>
 </div>

 <div
 class="card dashboard-card-clickable"
 onclick="navigate('registre')"
 role="button"
 tabindex="0"
 title="Accéder au registre des traitements"
 >
 <div class="card-icon">📋</div>
 <div>
 <span>Traitements</span>
 <strong id="traitement-count"></strong>
 </div>
 </div>

 <div
 class="card dashboard-card-clickable"
 onclick="navigate('incidents')"
 role="button"
 tabindex="0"
 title="Accéder aux incidents et violations"
 >
 <div class="card-icon">🚨</div>
 <div>
 <span>Incidents</span>
 <strong id="incident-count"></strong>
 </div>
 </div>

 <div
 class="card dashboard-card-clickable"
 onclick="navigate('incidents')"
 role="button"
 tabindex="0"
 title="Consulter les éléments hors délai"
 >
 <div class="card-icon">⏰</div>
 <div>
 <span>Hors délai</span>
 <strong id="incident-overdue"></strong>
 </div>
 </div>
 </section>


 <section class="dashboard-scoring-section">
 <div class="dashboard-scoring-header">
 <div>
 <h2>Analyse / Scoring</h2>
 <p>Évaluation de la conformité et du risque des traitements.</p>
 </div>

 <button
 type="button"
 class="btn-primary"
 onclick="navigate('scoring')">
 Voir l'analyse
 </button>
 </div>

 <div class="dashboard-scoring-grid">

 <div class="dashboard-score-card">
 <span>Score de conformité</span>
 <strong id="dashboard-score-conformite">—</strong>
 <small>Dernière évaluation</small>
 </div>

 <div class="dashboard-score-card">
 <span>Score de risque</span>
 <strong id="dashboard-score-risque">—</strong>
 <small>Dernière évaluation</small>
 </div>

 <div class="dashboard-score-card">
 <span>Niveau de risque</span>
 <strong id="dashboard-niveau-risque">—</strong>
 <small>Niveau calculé</small>
 </div>

 <div class="dashboard-score-card">
 <span>Traitement évalué</span>
 <strong id="dashboard-traitement-score">—</strong>
 <small id="dashboard-scoring-status">
 Aucun traitement évalué
 </small>
 </div>

 </div>
 </section>

<footer class="dashboard-footer">

 <div class="dashboard-footer-header">
 <div>
 <h2>Accès rapides</h2>
 <p>Les principales fonctions de ComplianceForge</p>
 </div>
 </div>

 <div class="dashboard-footer-actions">

 <button class="quick-card" onclick="navigate('organisation')">
 <span></span>
 <div>
 <strong>🏢 Organisation</strong>
 <small>Renseigner les informations de l'entreprise</small>
 </div>
 </button>

 <button class="quick-card" onclick="navigate('formulaires')">
 <span></span>
 <div>
 <strong>🧾 Formulaires APDP</strong>
 <small>Accéder aux formulaires et annexes</small>
 </div>
 </button>

 <button class="quick-card" onclick="navigate('registre')">
 <span></span>
 <div>
 <strong>📋 Registre des traitements</strong>
 <small>Gérer les traitements de l'organisation</small>
 </div>
 </button>

 <button class="quick-card" onclick="navigate('incidents')">
 <span></span>
 <div>
 <strong>🚨 Incidents / Violations</strong>
 <small>Suivre le workflow de notification</small>
 </div>
 </button>

 </div>

 <div class="dashboard-footer-bottom">
 <span>ComplianceForge</span>
 <span>Plateforme GRC</span>
 </div>

</footer>
 `
 },

 scoring: {
 title: "Analyse / Scoring",
 subtitle: "Évaluation de la conformité et du risque",
 content: `
 <div class="page-card">

 <div class="page-card-header">
 <div>
 <h2>Analyse / Scoring</h2>
 <p>
 Calcul et consultation des scores
 de conformité et de risque.
 </p>
 </div>
 </div>

 <div id="scoring-container">
 <div class="scoring-loading">
 Chargement des traitements...
 </div>
 </div>

 </div>
 `
 },

organisation: {
 title: "Organisation",
 subtitle: "Informations générales de l'entreprise",
 content: `
 <div class="page-card">
 <div class="page-card-header">
 <div>
 <h2>Informations de l'organisation</h2>
 <p>Ces informations pourront être réutilisées dans les formulaires APDP.</p>
 </div>
 </div>

 <form id="organisation-form" class="form-grid">
 <div class="form-group full">
 <label>Nom de l'organisation *</label>
 <input type="text" name="nom" placeholder="Ex. Entreprise Démo">
 </div>

 <div class="form-group">
 <label>Secteur d'activité</label>
 <input type="text" name="secteur_activite" placeholder="Ex. Services">
 </div>

 <div class="form-group">
 <label>IFU / RCCM</label>
 <input type="text" name="ifu_rccm" placeholder="Numéro IFU ou RCCM">
 </div>

 <div class="form-group full">
 <label>Adresse</label>
 <textarea name="adresse" rows="3" placeholder="Adresse de l'organisation"></textarea>
 </div>

 <div class="form-group">
 <label>Email DPO</label>
 <input type="email" name="contact_dpo_email" placeholder="dpo@example.local">
 </div>

 <div class="form-actions full">
 <button type="submit" class="btn-primary">
 Enregistrer l'organisation
 </button>
 </div>
 </form>

 <div id="organisation-message" class="form-message"></div>
 </div>
 `
 },

 profil: {
 title: "👤 Profil APDP",
 subtitle: "Informations nécessaires au Formulaire Unique",
 content: `
 <div class="page-card">

 <div class="page-card-header">
 <div>
 <h2>Responsable du traitement</h2>
 <p>
 Renseignez les informations nécessaires à la préparation
 du Formulaire Unique APDP.
 </p>
 </div>
 </div>

 <form id="profil-apdp-form" class="form-grid">

 <div class="form-group full">
 <label for="profil-organisation">
 Organisation *
 </label>

 <select id="profil-organisation" name="organisation_id" required>
 <option value="">Chargement des organisations...</option>
 </select>
 </div>

 <div class="form-group full">
 <label>Nom / Prénoms / Raison sociale</label>
 <input
 type="text"
 name="nom_prenoms_raison_sociale"
 placeholder="Nom, prénoms ou raison sociale"
 >
 </div>

 <div class="form-group">
 <label>NPI / RCCM</label>
 <input
 type="text"
 name="npi_rccm"
 placeholder="Numéro NPI ou RCCM"
 >
 </div>

 <div class="form-group">
 <label>Carré / Lot</label>
 <input
 type="text"
 name="carre_lot"
 placeholder="Carré / Lot"
 >
 </div>

 <div class="form-group">
 <label>Quartier</label>
 <input
 type="text"
 name="quartier"
 placeholder="Quartier"
 >
 </div>

 <div class="form-group">
 <label>Ville</label>
 <input
 type="text"
 name="ville"
 placeholder="Ville"
 >
 </div>

 <div class="form-group full">
 <label>Adresse postale</label>
 <textarea
 name="adresse_postale"
 rows="3"
 placeholder="Adresse postale"
 ></textarea>
 </div>

 <div class="form-group">
 <label>Adresse électronique</label>
 <input
 type="email"
 name="adresse_electronique"
 placeholder="contact@example.local"
 >
 </div>

 <div class="form-group">
 <label>Contact téléphonique</label>
 <input
 type="text"
 name="contact_telephonique"
 placeholder="+229 ..."
 >
 </div>

 <div class="form-group full">
 <label>Autres contacts</label>
 <input
 type="text"
 name="autres_contacts"
 placeholder="Autres moyens de contact"
 >
 </div>

 <div class="form-group full">
 <label>Activité</label>
 <textarea
 name="activite"
 rows="3"
 placeholder="Description de l'activité"
 ></textarea>
 </div>

 <div class="form-group">
 <label>Secteur d'activité</label>
 <input
 type="text"
 name="secteur_activite"
 placeholder="Ex. Services numériques"
 >
 </div>

 <div class="form-group">
 <label>Représentant légal - Nom / Prénoms</label>
 <input
 type="text"
 name="representant_legal_nom_prenoms"
 placeholder="Nom et prénoms"
 >
 </div>

 <div class="form-group">
 <label>Représentant légal - NPI</label>
 <input
 type="text"
 name="representant_legal_npi"
 placeholder="NPI"
 >
 </div>

 <div class="form-group">
 <label>Représentant légal - Contacts</label>
 <input
 type="text"
 name="representant_legal_contacts"
 placeholder="Téléphone / email"
 >
 </div>

 <div class="form-group full">
 <label>Représentant légal - Adresse</label>
 <textarea
 name="representant_legal_adresse"
 rows="3"
 placeholder="Adresse du représentant légal"
 ></textarea>
 </div>

 <div class="form-actions full">
 <button
 type="submit"
 class="btn-primary"
 >
 Enregistrer le profil APDP
 </button>
 </div>

 </form>

 <div id="profil-apdp-message" class="form-message"></div>

 </div>
 `
 },

registre: {
 title: "Registre des traitements",
 subtitle: "Gestion des traitements de données personnelles",
 content: `
 <div class="page-card">

 <div class="page-card-header">
 <div>
 <h2>📋 Registre des traitements</h2>
 <p>
 Créez et gérez les traitements de données personnelles
 de l'organisation.
 </p>
 </div>
 </div>

 <form id="traitement-form" class="form-grid">

 <div class="form-section full">
 <div class="form-section-title">
 <span></span>
 <div>
 <h3>Identification du traitement</h3>
 <p>Informations générales sur le traitement.</p>
 </div>
 </div>
 </div>

 <div class="form-group full">
 <label>Organisation *</label>
 <select
 name="organisation_id"
 id="traitement-organisation"
 required
 >
 <option value="">Sélectionner une organisation</option>
 </select>
 </div>

 <div class="form-group">
 <label>Nom du traitement *</label>
 <input
 type="text"
 name="nom"
 placeholder="Ex. Gestion des ressources humaines"
 required
 >
 </div>

 <div class="form-group">
 <label>Service responsable</label>
 <input
 type="text"
 name="service_responsable"
 placeholder="Ex. Direction des Ressources Humaines"
 >
 </div>

 <div class="form-section full">
 <div class="form-section-title">
 <span></span>
 <div>
 <h3>Finalité et base légale</h3>
 <p>Cadre juridique et objectif du traitement.</p>
 </div>
 </div>
 </div>

 <div class="form-group full">
 <label>Finalité</label>
 <textarea
 name="finalite"
 rows="3"
 placeholder="Décrivez la finalité du traitement"
 ></textarea>
 </div>

 <div class="form-group">
 <label>Base légale</label>
 <input
 type="text"
 name="base_legale"
 placeholder="Ex. Obligation légale"
 >
 </div>

 <div class="form-group">
 <label>Justification de la base légale</label>
 <textarea
 name="justification_base_legale"
 rows="3"
 placeholder="Expliquez la base légale retenue"
 ></textarea>
 </div>

 <div class="form-section full">
 <div class="form-section-title">
 <span></span>
 <div>
 <h3>Catégories de données</h3>
 <p>
 Ajoutez les catégories de données traitées
 et indiquez si elles sont sensibles.
 </p>
 </div>
 </div>
 </div>

 <div class="form-group full">
 <div id="categories-donnees">

 <div class="categorie-row">
 <input
 type="text"
 class="categorie-nom"
 placeholder="Ex. Données d'identification"
 >

 <label class="checkbox-label">
 <input
 type="checkbox"
 class="categorie-sensible"
 >
 Donnée sensible
 </label>

 <button
 type="button"
 class="btn-secondary categorie-remove"
 >
 Supprimer
 </button>
 </div>

 </div>

 <button
 type="button"
 class="btn-secondary"
 id="ajouter-categorie"
 >
 + Ajouter une catégorie
 </button>
 </div>

 <div class="form-section full">
 <div class="form-section-title">
 <span></span>
 <div>
 <h3>Paramètres d'évaluation</h3>
 <p>
 Paramètres utilisés pour l'évaluation
 du traitement.
 </p>
 </div>
 </div>
 </div>

 <div class="form-group">
 <label>Sensibilité des données</label>
 <select name="sensibilite_donnees">
 <option value="">Non renseigné</option>
 <option value="1">1 — Faible</option>
 <option value="2">2</option>
 <option value="3">3</option>
 <option value="4">4 — Élevée</option>
 </select>
 </div>

 <div class="form-group">
 <label>Niveau des mesures de sécurité</label>
 <select name="niveau_mesures_securite">
 <option value="">Non renseigné</option>
 <option value="1">1</option>
 <option value="2">2</option>
 <option value="3">3</option>
 <option value="4">4</option>
 </select>
 </div>

 <div class="form-group">
 <label>Sous-traitance / transferts</label>
 <select name="sous_traitance_transferts">
 <option value="">Non renseigné</option>
 <option value="1">1</option>
 <option value="2">2</option>
 <option value="3">3</option>
 <option value="4">4</option>
 </select>
 </div>

 <div class="form-group">
 <label>Exposition</label>
 <select name="exposition">
 <option value="">Non renseigné</option>
 <option value="1">1</option>
 <option value="2">2</option>
 <option value="3">3</option>
 <option value="4">4</option>
 </select>
 </div>

 <div class="form-group">
 <label>Volume</label>
 <select name="volume">
 <option value="">Non renseigné</option>
 <option value="1">1</option>
 <option value="2">2</option>
 <option value="3">3</option>
 <option value="4">4</option>
 </select>
 </div>

 <div class="form-actions full">
 <button type="submit" class="btn-primary">
 Enregistrer le traitement
 </button>
 </div>

 </form>

 <div id="traitement-message" class="form-message"></div>

 </div>
 `
},
formulaires: {
 title: "Formulaires APDP",
 subtitle: "Préparer et générer les formulaires officiels APDP",
 content: `
 <div class="page-card">
 <div class="page-card-header">
 <div>
 <h2>Formulaires officiels APDP</h2>
 <p>
 Sélectionnez un formulaire pour préparer les informations
 à reporter sur le document officiel.
 </p>
 </div>
 <span class="status-badge">
 Documents officiels préservés
 </span>
 </div>


 <div class="page-card" id="apdp-context-selector"
 style="margin-bottom:20px;">

 <div class="page-card-header">
 <div>
 <h3>Contexte du formulaire</h3>
 <p>
 Sélectionnez l'organisation et le traitement
 concernés par la formalité APDP.
 </p>
 </div>
 </div>

 <div style="
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:16px;
 margin-top:16px;
 ">

 <div class="form-group">
 <label for="apdp-organisation-select">
 Organisation
 </label>

 <select
 id="apdp-organisation-select"
 class="form-control">
 <option value="">
 Chargement des organisations...
 </option>
 </select>
 </div>

 <div class="form-group">
 <label for="apdp-traitement-select">
 Traitement
 </label>

 <select
 id="apdp-traitement-select"
 class="form-control"
 disabled>
 <option value="">
 Sélectionnez d'abord une organisation
 </option>
 </select>
 </div>

 </div>

 <div
 id="apdp-context-message"
 class="form-message"
 style="margin-top:12px;">
 </div>

 </div>

 <div class="forms-grid">

 <div class="form-tile">
 <span></span>
 <h3>Formulaire Unique</h3>
 <p>Déclaration principale d'un traitement.</p>
 <button
 type="button"
 class="btn-primary"
 onclick="openAPDPForm('formulaire_unique')">
 Préparer
 </button>
 </div>

 <div class="form-tile">
 <span></span>
 <h3>Annexe 1 - Sous-traitance</h3>
 <p>Informations relatives aux sous-traitants.</p>
 <button
 type="button"
 class="btn-secondary"
 onclick="openAPDPForm('annexe_1_sous_traitance')">
 Préparer
 </button>
 </div>

 <div class="form-tile">
 <span></span>
 <h3>Annexe 2 - Communication</h3>
 <p>Communication des données personnelles.</p>
 <button
 type="button"
 class="btn-secondary"
 onclick="openAPDPForm('annexe_2_communication')">
 Préparer
 </button>
 </div>

 <div class="form-tile">
 <span></span>
 <h3>Annexe 3 - Interconnexion</h3>
 <p>Interconnexion de fichiers ou traitements.</p>
 <button
 type="button"
 class="btn-secondary"
 onclick="openAPDPForm('annexe_3_interconnexion')">
 Préparer
 </button>
 </div>

 <div class="form-tile">
 <span></span>
 <h3>Annexe 4 - Transfert</h3>
 <p>Transfert de données personnelles.</p>
 <button
 type="button"
 class="btn-secondary"
 onclick="openAPDPForm('annexe_4_transfert')">
 Préparer
 </button>
 </div>

 <div class="form-tile">
 <span></span>
 <h3>Formulaire Capteurs</h3>
 <p>Traitements utilisant des capteurs.</p>
 <button
 type="button"
 class="btn-secondary"
 onclick="openAPDPForm('formulaire_capteurs')">
 Préparer
 </button>
 </div>

 <div class="form-tile">
 <span></span>
 <h3>Formulaire Site Web</h3>
 <p>Traitements liés à un site web.</p>
 <button
 type="button"
 class="btn-secondary"
 onclick="openAPDPForm('formulaire_site_web')">
 Préparer
 </button>
 </div>

 <div class="form-tile">
 <span></span>
 <h3>Engagement de conformité</h3>
 <p>Préparation de l'engagement officiel.</p>
 <button
 type="button"
 class="btn-secondary"
 onclick="openAPDPForm('engagement_conformite')">
 Préparer
 </button>
 </div>

 </div>

 <div class="apdp-info-box">
 <strong> Principe de fonctionnement</strong>
 <p>
 ComplianceForge utilise les mappings APDP existants pour
 positionner les données dans les zones prévues du document.
 La structure du PDF officiel n'est pas reconstruite ni
 modifiée.
 </p>
 </div>

 <div id="apdp-form-editor"></div>
 </div>
 `
},
 conformite: {
 title: "Analyse des écarts",
 subtitle: "Vue synthétique de la conformité APDP",
 content: `
 <div class="gap-container">

 <div class="page-card gap-summary">
 <div>
 <h2>📊 Analyse des écarts</h2>
 <p>État actuel des processus de conformité APDP et niveau cible ComplianceForge.</p>
 </div>

 <div class="gap-summary-stats">
 <div>
 <strong>10</strong>
 <span>domaines analysés</span>
 </div>
 <div>
 <strong>4</strong>
 <span>niveau cible</span>
 </div>
 <div>
 <strong>3</strong>
 <span>écarts prioritaires</span>
 </div>
 </div>
 </div>

 <div class="page-card">
 <div class="gap-title">
 <h3>Maturité</h3>
 <span class="gap-target">Cible : 4</span>
 </div>

 <div class="gap-maturity-summary">
 <div>
 <strong>1</strong>
 <span>Plus faible niveau actuel</span>
 </div>
 <div>
 <strong>2</strong>
 <span>Niveau le plus fréquent</span>
 </div>
 <div>
 <strong>3</strong>
 <span>Meilleur niveau actuel</span>
 </div>
 <div>
 <strong>4</strong>
 <span>Niveau cible</span>
 </div>
 </div>
 </div>

 <div class="page-card">
 <div class="gap-title">
 <h3>Principaux écarts</h3>
 <span>Situation actuelle → cible</span>
 </div>

 <div class="gap-compact-list">
 <div>
 <span>Conformité documentaire</span>
 <b>1 → 4</b>
 </div>
 <div>
 <span>Violations de données</span>
 <b>1 → 4</b>
 </div>
 <div>
 <span>📋 Registre des traitements</span>
 <b>2 → 4</b>
 </div>
 <div>
 <span>Formalités APDP</span>
 <b>2 → 4</b>
 </div>
 <div>
 <span>Sécurité des données</span>
 <b>2 → 4</b>
 </div>
 <div>
 <span>Droits des personnes</span>
 <b>2 → 4</b>
 </div>
 </div>
 </div>

 <div class="page-card">
 <div class="gap-title">
 <h3>Priorités</h3>
 <span>Actions à traiter en premier</span>
 </div>

 <div class="gap-priority-mini">
 <div class="critical">
 <strong>Critique</strong>
 <span>Registre · Formalités APDP · Sécurité · Violations</span>
 </div>
 <div class="high">
 <strong>Haute</strong>
 <span>Sous-traitance · Droits · Transferts · Documentation</span>
 </div>
 <div class="medium">
 <strong>Moyenne</strong>
 <span>Reporting · Gouvernance DPO</span>
 </div>
 </div>
 </div>

 <div class="page-card">
 <div class="gap-title">
 <h3>Feuille de route</h3>
 <span>Progression vers le niveau cible</span>
 </div>

 <div class="gap-roadmap-mini">
 <div>
 <strong>Phase 1</strong>
 <span>Fondations et structuration</span>
 <small>M+1 → M+3</small>
 </div>
 <div>
 <strong>Phase 2</strong>
 <span>Déploiement des fonctionnalités</span>
 <small>M+4 → M+6</small>
 </div>
 <div>
 <strong>Phase 3</strong>
 <span>Consolidation et pilotage</span>
 <small>M+7 → M+10</small>
 </div>
 </div>
 </div>

 <div class="gap-note">
 <strong>Objectif :</strong>
 réduire les écarts de conformité et atteindre un niveau de maturité
 cible de 4 grâce à la centralisation, l'automatisation, le suivi
 et le pilotage apportés par ComplianceForge.
 </div>

 </div>
 `
 },

 risques: {
 title: "🛡️ Risques / EBIOS RM",
 subtitle: "Vue synthétique des risques ComplianceForge",
 content: `
 <div class="page-card">
 <div class="risk-title">
 <div>
 <h3>Parties prenantes</h3>
 <span>Niveau d’exposition et fiabilité cyber</span>
 </div>
 </div>

 <div class="stakeholder-table-wrap">
 <table class="stakeholder-table">
 <thead>
 <tr>
 <th>Réf.</th>
 <th>Partie prenante</th>
 <th>Catégorie</th>
 <th>Exposition</th>
 <th>Fiabilité</th>
 </tr>
 </thead>
 <tbody>
 <tr>
 <td>I1</td>
 <td>Direction / responsable du projet</td>
 <td>Interne</td>
 <td><strong>6</strong></td>
 <td><strong>9</strong></td>
 </tr>
 <tr>
 <td>I2</td>
 <td>Fonction sécurité / conformité</td>
 <td>Interne</td>
 <td><strong>6</strong></td>
 <td><strong>16</strong></td>
 </tr>
 <tr>
 <td>I3</td>
 <td>Équipe informatique</td>
 <td>Interne</td>
 <td><strong>12</strong></td>
 <td><strong>4</strong></td>
 </tr>
 <tr>
 <td>I4</td>
 <td>Utilisateurs de ComplianceForge</td>
 <td>Interne</td>
 <td><strong>6</strong></td>
 <td><strong>2</strong></td>
 </tr>
 <tr>
 <td>I5</td>
 <td>Administrateur applicatif</td>
 <td>Interne</td>
 <td><strong>12</strong></td>
 <td><strong>4</strong></td>
 </tr>
 <tr>
 <td>I6</td>
 <td>Utilisateur négligent ou malveillant</td>
 <td>Interne</td>
 <td><strong>9</strong></td>
 <td><strong>2</strong></td>
 </tr>
 <tr>
 <td>P1</td>
 <td>Prestataire technique</td>
 <td>Partenaire</td>
 <td><strong>6</strong></td>
 <td><strong>4</strong></td>
 </tr>
 <tr>
 <td>P2</td>
 <td>Fournisseur de services numériques</td>
 <td>Partenaire</td>
 <td><strong>6</strong></td>
 <td><strong>4</strong></td>
 </tr>
 <tr>
 <td>U1</td>
 <td>Responsable de traitement fictif</td>
 <td>Utilisateur</td>
 <td><strong>6</strong></td>
 <td><strong>2</strong></td>
 </tr>
 <tr>
 <td>U2</td>
 <td>Responsable conformité fictif</td>
 <td>Utilisateur</td>
 <td><strong>6</strong></td>
 <td><strong>4</strong></td>
 </tr>
 <tr>
 <td>A1</td>
 <td>APDP</td>
 <td>Autorité / référence</td>
 <td><strong>4</strong></td>
 <td><strong>16</strong></td>
 </tr>
 </tbody>
 </table>
 </div>

 <div class="stakeholder-legend">
 <span><strong>Exposition</strong> = D × P</span>
 <span><strong>Fiabilité</strong> = M × C</span>
 </div>
</div>

<div class="page-card">
 <div class="risk-title">
 <h3>Risques identifiés</h3>
 <span>Niveau initial → résiduel</span>
 </div>

 <div class="risk-list">

 <div class="risk-row">
 <div>
 <strong>R1</strong>
 <span>Compromission d’un compte par hameçonnage</span>
 </div>
 <b class="risk-critical">Critique → Moyen</b>
 </div>

 <div class="risk-row">
 <div>
 <strong>R2</strong>
 <span>Intrusion persistante et accès aux fonctions critiques</span>
 </div>
 <b class="risk-high">Très élevé → Faible</b>
 </div>

 <div class="risk-row">
 <div>
 <strong>R3</strong>
 <span>Compromission d’un accès de prestataire</span>
 </div>
 <b class="risk-high">Très élevé → Moyen</b>
 </div>

 <div class="risk-row">
 <div>
 <strong>R4</strong>
 <span>Abus de privilèges internes</span>
 </div>
 <b class="risk-critical">Critique → Moyen</b>
 </div>

 <div class="risk-row">
 <div>
 <strong>R5</strong>
 <span>Compromission d’identifiants / hameçonnage</span>
 </div>
 <b class="risk-high">Très élevé → Faible</b>
 </div>

 <div class="risk-row">
 <div>
 <strong>R6</strong>
 <span>Abus de privilèges ou mauvaise configuration</span>
 </div>
 <b class="risk-high">Très élevé → Moyen</b>
 </div>

 </div>
 </div>

 <div class="page-card">
 <div class="risk-title">
 <h3>Principaux scénarios</h3>
 </div>

 <div class="risk-scenario-grid">
 <div>
 <strong>Accès compromis</strong>
 <span>Hameçonnage et compromission de comptes.</span>
 </div>
 <div>
 <strong>Privilèges abusifs</strong>
 <span>Exfiltration ou modification non autorisée.</span>
 </div>
 <div>
 <strong>Accès tiers</strong>
 <span>Compromission d'un prestataire.</span>
 </div>
 <div>
 <strong>Configuration critique</strong>
 <span>Abus de privilèges ou mauvaise configuration.</span>
 </div>
 </div>
 </div>

 <div class="page-card">
 <div class="risk-title">
 <h3>Mesures prioritaires</h3>
 </div>

 <div class="risk-measures">
 <span>Authentification multifacteur</span>
 <span>Gestion des privilèges</span>
 <span>Journalisation et surveillance</span>
 <span>Contrôle des prestataires</span>
 <span>Sensibilisation au hameçonnage</span>
 <span>Sécurisation des configurations</span>
 </div>
 </div>

 <div class="risk-note">
 <strong>Résultat :</strong>
 après traitement, aucun des six risques ne demeure à un niveau
 critique ou très élevé. Les risques résiduels restent toutefois
 soumis à un suivi régulier.
 </div>

 </div>
 `
 },

 incidents: {
 title: "Incidents / Violations",
 subtitle: "Suivi des violations de données et du délai de notification",
 content: `
 <div class="page-card">
 <div class="page-card-header">
 <div>
 <h2>Incidents de sécurité</h2>
 <p>Suivi du workflow de notification sous 72 heures.</p>
 </div>
 <button class="btn-primary">+ Nouvel incident</button>
 </div>

 <div class="empty-state">
 <div></div>
 <h3>Gestion des incidents</h3>
 <p>Les incidents enregistrés et leur état de délai seront affichés ici.</p>
 </div>
 </div>
 `
 },

 documents: {
 title: "📁 Documents générés",
 subtitle: "Documents APDP préparés par ComplianceForge",
 content: `
 <div class="page-card">
 <h2>Documents</h2>
 <p>Les documents générés à partir des données saisies seront disponibles ici.</p>

 <div class="empty-state">
 <div></div>
 <h3>Aucun document affiché</h3>
 <p>Les documents apparaîtront ici après leur génération.</p>
 </div>
 </div>
 `
 }
};



/* Initialisation automatique du contexte APDP */
document.addEventListener("DOMContentLoaded", () => {
 setTimeout(() => {
 if (document.getElementById("apdp-organisation-select")) {
 initAPDPContextSelector();
 }
 }, 50);
});


function navigate(page) {
 const view = pages[page];

 if (!view) {
 return;
 }

 document.querySelector(".topbar-title").textContent = view.title;
 document.querySelector(".topbar-subtitle").textContent = view.subtitle;
 document.querySelector(".main-content").innerHTML = view.content;

 document.querySelectorAll(".nav-item").forEach(item => {
 item.classList.remove("active");

 if (item.dataset.page === page) {
 item.classList.add("active");
 }
 });

 if (page === "organisation") {
 bindOrganisationForm();
 }

 if (page === "profil") {
 bindProfilAPDPForm();
 }
 if (page === "registre") {
 bindTraitementForm();
 }

 if (page === "scoring") {
 loadScoringPage();
 }

}


window.navigate = navigate;


function getScoreValue(data, names) {
 if (!data || typeof data !== "object") {
 return null;
 }

 for (const name of names) {
 if (data[name] !== undefined && data[name] !== null) {
 return data[name];
 }
 }

 if (data.details && typeof data.details === "object") {
 for (const name of names) {
 if (
 data.details[name] !== undefined &&
 data.details[name] !== null
 ) {
 return data.details[name];
 }
 }
 }

 return null;
}

function formatScore(value) {
 if (value === null || value === undefined || value === "") {
 return "—";
 }

 if (typeof value === "number") {
 return Number.isInteger(value)
 ? String(value)
 : value.toFixed(1);
 }

 return String(value);
}

function calculateRiskLevel(value) {
 if (value === null || value === undefined || value === "") {
 return "—";
 }

 const score = Number(value);

 if (Number.isNaN(score)) {
 return String(value);
 }

 if (score >= 75) return "Critique";
 if (score >= 50) return "Élevé";
 if (score >= 25) return "Modéré";

 return "Faible";
}

async function calculateTreatmentScore(treatmentId) {

 const response = await fetch(
 `${API_BASE}/traitements/${treatmentId}/scores/calculer`,
 {
 method: "POST",
 headers: {
 "Content-Type": "application/json"
 }
 }
 );

 if (!response.ok) {
 let detail = "";
 try {
 const e = await response.json();
 detail = (typeof e.detail === "string") ? e.detail : JSON.stringify(e.detail);
 } catch (_) {}
 throw new Error(detail || `Erreur scoring HTTP ${response.status}`);
 }

 const data = await response.json();
 const c = data && data.conformite;
 const r = data && data.risque;
 const niveau = (r && r.niveau)
 ? String(r.niveau).charAt(0).toUpperCase() + String(r.niveau).slice(1)
 : undefined;

 return {
 ...data,
 conformite: (c && typeof c === "object") ? c.score_global : data.conformite,
 risque: (r && typeof r === "object") ? r.score_global : data.risque,
 niveau_risque: niveau || data.niveau_risque
 };
}

async function getTreatmentsForScoring() {

 const response =
 await fetch(`${API_BASE}/traitements`);

 if (!response.ok) {
 throw new Error(
 `Erreur traitements HTTP ${response.status}`
 );
 }

 const data = await response.json();

 if (Array.isArray(data)) {
 return data;
 }

 return (
 data.items ||
 data.data ||
 data.traitements ||
 []
 );
}

async function loadScoringPage() {

 const container =
 document.getElementById("scoring-container");

 if (!container) {
 return;
 }

 try {

 const treatments =
 await getTreatmentsForScoring();

 if (!treatments.length) {

 container.innerHTML = `
 <div class="empty-state">
 <div></div>
 <h3>Aucun traitement</h3>
 <p>
 Créez d'abord un traitement
 dans le registre.
 </p>
 </div>
 `;

 return;
 }

 let html = "";

 for (const treatment of treatments) {

 const id =
 treatment.id ||
 treatment.traitement_id;

 if (!id) continue;

 const name =
 treatment.nom_traitement ||
 treatment.nom ||
 treatment.name ||
 `Traitement #${id}`;

 try {

 const result =
 await calculateTreatmentScore(id);

 const conformity =
 getScoreValue(result, [
 "conformite",
 "score_conformite",
 "scoreConformite"
 ]);

 const risk =
 getScoreValue(result, [
 "risque",
 "score_risque",
 "scoreRisque"
 ]);

 const level =
 getScoreValue(result, [
 "niveau_risque",
 "niveauRisque",
 "niveau"
 ]) ||
 calculateRiskLevel(risk);

 html += `
 <div class="scoring-result-card">

 <div class="scoring-result-header">
 <div>
 <h3>${name}</h3>
 <p>Traitement #${id}</p>
 </div>
 </div>

 <div class="scoring-result-grid">

 <div class="scoring-result-item">
 <span>
 Score de conformité
 </span>
 <strong>
 ${formatScore(conformity)}
 </strong>
 </div>

 <div class="scoring-result-item">
 <span>
 Score de risque
 </span>
 <strong>
 ${formatScore(risk)}
 </strong>
 </div>

 <div class="scoring-result-item">
 <span>
 Niveau de risque
 </span>
 <strong>
 ${level}
 </strong>
 </div>

 </div>

 </div>
 `;

 } catch (error) {

 html += `
 <div class="scoring-result-card">
 <h3>${name}</h3>
 <p>
 Impossible de calculer le score :
 ${error.message}
 </p>
 </div>
 `;
 }
 }

 container.innerHTML = html;

 await loadDashboardScoring();

 } catch (error) {

 console.error(
 "Erreur Analyse / Scoring :",
 error
 );

 container.innerHTML = `
 <div class="empty-state">
 <div></div>
 <h3>Erreur de chargement</h3>
 <p>${error.message}</p>
 </div>
 `;
 }
}

async function loadDashboardScoring() {

 const conformity =
 document.getElementById(
 "dashboard-score-conformite"
 );

 if (!conformity) {
 return;
 }

 try {

 const treatments =
 await getTreatmentsForScoring();

 if (!treatments.length) {
 return;
 }

 const treatment =
 treatments[0];

 const id =
 treatment.id ||
 treatment.traitement_id;

 if (!id) {
 return;
 }

 const result =
 await calculateTreatmentScore(id);

 const conformityScore =
 getScoreValue(result, [
 "conformite",
 "score_conformite",
 "scoreConformite"
 ]);

 const riskScore =
 getScoreValue(result, [
 "risque",
 "score_risque",
 "scoreRisque"
 ]);

 const riskLevel =
 getScoreValue(result, [
 "niveau_risque",
 "niveauRisque",
 "niveau"
 ]) ||
 calculateRiskLevel(riskScore);

 const treatmentName =
 treatment.nom_traitement ||
 treatment.nom ||
 treatment.name ||
 `Traitement #${id}`;

 const riskElement =
 document.getElementById(
 "dashboard-score-risque"
 );

 const levelElement =
 document.getElementById(
 "dashboard-niveau-risque"
 );

 const treatmentElement =
 document.getElementById(
 "dashboard-traitement-score"
 );

 const statusElement =
 document.getElementById(
 "dashboard-scoring-status"
 );

 conformity.textContent =
 formatScore(conformityScore);

 if (riskElement) {
 riskElement.textContent =
 formatScore(riskScore);
 }

 if (levelElement) {
 levelElement.textContent =
 riskLevel;
 }

 if (treatmentElement) {
 treatmentElement.textContent =
 treatmentName;
 }

 if (statusElement) {
 statusElement.textContent =
 "Évaluation disponible";
 }

 } catch (error) {

 console.error(
 "Erreur scoring dashboard :",
 error
 );
 }
}

async function bindTraitementForm() {
 const form = document.getElementById("traitement-form");

 if (!form) {
 return;
 }

 const organisationSelect =
 document.getElementById("traitement-organisation");

 const categoriesContainer =
 document.getElementById("categories-donnees");

 const addCategoryButton =
 document.getElementById("ajouter-categorie");

 const message =
 document.getElementById("traitement-message");

 // Charger les organisations
 try {
 const response = await fetch(
 "https://api.complianceforge.test/organisations"
 );

 if (!response.ok) {
 throw new Error(
 "Impossible de récupérer les organisations."
 );
 }

 const organisations = await response.json();

 organisationSelect.innerHTML =
 '<option value="">Sélectionner une organisation</option>';

 organisations.forEach(organisation => {
 const option = document.createElement("option");

 option.value = organisation.id;
 option.textContent = organisation.nom;

 organisationSelect.appendChild(option);
 });

 if (organisations.length === 1) {
 organisationSelect.value = organisations[0].id;
 }

 } catch (error) {
 console.error("Erreur organisations :", error);

 organisationSelect.innerHTML =
 '<option value="">Erreur de chargement</option>';

 message.textContent =
 "Impossible de charger les organisations : " +
 error.message;

 message.className = "form-message error";

 return;
 }

 // Ajouter une catégorie
 addCategoryButton.addEventListener("click", () => {
 const row = document.createElement("div");

 row.className = "categorie-row";

 row.innerHTML = `
 <input
 type="text"
 class="categorie-nom"
 placeholder="Ex. Données financières"
 >

 <label class="checkbox-label">
 <input
 type="checkbox"
 class="categorie-sensible"
 >
 Donnée sensible
 </label>

 <button
 type="button"
 class="btn-secondary categorie-remove"
 >
 Supprimer
 </button>
 `;

 categoriesContainer.appendChild(row);
 });

 // Supprimer une catégorie
 categoriesContainer.addEventListener("click", event => {
 if (
 event.target.classList.contains("categorie-remove")
 ) {
 const rows =
 categoriesContainer.querySelectorAll(
 ".categorie-row"
 );

 // Garder au minimum une ligne
 if (rows.length > 1) {
 event.target.closest(".categorie-row").remove();
 }
 }
 });

 // Enregistrer le traitement
 form.addEventListener("submit", async event => {
 event.preventDefault();

 if (!organisationSelect.value) {
 message.textContent =
 "Veuillez sélectionner une organisation.";

 message.className = "form-message error";

 return;
 }

 const formData = new FormData(form);

 const data = {
 nom: formData.get("nom"),
 service_responsable:
 formData.get("service_responsable"),
 finalite: formData.get("finalite"),
 base_legale: formData.get("base_legale"),
 justification_base_legale:
 formData.get("justification_base_legale"),

 organisation_id:
 formData.get("organisation_id"),

 categories_donnees: [],

 sensibilite_donnees:
 formData.get("sensibilite_donnees"),

 niveau_mesures_securite:
 formData.get("niveau_mesures_securite"),

 sous_traitance_transferts:
 formData.get("sous_traitance_transferts"),

 exposition:
 formData.get("exposition"),

 volume:
 formData.get("volume")
 };

 // Transformer les valeurs de scoring en nombres
 const scoreFields = [
 "sensibilite_donnees",
 "niveau_mesures_securite",
 "sous_traitance_transferts",
 "exposition",
 "volume"
 ];

 scoreFields.forEach(field => {
 if (data[field] === "") {
 data[field] = null;
 } else if (data[field] !== null) {
 data[field] = Number(data[field]);
 }
 });

 // Récupérer les catégories
 const rows =
 categoriesContainer.querySelectorAll(
 ".categorie-row"
 );

 rows.forEach(row => {
 const input =
 row.querySelector(".categorie-nom");

 const checkbox =
 row.querySelector(".categorie-sensible");

 const categorie =
 input.value.trim();

 if (categorie) {
 data.categories_donnees.push({
 categorie: categorie,
 sensible: checkbox.checked
 });
 }
 });

 // Nettoyer les chaînes vides
 Object.keys(data).forEach(key => {
 if (
 typeof data[key] === "string" &&
 data[key].trim() === ""
 ) {
 data[key] = null;
 }
 });

 const submitButton =
 form.querySelector(
 'button[type="submit"]'
 );

 submitButton.disabled = true;
 submitButton.textContent =
 "Enregistrement...";

 try {
 const response = await fetch(
 "https://api.complianceforge.test/traitements",
 {
 method: "POST",
 headers: {
 "Content-Type": "application/json"
 },
 body: JSON.stringify(data)
 }
 );

 const result =
 await response.json();

 if (!response.ok) {
 const detail =
 result.detail
 ? typeof result.detail === "string"
 ? result.detail
 : JSON.stringify(result.detail)
 : "Erreur lors de l'enregistrement du traitement.";

 throw new Error(detail);
 }

 message.textContent =
 `Traitement « ${result.nom} » enregistré avec succès.`;

 message.className =
 "form-message success";

 console.log(
 "Traitement créé :",
 result
 );

 form.reset();

 organisationSelect.value =
 data.organisation_id;

 } catch (error) {
 console.error(
 "Erreur traitement :",
 error
 );

 message.textContent =
 "Impossible d'enregistrer le traitement : " +
 error.message;

 message.className =
 "form-message error";

 } finally {
 submitButton.disabled = false;

 submitButton.textContent =
 "Enregistrer le traitement";
 }
 });
}

async function bindProfilAPDPForm() {
 const form = document.getElementById("profil-apdp-form");

 if (!form) {
 return;
 }

 const organisationSelect =
 document.getElementById("profil-organisation");

 const message =
 document.getElementById("profil-apdp-message");

 try {
 const response = await fetch(
 "https://api.complianceforge.test/organisations"
 );

 if (!response.ok) {
 throw new Error("Impossible de récupérer les organisations.");
 }

 const organisations = await response.json();

 organisationSelect.innerHTML =
 '<option value="">Sélectionner une organisation</option>';

 organisations.forEach(organisation => {
 const option = document.createElement("option");

 option.value = organisation.id;
 option.textContent = organisation.nom;

 organisationSelect.appendChild(option);
 });

 if (organisations.length === 1) {
 organisationSelect.value = organisations[0].id;
 }

 } catch (error) {
 console.error("Erreur organisations :", error);

 organisationSelect.innerHTML =
 '<option value="">Erreur de chargement</option>';

 message.textContent =
 "Impossible de charger les organisations : " +
 error.message;

 message.className = "form-message error";

 return;
 }

 form.addEventListener("submit", async event => {
 event.preventDefault();

 if (!organisationSelect.value) {
 message.textContent =
 "Veuillez sélectionner une organisation.";

 message.className = "form-message error";
 return;
 }

 const formData = new FormData(form);
 const data = Object.fromEntries(formData.entries());

 const organisationId = data.organisation_id;

 delete data.organisation_id;

 for (const key of Object.keys(data)) {
 if (
 typeof data[key] === "string" &&
 data[key].trim() === ""
 ) {
 data[key] = null;
 }
 }

 const submitButton =
 form.querySelector('button[type="submit"]');

 submitButton.disabled = true;
 submitButton.textContent = "Enregistrement...";

 try {
 const response = await fetch(
 `https://api.complianceforge.test/apdp/organisations/${organisationId}/profil`,
 {
 method: "POST",
 headers: {
 "Content-Type": "application/json"
 },
 body: JSON.stringify({
 organisation_id: organisationId,
 ...data
 })
 }
 );

 const result = await response.json();

 if (!response.ok) {
 const detail = result.detail
 ? typeof result.detail === "string"
 ? result.detail
 : JSON.stringify(result.detail)
 : "Erreur lors de l'enregistrement du profil APDP.";

 throw new Error(detail);
 }

 message.textContent =
 "Profil APDP enregistré avec succès.";

 message.className = "form-message success";

 console.log("Profil APDP créé :", result);

 } catch (error) {
 console.error("Erreur profil APDP :", error);

 message.textContent =
 "Impossible d'enregistrer le profil APDP : " +
 error.message;

 message.className = "form-message error";

 } finally {
 submitButton.disabled = false;
 submitButton.textContent =
 "Enregistrer le profil APDP";
 }
 });
}


function bindOrganisationForm() {
 const form = document.getElementById("organisation-form");

 if (!form) {
 return;
 }

 form.addEventListener("submit", async event => {
 event.preventDefault();

 const message = document.getElementById("organisation-message");
 const submitButton = form.querySelector('button[type="submit"]');

 const formData = new FormData(form);
 const data = Object.fromEntries(formData.entries());

 for (const key of Object.keys(data)) {
 if (typeof data[key] === "string" && data[key].trim() === "") {
 data[key] = null;
 }
 }

 if (!data.nom) {
 message.textContent = "Le nom de l'organisation est obligatoire.";
 message.className = "form-message error";
 return;
 }

 submitButton.disabled = true;
 submitButton.textContent = "Enregistrement...";

 try {
 const response = await fetch(
 "https://api.complianceforge.test/organisations",
 {
 method: "POST",
 headers: {
 "Content-Type": "application/json"
 },
 body: JSON.stringify(data)
 }
 );

 const result = await response.json();

 if (!response.ok) {
 const detail = result.detail
 ? typeof result.detail === "string"
 ? result.detail
 : JSON.stringify(result.detail)
 : "Erreur lors de la création de l'organisation.";

 throw new Error(detail);
 }

 message.textContent =
 `Organisation « ${result.nom} » enregistrée avec succès.`;

 message.className = "form-message success";

 form.reset();

 console.log("Organisation créée :", result);

 } catch (error) {
 console.error("Erreur API :", error);

 message.textContent =
 `Impossible d'enregistrer l'organisation : ${error.message}`;

 message.className = "form-message error";

 } finally {
 submitButton.disabled = false;
 submitButton.textContent = "Enregistrer l'organisation";
 }
 });
}

document.addEventListener("DOMContentLoaded", () => {
 document.querySelectorAll(".nav-item").forEach(item => {
 item.addEventListener("click", () => {
 navigate(item.dataset.page);
 });
 });
});
/* ============================================================
 * DOSSIER GLOBAL APDP
 * Les données communes aux 8 formulaires sont saisies une fois
 * puis réutilisées automatiquement.
 * ============================================================ */
window.apdpDossier = JSON.parse(
 localStorage.getItem("apdpDossier") || "{}"
);

function saveAPDPDossier(dossier) {
 window.apdpDossier = dossier || {};
 localStorage.setItem(
 "apdpDossier",
 JSON.stringify(window.apdpDossier)
 );
}

function getAPDPDossier() {
 return window.apdpDossier || {};
}

function updateAPDPCommonData(documentId, data) {
 const dossier = getAPDPDossier();

 const aliases = {
 "formulaire_unique.1.nom_prenoms_raison_sociale":
 "responsable_traitement.nom_prenoms_raison_sociale",
 "formulaire_unique.1.npi_rccm":
 "responsable_traitement.npi_rccm",
 "formulaire_unique.1.carre_lot":
 "responsable_traitement.carre_lot",
 "formulaire_unique.1.quartier":
 "responsable_traitement.quartier",
 "formulaire_unique.1.ville":
 "responsable_traitement.ville",
 "formulaire_unique.1.adresse_postale":
 "responsable_traitement.adresse_postale",
 "formulaire_unique.1.adresse_electronique":
 "responsable_traitement.adresse_electronique",
 "formulaire_unique.1.contact_telephonique":
 "responsable_traitement.contact_telephonique",
 "formulaire_unique.1.autres_contacts":
 "responsable_traitement.autres_contacts",
 "formulaire_unique.1.activite":
 "responsable_traitement.activite",

 "formulaire_unique.2.origine_donnees":
 "traitement.origine_donnees",
 "formulaire_unique.2.nombre_personnes":
 "traitement.nombre_personnes",
 "formulaire_unique.2.caracteristiques_techniques":
 "traitement.caracteristiques_techniques",
 "formulaire_unique.2.fonctionnalites_systeme":
 "traitement.fonctionnalites_systeme",

 "formulaire_unique.3.duree_conservation":
 "traitement.duree_conservation",
 "formulaire_unique.3.texte_legal_conservation":
 "traitement.texte_legal_conservation"
 };

 const prefix = documentId + ".";
 
 Object.entries(aliases).forEach(([source, target]) => {
 if (!source.startsWith(prefix)) return;

 const field = source.slice(prefix.length);

 if (
 Object.prototype.hasOwnProperty.call(data, field) &&
 data[field] !== "" &&
 data[field] !== null &&
 data[field] !== undefined
 ) {
 setNestedAPDPValue(dossier, target, data[field]);
 }
 });

 saveAPDPDossier(dossier);
}

function setNestedAPDPValue(root, path, value) {
 const parts = path.split(".");
 let obj = root;

 for (let i = 0; i < parts.length - 1; i++) {
 if (!obj[parts[i]] || typeof obj[parts[i]] !== "object") {
 obj[parts[i]] = {};
 }
 obj = obj[parts[i]];
 }

 obj[parts[parts.length - 1]] = value;
}

/* ============================================================ */


/* ============================================================
 * SÉLECTION ORGANISATION / TRAITEMENT APDP
 * ============================================================ */

async function initAPDPContextSelector() {

 const organisationSelect =
 document.getElementById(
 "apdp-organisation-select"
 );

 const traitementSelect =
 document.getElementById(
 "apdp-traitement-select"
 );

 const message =
 document.getElementById(
 "apdp-context-message"
 );

 if (!organisationSelect || !traitementSelect) {
 return;
 }

 try {

 const response = await fetch(
 "https://api.complianceforge.test/organisations"
 );

 if (!response.ok) {
 throw new Error(
 `Erreur chargement organisations (${response.status})`
 );
 }

 const organisations =
 await response.json();

 organisationSelect.innerHTML =
 `<option value="">Sélectionner une organisation</option>`;

 organisations.forEach(org => {

 const option =
 document.createElement("option");

 option.value = org.id;
 option.textContent = org.nom;

 organisationSelect.appendChild(option);
 });

 const savedOrganisation =
 localStorage.getItem(
 "complianceForgeOrganisationId"
 );

 const savedTraitement =
 localStorage.getItem(
 "complianceForgeTraitementId"
 );

 if (savedOrganisation) {

 organisationSelect.value =
 savedOrganisation;

 await loadAPDPTreatments(
 savedOrganisation,
 savedTraitement
 );
 }

 } catch (error) {

 console.error(
 "Erreur chargement organisations APDP :",
 error
 );

 message.className =
 "form-message error";

 message.textContent =
 error.message;
 }

 organisationSelect.addEventListener(
 "change",
 async function() {

 const organisationId =
 this.value;

 traitementSelect.innerHTML =
 `<option value="">
 Sélectionnez un traitement
 </option>`;

 traitementSelect.disabled =
 !organisationId;

 if (!organisationId) {

 localStorage.removeItem(
 "complianceForgeOrganisationId"
 );

 localStorage.removeItem(
 "complianceForgeTraitementId"
 );

 return;
 }

 localStorage.setItem(
 "complianceForgeOrganisationId",
 organisationId
 );

 await loadAPDPTreatments(
 organisationId,
 null
 );
 }
 );

 traitementSelect.addEventListener(
 "change",
 function() {

 const traitementId =
 this.value;

 if (!traitementId) {
 return;
 }

 setComplianceForgeContext(
 organisationSelect.value,
 traitementId
 );

 message.className =
 "form-message success";

 message.textContent =
 " Traitement sélectionné. Les formulaires APDP utiliseront automatiquement ses informations.";
 }
 );
}


async function loadAPDPTreatments(
 organisationId,
 selectedTreatmentId = null
) {

 const select =
 document.getElementById(
 "apdp-traitement-select"
 );

 if (!select) {
 return;
 }

 select.disabled = true;

 select.innerHTML =
 `<option value="">
 Chargement des traitements...
 </option>`;

 try {

 const response = await fetch(
 `https://api.complianceforge.test/traitements?organisation_id=${encodeURIComponent(organisationId)}`
 );

 if (!response.ok) {
 throw new Error(
 `Erreur chargement traitements (${response.status})`
 );
 }

 const traitements =
 await response.json();

 select.innerHTML =
 `<option value="">
 Sélectionner un traitement
 </option>`;

 traitements.forEach(traitement => {

 const option =
 document.createElement("option");

 option.value =
 traitement.id;

 option.textContent =
 traitement.nom;

 select.appendChild(option);
 });

 select.disabled =
 traitements.length === 0;

 if (selectedTreatmentId) {

 const exists =
 traitements.some(
 t => t.id === selectedTreatmentId
 );

 if (exists) {

 select.value =
 selectedTreatmentId;

 setComplianceForgeContext(
 organisationId,
 selectedTreatmentId
 );
 }
 }

 const message =
 document.getElementById(
 "apdp-context-message"
 );

 if (message) {

 if (!traitements.length) {

 message.className =
 "form-message error";

 message.textContent =
 "Aucun traitement n'est enregistré pour cette organisation.";

 } else {

 message.className =
 "form-message";

 message.textContent =
 `${traitements.length} traitement(s) disponible(s).`;
 }
 }

 } catch (error) {

 console.error(
 "Erreur chargement traitements APDP :",
 error
 );

 select.innerHTML =
 `<option value="">
 Erreur de chargement
 </option>`;

 const message =
 document.getElementById(
 "apdp-context-message"
 );

 if (message) {

 message.className =
 "form-message error";

 message.textContent =
 error.message;
 }
 }
}


/* ============================================================
 * CONTEXTE MÉTIER APDP
 * Organisation -> Traitement -> APDP
 * ============================================================ */

window.complianceForgeContext = {
 organisationId:
 localStorage.getItem("complianceForgeOrganisationId") || null,

 traitementId:
 localStorage.getItem("complianceForgeTraitementId") || null
};

function setComplianceForgeContext(organisationId, traitementId) {

 window.complianceForgeContext = {
 organisationId: organisationId || null,
 traitementId: traitementId || null
 };

 if (organisationId) {
 localStorage.setItem(
 "complianceForgeOrganisationId",
 organisationId
 );
 }

 if (traitementId) {
 localStorage.setItem(
 "complianceForgeTraitementId",
 traitementId
 );
 }
}

async function getTraitementContext() {

 const traitementId =
 window.complianceForgeContext?.traitementId ||
 localStorage.getItem("complianceForgeTraitementId");

 if (!traitementId) {
 return null;
 }

 const response = await fetch(
 `https://api.complianceforge.test/traitements/${traitementId}`
 );

 if (!response.ok) {
 throw new Error(
 `Impossible de récupérer le traitement (${response.status})`
 );
 }

 return await response.json();
}

async function getOrganisationContext(organisationId) {

 if (!organisationId) {
 return null;
 }

 const response = await fetch(
 `https://api.complianceforge.test/organisations/${organisationId}`
 );

 if (!response.ok) {
 return null;
 }

 return await response.json();
}

async function getAPDPContextFromTreatment(traitement) {

 if (!traitement?.id) {
 return {};
 }

 const context = {
 organisation: {},
 traitement: {},
 apdp: {},
 profil_apdp: {}
 };

 if (traitement.organisation_id) {

 const organisation =
 await getOrganisationContext(
 traitement.organisation_id
 );

 if (organisation) {
 context.organisation = organisation;
 }

 /*
  * Profil APDP de l'organisation.
  * Les informations du responsable du traitement et du
  * représentant légal sont enregistrées une seule fois
  * dans le Profil APDP.
  */

 try {

 const profilResponse = await fetch(
 `https://api.complianceforge.test/apdp/organisations/${traitement.organisation_id}/profil`
 );

 if (profilResponse.ok) {

 context.profil_apdp =
 await profilResponse.json();

 }

 } catch (error) {

 console.warn(
 "Aucun Profil APDP disponible pour cette organisation.",
 error
 );

 }

 }

 context.traitement = traitement;

 try {

 const response = await fetch(
 `https://api.complianceforge.test/apdp/traitements/${traitement.id}`
 );

 if (response.ok) {
 context.apdp = await response.json();
 }

 } catch (error) {

 console.warn(
 "Aucune information APDP existante pour ce traitement.",
 error
 );
 }

 return context;
}



function buildAPDPDossierFromContext(context) {

 const dossier = {};

 const organisation = context?.organisation || {};
 const traitement = context?.traitement || {};
 const apdp = context?.apdp || {};
 const profilAPDP = context?.profil_apdp || {};

 /* Organisation */

 setNestedAPDPValue(
 dossier,
 "responsable_traitement.nom_prenoms_raison_sociale",
 organisation.nom
 );

 setNestedAPDPValue(
 dossier,
 "responsable_traitement.npi_rccm",
 organisation.ifu_rccm
 );

 setNestedAPDPValue(
 dossier,
 "responsable_traitement.adresse_postale",
 organisation.adresse
 );

 setNestedAPDPValue(
 dossier,
 "responsable_traitement.adresse_electronique",
 organisation.contact_dpo_email
 );

 setNestedAPDPValue(
 dossier,
 "responsable_traitement.secteur_activite",
 organisation.secteur_activite
 );

 /*
 * ==========================================================
 * PROFIL APDP
 * ==========================================================
 * Les informations déjà saisies dans Profil APDP sont
 * réutilisées automatiquement.
 *
 * Elles restent dans le dossier global afin d'être utilisées
 * lors de la génération du PDF officiel.
 * ==========================================================
 */

 const profilResponsable = {
 nom_prenoms_raison_sociale:
 profilAPDP.nom_prenoms_raison_sociale,

 npi_rccm:
 profilAPDP.npi_rccm,

 carre_lot:
 profilAPDP.carre_lot,

 quartier:
 profilAPDP.quartier,

 ville:
 profilAPDP.ville,

 adresse_postale:
 profilAPDP.adresse_postale,

 adresse_electronique:
 profilAPDP.adresse_electronique,

 contact_telephonique:
 profilAPDP.contact_telephonique,

 autres_contacts:
 profilAPDP.autres_contacts,

 activite:
 profilAPDP.activite
 };

 Object.entries(profilResponsable).forEach(
 ([key, value]) => {

 if (
 value !== null &&
 value !== undefined &&
 String(value).trim() !== ""
 ) {

 setNestedAPDPValue(
 dossier,
 `responsable_traitement.${key}`,
 value
 );

 }

 }
 );

 const profilRepresentant = {
 nom_prenoms:
 profilAPDP.representant_legal_nom_prenoms,

 npi:
 profilAPDP.representant_legal_npi,

 contacts:
 profilAPDP.representant_legal_contacts,

 adresse:
 profilAPDP.representant_legal_adresse
 };

 Object.entries(profilRepresentant).forEach(
 ([key, value]) => {

 if (
 value !== null &&
 value !== undefined &&
 String(value).trim() !== ""
 ) {

 setNestedAPDPValue(
 dossier,
 `representant_legal.${key}`,
 value
 );

 }

 }
 );

 /* Traitement */

 setNestedAPDPValue(
 dossier,
 "traitement.nom",
 traitement.nom
 );

 setNestedAPDPValue(
 dossier,
 "traitement.finalite",
 traitement.finalite
 );

 setNestedAPDPValue(
 dossier,
 "traitement.base_legale",
 traitement.base_legale
 );

 setNestedAPDPValue(
 dossier,
 "traitement.justification_base_legale",
 traitement.justification_base_legale
 );

 /* Informations APDP existantes */

 Object.entries(apdp).forEach(([key, value]) => {

 if (
 key === "id" ||
 key === "traitement_id" ||
 value === null ||
 value === undefined ||
 value === ""
 ) {
 return;
 }

 setNestedAPDPValue(
 dossier,
 `traitement.${key}`,
 value
 );
 });

 return dossier;
}


/* ============================================================
 * COMPLIANCEFORGE — INTERFACE APDP MÉTIER
 *
 * L'ordre de l'interface est indépendant du PDF.
 * Les clés APDP restent inchangées pour la génération.
 * ============================================================ */

const APDP_UI_GROUPS = {

 responsable: {
 title: "I. Responsable du traitement",
 icon: "",
 keywords: [
 "nom_prenoms_raison_sociale",
 "npi_rccm",
 "carre_lot",
 "quartier",
 "ville",
 "adresse_postale",
 "adresse_electronique",
 "contact_telephonique",
 "autres_contacts",
 "activite",
 "secteur"
 ]
 },

 representant: {
 title: "II. Représentant légal",
 icon: "",
 keywords: [
 "representant_legal",
 "nom_prenoms",
 "npi",
 "adresse_representant",
 "contact_representant"
 ]
 },

 traitement: {
 title: "III. Traitement",
 icon: "",
 keywords: [
 "nom_traitement",
 "traitement",
 "origine_donnees",
 "donnees_personnelles",
 "nombre_personnes",
 "caracteristiques_techniques",
 "fonctionnalites",
 "fonctionnalites_systeme",
 "procedure_manuelle",
 "procedure_automatisee",
 "type_video_photo",
 "type_site_web_application",
 "type_biometrique"
 ]
 },

 personnes: {
 title: "IV. Personnes concernées",
 icon: "",
 keywords: [
 "personnes_",
 "salaries",
 "adherents",
 "usagers",
 "visiteurs",
 "patients",
 "clients",
 "eleves",
 "etudiants",
 "enfants",
 "mineurs",
 "agents",
 "autres_personnes"
 ]
 },

 operations: {
 title: "V. Opérations réalisées",
 icon: "",
 keywords: [
 "operation_",
 "collecte",
 "developpement",
 "exposition",
 "affichage",
 "conservation",
 "copie",
 "traitement_image",
 "exploitation",
 "adaptation",
 "modification",
 "enregistrement",
 "extraction",
 "sauvegarde",
 "consultation",
 "utilisation",
 "communication_transmission",
 "diffusion",
 "structuration",
 "rapprochement",
 "interconnexion",
 "limitation",
 "cryptage",
 "effacement",
 "destruction",
 "organisation"
 ]
 },

 finalite: {
 title: "VI. Finalité et fondement juridique",
 icon: "",
 keywords: [
 "finalite",
 "base_legale",
 "justification_base_legale",
 "consentement",
 "obligation_legale",
 "mission_interet_public",
 "contrat",
 "interet_legitime",
 "interets_vitaux",
 "licéite",
 "liciete"
 ]
 },

 conservation: {
 title: "VII. Conservation et stockage",
 icon: "🗄️",
 keywords: [
 "duree_conservation",
 "conservation",
 "texte_legal_conservation",
 "support_",
 "papier",
 "numerique",
 "lieu_stockage",
 "modalites_stockage",
 "responsable_stockage",
 "stockage_",
 "cloud",
 "nas",
 "lvm"
 ]
 },

 partage: {
 title: "VIII. Partage des données",
 icon: "",
 keywords: [
 "sous_traitance",
 "communication",
 "interconnexion",
 "transfert",
 "destinataire",
 "pays_tiers",
 "autorisation_annexe",
 "annexe"
 ]
 },

 information: {
 title: "IX. Information et consentement",
 icon: "",
 keywords: [
 "information_prealable",
 "information_",
 "info_",
 "consentement_",
 "preuve_consentement",
 "mode_consentement",
 "modalites_consentement"
 ]
 },

 securite: {
 title: "X. Sécurité",
 icon: "",
 keywords: [
 "securite",
 "securite_",
 "personnes_autorisees",
 "protection_",
 "politique_acces",
 "acces_",
 "mesures_",
 "incendie",
 "inondation",
 "surtension",
 "magnetique",
 "organisationnelles",
 "logiques",
 "tests",
 "certifications",
 "verification_identite",
 "journalisation",
 "authentification",
 "chiffrement",
 "sensibilisation",
 "confidentialite",
 "integrite",
 "disponibilite",
 "sauvegardes",
 "continuite",
 "architecture_reseau"
 ]
 },

 droits: {
 title: "XI. Droits des personnes",
 icon: "⚖️",
 keywords: [
 "droit_",
 "droits_",
 "acces_personne",
 "portabilite",
 "opposition",
 "retrait",
 "interrogation",
 "rectification",
 "suppression",
 "oubli",
 "modalites_exercice"
 ]
 },

 anterieurs: {
 title: "XII. Formalités et suivi",
 icon: "",
 keywords: [
 "traitements_anterieurs",
 "traitement_anterieur",
 "registre",
 "dpo",
 "formalites",
 "reference"
 ]
 },

 declaration: {
 title: "XIII. Déclaration",
 icon: "✍️",
 keywords: [
 "declaration",
 "honneur",
 "nom_prenom",
 "fonction",
 "date"
 ]
 },

 autre: {
 title: "Informations complémentaires",
 icon: "➕",
 keywords: []
 }
};


function apdpNormalizeKey(value) {

 return String(value || "")
 .normalize("NFD")
 .replace(/[\u0300-\u036f]/g, "")
 .toLowerCase()
 .replace(/[^a-z0-9_]+/g, "_")
 .replace(/^_+|_+$/g, "");
}


function apdpFieldKey(field) {

 return apdpNormalizeKey(
 field.key ||
 field.name ||
 field.label ||
 ""
 );
}


function apdpFindGroup(field) {

 const key = apdpFieldKey(field);

 /*
 * Les règles spécifiques passent avant les règles générales.
 */

 if (
 key.startsWith("personnes_") ||
 key.includes("personnes_concernees") ||
 /(^|_)salaries$/.test(key) ||
 key.includes("adherents") ||
 key.includes("usagers") ||
 key.includes("visiteurs") ||
 key.includes("patients") ||
 key.includes("clients") ||
 key.includes("eleves") ||
 key.includes("etudiants")
 ) {
 return "personnes";
 }

 if (
 key.startsWith("operation_") ||
 key.includes("operations_")
 ) {
 return "operations";
 }

 if (
 key === "support_papier" ||
 key === "support_numerique" ||
 key.includes("support_autre") ||
 key.includes("lieu_stockage") ||
 key.includes("modalites_stockage") ||
 key.includes("responsable_stockage") ||
 key.startsWith("stockage_")
 ) {
 return "conservation";
 }

 if (
 key.includes("acces_physique") ||
 key.includes("acces_electronique") ||
 key.includes("acces_autre") ||
 key.includes("modalite_acces")
 ) {
 return "securite";
 }

 if (
 key.includes("sous_traitance") ||
 key.includes("communication_donnees") ||
 key.includes("interconnexion") ||
 key.includes("transfert")
 ) {
 return "partage";
 }

 if (
 key.includes("information_prealable") ||
 key.startsWith("info_") ||
 key.startsWith("consentement")
 ) {
 return "information";
 }

 for (const [groupName, group] of Object.entries(APDP_UI_GROUPS)) {

 if (!group.keywords.length) {
 continue;
 }

 if (
 group.keywords.some(keyword =>
 key.includes(
 apdpNormalizeKey(keyword)
 )
 )
 ) {
 return groupName;
 }
 }

 return "autre";
}


function apdpFlattenFields(pages) {

 const result = [];

 pages.forEach(page => {

 (page.fields || []).forEach(field => {

 if (!field) return;

 /*
 * Les sections du schema restent utilisables.
 * On les transforme en champs normaux si nécessaire.
 */
 if (
 field.type === "section" &&
 Array.isArray(field.children)
 ) {

 field.children.forEach(child => {
 result.push({
 ...child,
 _sourcePage: page.page
 });
 });

 return;
 }

 result.push({
 ...field,
 _sourcePage: page.page
 });
 });
 });

 return result;
}



function apdpIsRepresentantLegal(field) {

    const values = [
        field && field.key,
        field && field.name,
        field && field.id,
        field && field.label
    ]
        .filter(value => value !== undefined && value !== null)
        .map(value =>
            String(value)
                .normalize("NFD")
                .replace(/[\u0300-\u036f]/g, "")
                .toLowerCase()
        );

    return values.some(value =>
        value.includes("representant_legal") ||
        value.includes("representant legal") ||
        value.includes("representantlegal")
    );
}


function apdpIsRepresentantField(field) {

    const values = [
        field && field.key,
        field && field.name,
        field && field.id,
        field && field.label,
        field && field.title
    ]
        .filter(v => v !== undefined && v !== null)
        .map(v =>
            String(v)
                .normalize("NFD")
                .replace(/[\u0300-\u036f]/g, "")
                .toLowerCase()
        );

    return values.some(value => {
        const compact = value
            .replace(/[\s_\-./]+/g, "");

        return (
            compact.includes("representant") ||
            compact.includes("representantlegal")
        );
    });
}

function apdpCreateLogicalPages(documentId, pages) {

    /*
     * ============================================================
     * CAS SPÉCIAL — ANNEXE 1 SOUS-TRAITANCE
     *
     * L'Annexe 1 possède sa propre structure métier officielle.
     * Elle ne doit PAS être passée dans APDP_UI_GROUPS
     * (responsable, traitement, personnes, opérations, etc.).
     *
     * Le mapping PDF backend reste inchangé.
     * ============================================================
     */


    /*
     * ============================================================
     * CAS SPÉCIAL — ANNEXE 2 COMMUNICATION
     *
     * Présentation métier indépendante de l'ordre du PDF.
     * Le mapping officiel reste inchangé côté backend.
     * ============================================================
     */

    if (documentId === "annexe_2_communication") {

        const fields = apdpFlattenFields(pages);
        const byKey = {};

        fields.forEach(field => {
            if (field && field.key) {
                byKey[field.key] = field;
            }
        });

        function annexe2Field(key, label, extra = {}) {
            const source = byKey[key];

            if (!source) {
                return null;
            }

            return {
                ...source,
                key: source.key || key,
                name: source.name || source.key || key,
                label: label || source.label || key,
                ...extra
            };
        }

        function annexe2Child(key, label, extra = {}) {
            const source = byKey[key];

            if (!source) {
                return null;
            }

            return {
                ...source,
                key: source.key || key,
                name: source.name || source.key || key,
                label: label || source.label || key,
                ...extra
            };
        }

        /*
         * I — DESTINATAIRES
         */

        const destinatairesBenin =
            annexe2Field(
                "destinataires_benin",
                "Destinataires situés au Bénin"
            );

        const destinatairesCedeao =
            annexe2Field(
                "destinataires_cedeao",
                "Destinataires situés dans un pays de la CEDEAO"
            );

        /*
         * II — FINALITÉ ET BASE
         */

        const finalite =
            annexe2Field(
                "finalite_communication",
                "Finalité de la communication"
            );

        const texteLegal =
            annexe2Field(
                "texte_legal_reglementaire",
                "Texte légal / réglementaire"
            );

        const baseCommunication =
            annexe2Field(
                "base_communication",
                "Base justifiant la communication"
            );

        const justification =
            annexe2Child(
                "base_communication.justification",
                "Justification"
            );

        /*
         * III — CONSENTEMENT
         */

        const consentement =
            annexe2Field(
                "consentement_prealable",
                "Consentement préalable",
                {
                    exclusive: true
                }
            );

        const methodeConsentement =
            annexe2Field(
                "methode_consentement",
                "Méthode d'obtention du consentement"
            );

        /*
         * IV — MODALITÉS
         */

        const modalites =
            annexe2Field(
                "modalites_communication",
                "Modalités de communication"
            );

        /*
         * V — SÉCURITÉ
         */

        const securite =
            annexe2Field(
                "mesures_securite_communication",
                "Mesures de sécurité de la communication"
            );

        /*
         * VI — INFORMATION PRÉALABLE
         */

        const informationSource =
            byKey["information_prealable"];

        let information = null;

        if (informationSource) {

            const informationChildren = [];

            const ouiNon =
                annexe2Child(
                    "information_prealable.oui_non",
                    "Les personnes concernées sont-elles informées ?",
                    {
                        exclusive: true
                    }
                );

            const contenu =
                annexe2Child(
                    "information_prealable.contenu",
                    "Contenu de l'information"
                );

            const modalitesInformation =
                annexe2Child(
                    "information_prealable.modalites",
                    "Modalités d'information"
                );

            const autresModalites =
                annexe2Child(
                    "information_prealable.autres_modalites",
                    "Autres modalités"
                );

            const preuve =
                annexe2Child(
                    "information_prealable.preuve",
                    "Preuve de l'information"
                );

            [
                ouiNon,
                contenu,
                modalitesInformation,
                autresModalites,
                preuve
            ].forEach(field => {
                if (field) {
                    informationChildren.push(field);
                }
            });

            information = {
                ...informationSource,
                key: "information_prealable",
                name: "information_prealable",
                label: "Information préalable",
                type: "section",
                children: informationChildren
            };
        }

        /*
         * VII — DÉCLARATION
         */

        const declarationSource =
            byKey["declaration_honneur"];

        let declaration = null;

        if (declarationSource) {

            const declarationFields = [];

            [
                ["declaration_honneur.nom_prenom", "Nom et prénom"],
                ["declaration_honneur.fonction", "Fonction"],
                ["declaration_honneur.date", "Date"]
            ].forEach(([key, label]) => {

                const child =
                    annexe2Child(key, label);

                if (child) {
                    declarationFields.push(child);
                }
            });

            /*
             * Si les champs sont déjà aplatis avec uniquement
             * nom_prenom / fonction / date, on récupère également
             * ces variantes.
             */

            if (!declarationFields.length) {

                [
                    ["nom_prenom", "Nom et prénom"],
                    ["fonction", "Fonction"],
                    ["date", "Date"]
                ].forEach(([key, label]) => {

                    const child =
                        annexe2Child(key, label);

                    if (child) {
                        declarationFields.push(child);
                    }
                });
            }

            declaration = {
                ...declarationSource,
                key: "declaration_honneur",
                name: "declaration_honneur",
                label: "Déclaration sur l'honneur",
                type: "declaration",
                fields: declarationFields
            };
        }

        return [
            {
                page: 1,
                title: "I. Destinataires",
                fields: [
                    destinatairesBenin,
                    destinatairesCedeao
                ].filter(Boolean)
            },

            {
                page: 2,
                title: "II. Finalité et base de la communication",
                fields: [
                    finalite,
                    texteLegal,
                    baseCommunication,
                    justification
                ].filter(Boolean)
            },

            {
                page: 3,
                title: "III. Consentement",
                fields: [
                    consentement,
                    methodeConsentement
                ].filter(Boolean)
            },

            {
                page: 4,
                title: "IV. Modalités de communication",
                fields: [
                    modalites
                ].filter(Boolean)
            },

            {
                page: 5,
                title: "V. Sécurité",
                fields: [
                    securite
                ].filter(Boolean)
            },

            {
                page: 6,
                title: "VI. Information préalable",
                fields: information
                    ? [information]
                    : []
            },

            {
                page: 7,
                title: "VII. Déclaration sur l'honneur",
                fields: declaration
                    ? [declaration]
                    : []
            }
        ];
    }

    if (documentId === "annexe_1_sous_traitance") {

        const fieldsByKey = {};

        pages.forEach(page => {
            (page.fields || []).forEach(field => {
                if (field && field.key) {
                    fieldsByKey[field.key] = field;
                }
            });
        });

        const annexe1Sections = [
            {
                key: "intervenants",
                title: "I. Intervenants au traitement"
            },
            {
                key: "donnees_acces_intervenant",
                title: "II. Données auxquelles l'intervenant a accès"
            },
            {
                key: "operations_sous_traitant",
                title: "III. Opérations effectuées / utilisations"
            },
            {
                key: "contrat_confidentialite",
                title: "IV. Contrat de confidentialité et garanties offertes"
            },
            {
                key: "personnes_informees",
                title: "V. Information des personnes impliquées"
            },
            {
                key: "mise_en_conformite_apdp",
                title: "VI. Mise en conformité auprès de l'APDP"
            },
            {
                key: "securite_sous_traitant",
                title: "VII. Sécurité organisée par le sous-traitant"
            },
            {
                key: "declaration_honneur",
                title: "VIII. Déclaration sur l'honneur"
            }
        ];

        const complete = annexe1Sections.every(
            section => fieldsByKey[section.key]
        );

        if (complete) {

            return annexe1Sections.map((section, index) => ({
                page: `annexe1-${index + 1}`,
                title: section.title,
                fields: [
                    {
                        ...fieldsByKey[section.key],
                        hideLabel: true
                    }
                ]
            }));
        }
    }

    /*
     * ============================================================
     * AUTRES FORMULAIRES
     * Le comportement générique existant reste inchangé.
     * ============================================================
     */

    const fields = apdpFlattenFields(pages);

    const groups = {};

    Object.keys(APDP_UI_GROUPS).forEach(key => {
        groups[key] = [];
    });

    fields.forEach(field => {

        /*
         * RÈGLE ABSOLUE :
         * tout champ "représentant" appartient au bloc II.
         */
        if (apdpIsRepresentantField(field)) {
            groups.representant.push(field);
            return;
        }

        const group = apdpFindGroup(field);

        groups[group].push(field);
    });

    /*
     * SÉCURITÉ :
     * le bloc I ne peut contenir aucun représentant,
     * même si apdpFindGroup() l'a classé comme responsable.
     */
    groups.responsable =
        groups.responsable.filter(field =>
            !apdpIsRepresentantField(field)
        );

    /*
     * Nettoyage des doublons dans le bloc II.
     */
    const seen = new Set();

    groups.representant =
        groups.representant.filter(field => {

            const key = String(
                field.key ||
                field.name ||
                field.id ||
                field.label ||
                ""
            );

            if (seen.has(key)) {
                return false;
            }

            seen.add(key);
            return true;
        });

    const orderedGroups = [
        "responsable",
        "representant",
        "traitement",
        "personnes",
        "operations",
        "finalite",
        "conservation",
        "partage",
        "information",
        "securite",
        "droits",
        "anterieurs",
        "declaration",
        "autre"
    ];

    const logicalPages = [];

    orderedGroups.forEach(groupName => {

        const groupFields = groups[groupName];

        if (!groupFields || !groupFields.length) {
            return;
        }

        const group = APDP_UI_GROUPS[groupName];

        logicalPages.push({
            page: `cf-${groupName}`,
            title: group.title,
            fields: groupFields
        });
    });

    return logicalPages.length
        ? logicalPages
        : pages;
}

function apdpRememberCurrentPage(container) {

 if (!container) return;

 container.querySelectorAll(
 "input, textarea, select"
 ).forEach(input => {

 if (!input.name) return;

 if (
 input.type === "checkbox" ||
 input.type === "radio"
 ) {

 window.apdpUIState[
 input.name
 ] = window.apdpUIState[
 input.name
 ] || {
 type: input.type,
 values: []
 };

 if (input.checked) {

 if (
 !window.apdpUIState[
 input.name
 ].values.includes(input.value)
 ) {
 window.apdpUIState[
 input.name
 ].values.push(input.value);
 }

 } else {

 window.apdpUIState[
 input.name
 ].values =
 window.apdpUIState[
 input.name
 ].values.filter(
 value =>
 value !== input.value
 );
 }

 return;
 }

 window.apdpUIState[
 input.name
 ] = {
 type: input.type,
 value: input.value
 };
 });
}


function apdpRestoreState(container) {

 if (!container) return;

 container.querySelectorAll(
 "input, textarea, select"
 ).forEach(input => {

 if (!input.name) return;

 const saved =
 window.apdpUIState[
 input.name
 ];

 if (!saved) return;

 if (
 input.type === "checkbox" ||
 input.type === "radio"
 ) {

 input.checked =
 Array.isArray(saved.values) &&
 saved.values.includes(
 input.value
 );

 } else {

 input.value =
 saved.value ?? "";
 }
 });
}


/* ============================================================
 * LIBELLÉS PROPRES
 * ============================================================ */

const APDP_LABELS = {

 personnes_salaries: "Salariés",
 personnes_adherents: "Adhérents",
 personnes_usagers: "Usagers",
 personnes_visiteurs: "Visiteurs",
 personnes_patients: "Patients",
 personnes_clients: "Clients",
 personnes_eleves_etudiants: "Élèves et étudiants",
 personnes_autres: "Autres",

 operation_collecte: "Collecte",
 operation_developpement: "Développement",
 operation_exposition_affichage: "Exposition et affichage",
 operation_conservation: "Conservation",
 operation_copie: "Copie",
 operation_traitement_image: "Traitement d’image",
 operation_exploitation: "Exploitation",
 operation_adaptation: "Adaptation",
 operation_modification: "Modification",
 operation_enregistrement: "Enregistrement",
 operation_extraction: "Extraction",
 operation_sauvegarde: "Sauvegarde",
 operation_consultation: "Consultation",
 operation_utilisation: "Utilisation",
 operation_communication_transmission: "Communication / transmission",
 operation_diffusion: "Diffusion",
 operation_structuration: "Structuration",
 operation_rapprochement_interconnexion:
 "Rapprochement / interconnexion",
 operation_limitation: "Limitation",
 operation_cryptage: "Cryptage",
 operation_effacement: "Effacement",
 operation_destruction: "Destruction",
 operation_organisation: "Organisation",

 acces_physique: "Accès physique",
 acces_electronique: "Accès électronique",
 acces_autre: "Autre",

 support_papier: "Papier",
 support_numerique: "Numérique",
 support_autre: "Autre",

 secteur_prive: "Privé",
 secteur_public: "Public",
 secteur_institutions_etrangeres:
 "Institutions étrangères",

 information_prealable_oui: "Oui",
 information_prealable_non: "Non",

 consentement_oui: "Oui",
 consentement_non: "Non",

 sous_traitance_oui: "Oui",
 sous_traitance_non: "Non",

 communication_donnees_oui: "Oui",
 communication_donnees_non: "Non",

 interconnexion_oui: "Oui",
 interconnexion_non: "Non",

 transfert_pays_tiers_oui: "Oui",
 transfert_pays_tiers_non: "Non"
};


function apdpPrettyFieldLabel(field) {
    
    const _apdpRawKey = String(
        field.key ||
        field.name ||
        field.id ||
        ""
    )
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase();

    const _apdpRawLabel = String(
        field.label ||
        field.name ||
        ""
    );

    if (
        _apdpRawKey.includes("representant") ||
        _apdpRawLabel
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .toLowerCase()
            .includes("representant")
    ) {

        const _key = _apdpRawKey;

        if (
            _key.includes("nom_prenoms") ||
            _key.includes("nomprenoms")
        ) {
            return "Nom, Prénoms";
        }

        if (
            _key.includes("npi")
        ) {
            return "NPI";
        }

        if (
            _key.includes("carre_lot") ||
            _key.includes("carrelot")
        ) {
            return "Carré / Lot";
        }

        if (_key.includes("quartier")) {
            return "Quartier";
        }

        if (_key.includes("ville")) {
            return "Ville";
        }

        if (
            _key.includes("adresse_postale") ||
            _key.includes("adressepostale") ||
            _key.endsWith("_adresse")
        ) {
            return "Adresse postale";
        }

        if (
            _key.includes("adresse_electronique") ||
            _key.includes("adresseelectronique")
        ) {
            return "Adresse électronique";
        }

        if (
            _key.includes("contact_telephonique") ||
            _key.includes("contacttelephonique") ||
            _key.includes("_contact")
        ) {
            return "Contact téléphonique";
        }

        if (
            _key.includes("autres_contacts") ||
            _key.includes("autrescontacts")
        ) {
            return "Autres contacts";
        }
    }

 
 const rawKey = apdpNormalizeKey(
 field.key ||
 field.name ||
 ""
 );

 const isRepresentantLegal =
 rawKey.includes("representant_legal") ||
 rawKey.startsWith("representant_");

 if (isRepresentantLegal) {
 let representativeLabel =
 String(
 field.label ||
 field.name ||
 ""
 );

 representativeLabel = representativeLabel
 .replace(/^représentant\s+légal\s*/i, "")
 .replace(/^representant\s+legal\s*/i, "")
 .replace(/^représentant\s*/i, "")
 .replace(/^representant\s*/i, "")
 .trim();

 if (
 rawKey.includes(
 "representant_legal_nom_prenoms"
 ) ||
 rawKey.includes(
 "representant_nom_prenoms"
 )
 ) {
 return "Nom, Prénoms";
 }

 return representativeLabel;
 }


 const key =
 apdpNormalizeKey(
 field.key ||
 field.name ||
 ""
 );

 if (APDP_LABELS[key]) {
 return APDP_LABELS[key];
 }

 let label =
 field.label ||
 field.name ||
 key;

 label = String(label)
 .replace(/^Personnes?\s+/i, "")
 .replace(/^Personne\s+/i, "")
 .replace(/^Opérations?\s+/i, "")
 .replace(/^Operation\s+/i, "")
 .trim();

 return label;
}


/* ============================================================
 * STYLE
 * ============================================================ */

function injectAPDPBusinessStyles() {

 if (
 document.getElementById(
 "complianceforge-apdp-business-style"
 )
 ) {
 return;
 }

 const style =
 document.createElement("style");

 style.id =
 "complianceforge-apdp-business-style";

 style.textContent = `

 .apdp-page {
 max-width: 1100px;
 margin: 0 auto;
 }

 .apdp-page-title {
 padding: 20px 22px;
 margin-bottom: 18px;
 border-radius: 14px;
 background: linear-gradient(
 135deg,
 #f8fafc,
 #eef4ff
 );
 border: 1px solid #dce4f0;
 }

 .apdp-page-title h3 {
 margin: 0;
 font-size: 21px;
 color: #1f2937;
 }

 .apdp-business-group {
 margin: 0 0 22px;
 padding: 18px;
 border: 1px solid #e1e7ef;
 border-radius: 14px;
 background: #fff;
 }

 .apdp-business-group-title {
 margin: 0 0 12px;
 font-size: 16px;
 font-weight: 700;
 color: #263244;
 }

 .apdp-choice-grid {
 display: grid;
 grid-template-columns:
 repeat(auto-fit, minmax(190px, 1fr));
 gap: 10px;
 }

 .apdp-choice-card {
 display: flex;
 align-items: center;
 gap: 9px;
 min-height: 44px;
 padding: 10px 13px;
 border: 1px solid #d9e0ea;
 border-radius: 10px;
 background: #fff;
 cursor: pointer;
 transition:
 border-color .15s ease,
 background .15s ease,
 box-shadow .15s ease;
 }

 .apdp-choice-card:hover {
 border-color: #7aa2e8;
 background: #f8fbff;
 }

 .apdp-choice-card:has(input:checked) {
 border-color: #2563eb;
 background: #eff6ff;
 box-shadow:
 0 2px 5px rgba(
 37,
 99,
 235,
 .10
 );
 }

 .apdp-choice-card input {
 width: 17px;
 height: 17px;
 margin: 0;
 flex: 0 0 auto;
 }

 .apdp-field label {
 font-weight: 600;
 }

 .apdp-field {
 margin-bottom: 15px;
 }

 .apdp-form-navigation {
 position: sticky;
 bottom: 0;
 z-index: 10;
 margin-top: 20px;
 padding: 14px;
 border-top: 1px solid #dfe5ee;
 background: rgba(
 255,
 255,
 255,
 .96
 );
 backdrop-filter: blur(8px);
 }

 `;

 document.head.appendChild(style);
}

injectAPDPBusinessStyles();


async function openAPDPForm(documentId) {

 const container = document.querySelector('.main-content');

 if (!container) {
 console.error('Conteneur .main-content introuvable');
 return;
 }

 /* ========================================================
 * CHARGEMENT DU TRAITEMENT MÉTIER
 * ======================================================== */

 try {

 const traitementContext =
 await getTraitementContext();

 if (!traitementContext) {

 container.innerHTML = `
 <div class="form-message error">
 <strong>⚠ Aucun traitement sélectionné</strong>
 <p>
 Sélectionnez d'abord un traitement dans le registre
 avant de préparer un formulaire APDP.
 </p>

 <button
 type="button"
 class="btn-primary"
 onclick="navigate('registre')">
 Aller au registre des traitements
 </button>
 </div>
 `;

 return;
 }

 const metierDossier =
 await getAPDPContextFromTreatment(
 traitementContext
 );

 const ancienDossier =
 getAPDPDossier();

 const dossierMetier =
 buildAPDPDossierFromContext(
 metierDossier
 );

 /*
 * Les informations métier deviennent prioritaires.
 * Les informations complémentaires déjà saisies restent
 * conservées.
 */

 const nouveauDossier = {
 ...ancienDossier,
 ...dossierMetier
 };

 saveAPDPDossier(nouveauDossier);

 } catch (error) {

 console.error(
 "Erreur chargement contexte APDP :",
 error
 );

 container.innerHTML = `
 <div class="form-message error">
 <strong>Erreur de chargement du traitement</strong>
 <p>${error.message}</p>
 </div>
 `;

 return;
 }


 if (!container) {
 console.error('Conteneur .main-content introuvable');
 return;
 }

 container.innerHTML = `
 <div class="apdp-loading">
 <h2>Formulaire APDP</h2>
 <p>Chargement du formulaire...</p>
 </div>
 `;

 try {
 const response = await fetch(
 `https://api.complianceforge.test/apdp/formulaires/${documentId}/schema`
 );

 if (!response.ok) {
 throw new Error(`Erreur HTTP ${response.status}`);
 }

 const schema = await response.json();

 if (!schema.pages || !schema.pages.length) {
 throw new Error("Aucune page disponible dans le formulaire.");
 }

 const sourcePages = schema.pages;

/*
 * L'utilisateur remplit une vue métier.
 * Le mapping PDF reste côté backend.
 */
const pages =
 apdpCreateLogicalPages(
 documentId,
 sourcePages
 );


/*
 * ============================================================
 * DÉCLARATION SUR L'HONNEUR
 *
 * La déclaration est saisie une seule fois dans le
 * Formulaire Unique.
 *
 * Pour les autres formulaires APDP, le bloc est masqué
 * dans l'interface afin d'éviter une saisie répétitive.
 *
 * IMPORTANT :
 * - le mapping PDF officiel n'est pas modifié ;
 * - les données existantes ne sont pas supprimées ;
 * - seule l'affichage utilisateur est filtré.
 * ============================================================
 */

if (documentId !== "formulaire_unique") {

    pages.forEach(page => {

        if (!page || !Array.isArray(page.fields)) {
            return;
        }

        page.fields = page.fields.filter(field => {

            if (!field) {
                return true;
            }

            const key =
                String(
                    field.key ||
                    field.name ||
                    ""
                ).toLowerCase();

            return !(
                key === "declaration_honneur" ||
                key.endsWith(".declaration_honneur")
            );
        });
    });

    /*
     * Supprime également les pages devenues vides après
     * le retrait de la déclaration.
     */
    for (let i = pages.length - 1; i >= 0; i--) {

        if (
            pages[i] &&
            Array.isArray(pages[i].fields) &&
            pages[i].fields.length === 0
        ) {
            pages.splice(i, 1);
        }
    }
}


 // Conserve les définitions de champs du schema pour la
 // conversion des choix radio vers les clés du PDF officiel.
 window.apdpSchemaFields = {};

 pages.forEach(page => {
 (page.fields || []).forEach(field => {
 if (field && field.key) {
 window.apdpSchemaFields[field.key] = field;
 }
 });
 });

 let currentPage = 0;

 container.innerHTML = `
 <div class="apdp-form-container">

 <div class="apdp-form-header">
 <h2>${schema.title || 'Formulaire APDP'}</h2>

 <div class="apdp-progress-info">
 <span id="apdp-page-number">Page 1 / ${pages.length}</span>
 </div>

 <div class="apdp-progress">
 <div id="apdp-progress-bar"></div>
 </div>
 </div>

 <form id="apdp-dynamic-form">

 <div id="apdp-page-container"></div>

 <div class="apdp-navigation">
 <button
 type="submit"
 id="apdp-generate"
 class="btn btn-success">
 Générer le PDF
 </button>
 </div>

 </form>
 </div>
 `;

 const pageContainer = document.getElementById('apdp-page-container');
 const generateButton =
 document.getElementById('apdp-generate');
 const pageNumber = document.getElementById('apdp-page-number');
 const progressBar = document.getElementById('apdp-progress-bar');
 const form = document.getElementById('apdp-dynamic-form');

 function escapeHtml(value) {
 if (value === null || value === undefined) return '';

 return String(value)
 .replace(/&/g, '&amp;')
 .replace(/</g, '&lt;')
 .replace(/>/g, '&gt;')
 .replace(/"/g, '&quot;')
 .replace(/'/g, '&#039;');
 }

 function renderChoices(field) {
 if (!field.choices || !Array.isArray(field.choices)) {
 return '';
 }

 return field.choices.map(choice => {
 const value =
 typeof choice === 'object'
 ? (choice.value ?? choice.label ?? '')
 : choice;

 const label =
 typeof choice === 'object'
 ? (choice.label ?? choice.value ?? '')
 : choice;

 return `
 <option value="${escapeHtml(value)}">
 ${escapeHtml(label)}
 </option>
 `;
 }).join('');
 }


 /*
 * ============================================================
 * CHAMPS APDP AUTOMATIQUES
 *
 * Les informations déjà connues de l'organisation, du
 * traitement ou du dossier APDP ne sont pas redemandées.
 *
 * IMPORTANT :
 * - la valeur reste présente dans le DOM ;
 * - elle reste donc récupérable par generateAPDPDocument();
 * - seuls les champs réellement connus sont masqués.
 * ============================================================
 */

 function getNestedAPDPValue(root, path) {
 if (!root || !path) {
 return null;
 }

 const parts = path.split(".");
 let current = root;

 for (const part of parts) {
 if (
 current === null ||
 current === undefined ||
 typeof current !== "object" ||
 !(part in current)
 ) {
 return null;
 }

 current = current[part];
 }

 if (
 current === null ||
 current === undefined ||
 (typeof current === "string" && current.trim() === "")
 ) {
 return null;
 }

 return current;
 }

 function normalizeAPDPKey(value) {
 return String(value || "")
 .normalize("NFD")
 .replace(/[\u0300-\u036f]/g, "")
 .toLowerCase()
 .replace(/[^a-z0-9]+/g, "_")
 .replace(/^_+|_+$/g, "");
 }

 function getAPDPAutoValue(field) {
 if (!field) {
 return null;
 }

 const dossier =
 typeof getAPDPDossier === "function"
 ? getAPDPDossier()
 : (window.apdpDossier || {});

 const name = normalizeAPDPKey(field.name);
 const label = normalizeAPDPKey(field.label);

 /*
 * Valeurs provenant du responsable / de l'organisation.
 */
 const organisationPaths = {
 nom_prenoms_raison_sociale: [
 "responsable_traitement.nom_prenoms_raison_sociale",
 "organisation.nom",
 "organisation.nom_prenoms_raison_sociale"
 ],

 npi_rccm: [
 "responsable_traitement.npi_rccm",
 "organisation.ifu_rccm",
 "organisation.npi_rccm"
 ],

 ifu_rccm: [
 "organisation.ifu_rccm",
 "responsable_traitement.npi_rccm"
 ],

 quartier: [
 "responsable_traitement.quartier",
 "organisation.quartier"
 ],

 ville: [
 "responsable_traitement.ville",
 "organisation.ville"
 ],

 adresse_postale: [
 "responsable_traitement.adresse_postale",
 "organisation.adresse"
 ],

 adresse: [
 "responsable_traitement.adresse_postale",
 "organisation.adresse"
 ],

 adresse_electronique: [
 "responsable_traitement.adresse_electronique",
 "organisation.contact_dpo_email"
 ],

 contact_telephonique: [
 "responsable_traitement.contact_telephonique",
 "organisation.contact",
 "organisation.contact_telephonique"
 ],

 contact: [
 "responsable_traitement.contact_telephonique",
 "organisation.contact",
 "organisation.contact_telephonique"
 ],

 activite: [
 "responsable_traitement.activite",
 "organisation.secteur_activite"
 ]
 };

 /*
 * Valeurs de la déclaration sur l'honneur.
 *
 * Ces informations sont reprises du Profil APDP lorsqu'elles
 * existent déjà dans le dossier.
 */
 const declarationPaths = {

 nom_prenom: [
 "declaration_honneur.nom_prenom",
 "representant_legal.nom_prenoms",
 "profil_apdp.representant_legal_nom_prenoms"
 ],

 fonction: [
 "declaration_honneur.fonction",
 "representant_legal.fonction",
 "profil_apdp.representant_legal_fonction"
 ],

 date: [
 "declaration_honneur.date"
 ]

 };

 /*
 * Valeurs provenant du traitement.
 */
 const declarationKey =
 name.includes("declaration") ||
 label.includes("declaration");

 if (declarationKey) {

 const declarationName =
 name
 .replace("declaration_honneur.", "")
 .replace("declaration.", "");

 const paths =
 declarationPaths[declarationName];

 if (Array.isArray(paths)) {

 for (const path of paths) {

 const value =
 getNestedAPDPValue(dossier, path);

 if (
 value !== undefined &&
 value !== null &&
 String(value).trim() !== ""
 ) {
 return value;
 }

 }

 }

 /*
  * La date de déclaration peut être proposée automatiquement.
  * Elle n'est ajoutée que si le champ est explicitement un champ
  * de date.
  */
 if (
 declarationName === "date" &&
 (
 field.type === "date" ||
 normalizeAPDPKey(field.label || "").includes("date")
 )
 ) {
 return new Date().toISOString().slice(0, 10);
 }

 }


 const traitementPaths = {
 nom_traitement: [
 "traitement.nom",
 "traitement.nom_traitement"
 ],

 traitement: [
 "traitement.nom",
 "traitement.nom_traitement"
 ],

 finalite: [
 "traitement.finalite"
 ],

 base_legale: [
 "traitement.base_legale"
 ],

 justification_base_legale: [
 "traitement.justification_base_legale"
 ],

 service_responsable: [
 "traitement.service_responsable"
 ],

 statut: [
 "traitement.statut"
 ],

 origine_donnees: [
 "traitement.origine_donnees"
 ],

 nombre_personnes: [
 "traitement.nombre_personnes"
 ],

 caracteristiques_techniques: [
 "traitement.caracteristiques_techniques"
 ],

 fonctionnalites_systeme: [
 "traitement.fonctionnalites_systeme"
 ],

 duree_conservation: [
 "traitement.duree_conservation"
 ],

 texte_legal_conservation: [
 "traitement.texte_legal_conservation"
 ]
 };

 /*
 * ============================================================
 * PROFIL APDP — REPRÉSENTANT LÉGAL
 * ============================================================
 * Ces informations sont déjà saisies dans Profil APDP.
 * Elles sont récupérées automatiquement et restent disponibles
 * pour la génération du PDF.
 */

 const profilRepresentantPaths = {

 representant_legal_nom_prenoms: [
   "representant_legal.nom_prenoms",
   "representant_legal.nom_prenoms_raison_sociale"
 ],

 representant_legal_npi: [
   "representant_legal.npi",
   "representant_legal.npi_rccm"
 ],

 representant_legal_contacts: [
   "representant_legal.contacts",
   "representant_legal.contact_representant"
 ],

 representant_legal_adresse: [
   "representant_legal.adresse",
   "representant_legal.adresse_representant"
 ],

 nom_prenoms: [
   "representant_legal.nom_prenoms",
   "representant_legal.nom_prenoms_raison_sociale"
 ],

 npi: [
   "representant_legal.npi",
   "representant_legal.npi_rccm"
 ],

 contact_representant: [
   "representant_legal.contacts",
   "representant_legal.contact_representant"
 ],

 adresse_representant: [
   "representant_legal.adresse",
   "representant_legal.adresse_representant"
 ]

 };

 /*
 * Cherche d'abord sur le nom exact du champ.
 */
 const candidates = [];

 for (const key of Object.keys(organisationPaths)) {
 if (name === normalizeAPDPKey(key) || label === normalizeAPDPKey(key)) {
 candidates.push(...organisationPaths[key]);
 }
 }

 for (const key of Object.keys(traitementPaths)) {
 if (name === normalizeAPDPKey(key) || label === normalizeAPDPKey(key)) {
 candidates.push(...traitementPaths[key]);
 }
 }

 /*
 * Recherche des informations du représentant légal
 * provenant du Profil APDP.
 */

 for (const key of Object.keys(profilRepresentantPaths)) {

 const normalizedKey =
 normalizeAPDPKey(key);

 if (
 name === normalizedKey ||
 label === normalizedKey
 ) {

 candidates.push(
   ...profilRepresentantPaths[key]
 );

 }

 }

 /*
 * Correspondance avec les noms utilisés par le Formulaire Unique.
 * Les données restent dans le dossier pour la génération PDF.
 */

 const representantFieldAliases = {
   nom_prenoms: [
     "representant_legal.nom_prenoms"
   ],
   npi: [
     "representant_legal.npi"
   ],
   adresse_representant: [
     "representant_legal.adresse"
   ],
   contact_representant: [
     "representant_legal.contacts"
   ]
 };

 for (const key of Object.keys(representantFieldAliases)) {

   const normalizedKey =
     normalizeAPDPKey(key);

   if (
     name === normalizedKey ||
     name.endsWith("_" + normalizedKey) ||
     label === normalizedKey
   ) {

     candidates.push(
       ...representantFieldAliases[key]
     );

   }
 }

 /*
 * Certains champs du formulaire unique possèdent un préfixe
 * de section, par exemple formulaire_unique.1.xxx.
 */
 for (const key of Object.keys(organisationPaths)) {
 const normalizedKey = normalizeAPDPKey(key);

 if (
 name.endsWith("_" + normalizedKey) ||
 name.includes("_" + normalizedKey + "_")
 ) {
 candidates.push(...organisationPaths[key]);
 }
 }

 for (const key of Object.keys(traitementPaths)) {
 const normalizedKey = normalizeAPDPKey(key);

 if (
 name.endsWith("_" + normalizedKey) ||
 name.includes("_" + normalizedKey + "_")
 ) {
 candidates.push(...traitementPaths[key]);
 }
 }

 /*
 * Recherche dans le dossier APDP.
 */
 for (const candidate of candidates) {
 const value = getNestedAPDPValue(dossier, candidate);

 if (
 value !== null &&
 value !== undefined &&
 String(value).trim() !== ""
 ) {
 return value;
 }
 }

 /*
 * Dernier recours : si le champ lui-même existe déjà
 * directement dans le dossier.
 */
 const directCandidates = [
 field.name,
 name
 ];

 for (const candidate of directCandidates) {
 const value = getNestedAPDPValue(dossier, candidate);

 if (
 value !== null &&
 value !== undefined &&
 String(value).trim() !== ""
 ) {
 return value;
 }
 }

 return null;
 }

 function renderAPDPAutoField(field, value) {
 const name = field.name || "";
 const label = field.label || name;

 let serializedValue = value;

 if (Array.isArray(value)) {
 serializedValue = value.join(", ");
 }

 if (typeof value === "object" && value !== null) {
 serializedValue = JSON.stringify(value);
 }

 return `
 <div
 class="apdp-field apdp-field-auto"
 data-apdp-auto="1"
 data-apdp-field="${escapeHtml(name)}"
 style="display:none;"
 >
 <input
 type="hidden"
 name="${escapeHtml(name)}"
 value="${escapeHtml(serializedValue)}"
 >
 </div>
 `;
 }


 
/* ============================================================
 * COMPLIANCEFORGE — LOGIQUE CONDITIONNELLE APDP
 * ============================================================ */


/* ============================================================
 * APDP — LOGIQUE CONDITIONNELLE
 *
 * Le schéma officiel regroupe les choix Oui/Non en radios.
 * Les champs dépendants sont affichés selon la réponse.
 * ============================================================ */

const APDP_CONDITIONAL_GROUPS = [
 {
 selector: "sous_traitance",
 yes: [
 "sous_traitance_annexe"
 ],
 no: []
 },
 {
 selector: "communication_donnees",
 yes: [
 "communication_benin_cedeao",
 "communication_annexe"
 ],
 no: []
 },
 {
 selector: "interconnexion",
 yes: [
 "interconnexion_annexe"
 ],
 no: []
 },
 {
 selector: "transfert_pays_tiers",
 yes: [
 "transfert_pays_tiers",
 "transfert_autorisation_annexe"
 ],
 no: []
 },
 {
 selector: "information_prealable",
 yes: [
 "info_affichage",
 "info_mentions_ecrites",
 "info_entretien",
 "info_courrier_electronique",
 "info_courrier_postal",
 "info_questionnaire",
 "info_mention_legale",
 "info_autres",
 "contenu_information_prealable",
 "preuve_information_prealable"
 ],
 no: [
 "situation_surete_etat",
 "situation_condamnations_penales",
 "situation_infraction",
 "situation_autres"
 ]
 },
 {
 selector: "consentement",
 yes: [
 "consentement_ecrit",
 "consentement_oral",
 "consentement_electronique",
 "consentement_autres",
 "consentement_prospection",
 "consentement_partage",
 "consentement_duree_conservation"
 ],
 no: [
 "exclusion_obligation_legale",
 "exclusion_mission_interet_public",
 "exclusion_contrat",
 "exclusion_interets_vitaux",
 "exclusion_autre_justification"
 ]
 },
 {
 selector: "securite_donnees",
 yes: [
 "securite_donnees_comment"
 ],
 no: [
 "securite_donnees_pourquoi"
 ]
 },
 {
 selector: "politique_acces",
 yes: [
 "politique_acces_description",
 "mesures_physique",
 "mesures_electronique",
 "mesures_autres",
 "acces_physique",
 "acces_electronique",
 "acces_autres",
 "incendie_extincteurs",
 "incendie_autres",
 "inondation_hygrometre",
 "surtensions_parafoudre",
 "surtensions_autres"
 ],
 no: [
 "politique_acces_pourquoi"
 ]
 }
];


function apdpGetFieldWrapper(key) {
 const input = document.querySelector(
 `[data-apdp-key="${key}"]`
 );

 if (input) {
 return input.closest(".apdp-field");
 }

 const named = document.querySelector(
 `input[name="${key}"], textarea[name="${key}"], select[name="${key}"]`
 );

 return named ? named.closest(".apdp-field") : null;
}


function apdpClearField(wrapper) {
 if (!wrapper) return;

 wrapper.querySelectorAll(
 "input, textarea, select"
 ).forEach(input => {
 if (
 input.type === "checkbox" ||
 input.type === "radio"
 ) {
 input.checked = false;
 } else {
 input.value = "";
 }
 });
}


function apdpShowField(key, visible) {
 const wrapper = apdpGetFieldWrapper(key);

 if (!wrapper) return;

 wrapper.style.display = visible ? "" : "none";

 if (!visible) {
 apdpClearField(wrapper);
 }
}


function apdpReadChoice(selector) {
 const checked = document.querySelector(
 `input[name="${selector}"]:checked`
 );

 return checked ? checked.value.toLowerCase() : null;
}


function apdpApplyConditionalRules() {
 APDP_CONDITIONAL_GROUPS.forEach(rule => {

 const choice = apdpReadChoice(rule.selector);

 const yesFields = rule.yes || [];
 const noFields = rule.no || [];

 yesFields.forEach(key => {
 apdpShowField(
 key,
 choice === "oui"
 );
 });

 noFields.forEach(key => {
 apdpShowField(
 key,
 choice === "non"
 );
 });
 });
}


function apdpBindConditionalRules() {

 APDP_CONDITIONAL_GROUPS.forEach(rule => {

 const inputs = document.querySelectorAll(
 `input[name="${rule.selector}"]`
 );

 inputs.forEach(input => {

 input.addEventListener(
 "change",
 () => {

 apdpBindConditionalRules();
 apdpApplyConditionalRules();

 }
 );

 });

 });
}


/* ============================================================
 * APDP — LIBELLÉS PROPRES
 * ============================================================ */

function apdpPrettyLabel(name, label) {

 const labels = {

 personnes_salaries:
 "Salariés",

 personnes_adherents:
 "Adhérents",

 personnes_usagers:
 "Usagers",

 personnes_visiteurs:
 "Visiteurs",

 personnes_patients:
 "Patients",

 personnes_clients:
 "Clients",

 personnes_eleves_etudiants:
 "Élèves et étudiants",

 personnes_autres:
 "Autres",

 operation_collecte:
 "Collecte",

 operation_developpement:
 "Développement",

 operation_exposition_affichage:
 "Exposition et affichage",

 operation_conservation:
 "Conservation",

 operation_copie:
 "Copie",

 operation_traitement_image:
 "Traitement d’image",

 operation_exploitation:
 "Exploitation",

 operation_adaptation:
 "Adaptation",

 operation_modification:
 "Modification",

 operation_enregistrement:
 "Enregistrement",

 operation_extraction:
 "Extraction",

 operation_sauvegarde:
 "Sauvegarde",

 operation_consultation:
 "Consultation",

 operation_utilisation:
 "Utilisation",

 operation_communication_transmission:
 "Communication / transmission",

 operation_communication_transmission_diffusion:
 "Communication / transmission / diffusion",

 operation_diffusion:
 "Diffusion",

 operation_structuration:
 "Structuration",

 operation_rapprochement_interconnexion:
 "Rapprochement / interconnexion",

 operation_structuration_rapprochement_interconnexion:
 "Structuration / rapprochement / interconnexion",

 operation_limitation:
 "Limitation",

 operation_cryptage:
 "Cryptage",

 operation_effacement:
 "Effacement",

 operation_destruction:
 "Destruction",

 operation_organisation:
 "Organisation",

 operation_autre:
 "Autre",

 info_affichage:
 "Affichage",

 info_mentions_ecrites:
 "Mentions écrites",

 info_entretien:
 "Entretien",

 info_courrier_electronique:
 "Courrier électronique",

 info_courrier_postal:
 "Courrier postal",

 info_questionnaire:
 "Questionnaire",

 info_mention_legale:
 "Mention légale",

 info_autres:
 "Autres",

 situation_surete_etat:
 "Sûreté de l'État, défense ou sécurité publique",

 situation_condamnations_penales:
 "Condamnations pénales ou mesures de sûreté",

 situation_infraction:
 "Prévention, recherche ou poursuite d'une infraction",

 situation_autres:
 "Autre situation",

 consentement_ecrit:
 "Écrit",

 consentement_oral:
 "Oral",

 consentement_electronique:
 "Acceptation électronique",

 consentement_autres:
 "Autre",

 consentement_prospection:
 "Prospection",

 consentement_partage:
 "Partage",

 consentement_duree_conservation:
 "Durée de conservation",

 exclusion_obligation_legale:
 "Obligation légale",

 exclusion_mission_interet_public:
 "Mission d'intérêt public",

 exclusion_contrat:
 "Contrat",

 exclusion_interets_vitaux:
 "Intérêts vitaux",

 exclusion_autre_justification:
 "Autre justification",

 support_papier:
 "Papier",

 support_numerique:
 "Numérique",

 support_autres:
 "Autres"
 };

 if (labels[name]) {
 return labels[name];
 }

 return label || name;
}


/* ============================================================
 * APDP — RENDU DES CHAMPS
 * ============================================================ */

function renderField(field) {

 const name =
 field.name ||
 field.key ||
 "";

 const rawLabel =
 field.label ||
 name;

 const label =
 typeof apdpPrettyFieldLabel === "function"
 ? apdpPrettyFieldLabel({
     ...field,
     key: name,
     label: rawLabel
   })
 : apdpPrettyLabel(
     name,
     rawLabel
   );

 /*
  * Certains formulaires utilisent un titre de rubrique
  * externe (ex. Annexe 1). Dans ce cas, le label interne
  * du champ ne doit pas être répété.
  */
 const displayLabel =
 field.hideLabel === true
 ? ""
 : label;

 const type =
 field.type ||
 "text";


 /* Champs déjà connus : on conserve le mécanisme
 de préremplissage existant s'il est disponible. */
 if (
 typeof getAPDPAutoValue === "function"
 ) {

 const autoValue =
 getAPDPAutoValue(field);

 if (
 autoValue !== undefined &&
 autoValue !== null &&
 autoValue !== ""
 ) {

 return `
 <input
 type="hidden"
 name="${escapeHtml(name)}"
 data-apdp-key="${escapeHtml(name)}"
 value="${escapeHtml(autoValue)}"
 data-apdp-auto="1"
 >
 `;
 }
 }


 if (type === "section") {

 const children =
 Array.isArray(field.children)
 ? field.children
 : [];

 const childrenHtml =
 children.length
 ? children.map(child => renderField(child)).join("")
 : "";

 return `
 <div class="apdp-composite-field">

 ${displayLabel
 ? `<div class="apdp-section-title">
 ${escapeHtml(displayLabel)}
 </div>`
 : ""}

 <div class="apdp-composite-children">
 ${childrenHtml}
 </div>

 </div>
 `;
 }


 if (type === "declaration") {

 const declarationFields =
 Array.isArray(field.fields)
 ? field.fields
 : [];

 const fieldsHtml =
 declarationFields
 .map(child => renderField(child))
 .join("");

 return `
 <div class="apdp-composite-field">

 ${displayLabel
 ? `<div class="apdp-section-title">
 ${escapeHtml(displayLabel)}
 </div>`
 : ""}

 <div class="apdp-declaration-fields">
 ${fieldsHtml}
 </div>

 </div>
 `;
 }


 /* ========================================================
 RADIO = CHOIX UNIQUE
 ======================================================== */

 if (type === "radio") {

 const choices =
 Array.isArray(field.choices)
 ? field.choices
 : [];

 return `
 <div
 class="apdp-field apdp-radio-field"
 data-apdp-field="${escapeHtml(name)}"
 >

 <div class="apdp-choice-label">
 ${escapeHtml(displayLabel)}
 </div>

 <div class="apdp-radio-group">

 ${
 choices.map(choice => {

 const value =
 typeof choice === "object"
 ? (
 choice.value ??
 choice.label ??
 ""
 )
 : choice;

 const choiceLabel =
 typeof choice === "object"
 ? (
 choice.label ??
 choice.value ??
 ""
 )
 : choice;

 return `
 <label class="apdp-choice-card">

 <input
 type="radio"
 name="${escapeHtml(name)}"
 value="${escapeHtml(value)}"
 data-apdp-key="${escapeHtml(name)}"
 >

 <span>
 ${escapeHtml(choiceLabel)}
 </span>

 </label>
 `;

 }).join("")
 }

 </div>

 </div>
 `;
 }


 /* ========================================================
 CHECKBOX = CHOIX MULTIPLES
 ======================================================== */

 if (type === "checkbox") {

 return `
 <div
 class="apdp-field apdp-checkbox-field"
 data-apdp-field="${escapeHtml(name)}"
 >

 <label class="apdp-choice-card">

 <input
 type="checkbox"
 name="${escapeHtml(name)}"
 value="oui"
 data-apdp-key="${escapeHtml(name)}"
 >

 <span>
 ${escapeHtml(displayLabel)}
 </span>

 </label>

 </div>
 `;
 }


 /* ========================================================
 CHECKBOX GROUP
 ======================================================== */

 if (type === "checkbox_group") {

 const choices =
 Array.isArray(field.choices)
 ? field.choices
 : [];

 return `
 <div
 class="apdp-field apdp-checkbox-group-field"
 data-apdp-field="${escapeHtml(name)}"
 >

 <div class="apdp-choice-label">
 ${escapeHtml(displayLabel)}
 </div>

 <div class="apdp-checkbox-group">

 ${
 choices.map(choice => {

 const value =
 typeof choice === "object"
 ? (
 choice.value ??
 choice.label ??
 ""
 )
 : choice;

 const choiceLabel =
 typeof choice === "object"
 ? (
 choice.label ??
 choice.value ??
 ""
 )
 : choice;

 return `
 <label class="apdp-choice-card">

 <input
 type="checkbox"
 name="${escapeHtml(name)}"
 value="${escapeHtml(value)}"
 data-apdp-key="${escapeHtml(name)}"
 >

 <span>
 ${escapeHtml(choiceLabel)}
 </span>

 </label>
 `;

 }).join("")
 }

 </div>

 </div>
 `;
 }


 /* ========================================================
 SELECT
 ======================================================== */

 if (type === "select") {

 return `
 <div class="apdp-field">

 <label for="field-${escapeHtml(name)}">
 ${escapeHtml(displayLabel)}
 </label>

 <select
 id="field-${escapeHtml(name)}"
 name="${escapeHtml(name)}"
 data-apdp-key="${escapeHtml(name)}"
 >

 <option value="">
 - Sélectionner -
 </option>

 ${renderChoices(field)}

 </select>

 </div>
 `;
 }


 /* ========================================================
 TABLEAU APDP
 ======================================================== */

 if (type === "table") {

 const columns = Array.isArray(field.columns)
 ? field.columns
 : [];

 const tableColumns = columns.length
 ? columns
 : [{ key: "value", label: label }];

 const rowCount = 2;

 const headerHtml = tableColumns.map(column => `
 <th scope="col">
 ${escapeHtml(column.label || column.key || "")}
 </th>
 `).join("");

 const rowsHtml = Array.from(
 { length: rowCount },
 (_, rowIndex) => `
 <tr>
 ${
 tableColumns.map(column => {
 const columnKey = column.key || "value";
 const inputName =
 `${name}[${rowIndex}][${columnKey}]`;

 return `
 <td>
 <input
 type="text"
 name="${escapeHtml(inputName)}"
 data-apdp-key="${escapeHtml(name)}"
 data-apdp-table="${escapeHtml(name)}"
 data-apdp-row="${rowIndex}"
 data-apdp-column="${escapeHtml(columnKey)}"
 >
 </td>
 `;
 }).join("")
 }
 </tr>
 `
 ).join("");

 return `
 <div class="apdp-field apdp-table-field">

 <label>
 ${escapeHtml(displayLabel)}
 </label>

 <div class="apdp-table-wrapper">
 <table class="apdp-input-table">
 <thead>
 <tr>
 ${headerHtml}
 </tr>
 </thead>

 <tbody>
 ${rowsHtml}
 </tbody>
 </table>
 </div>

 </div>
 `;
 }


 /* ========================================================
 TEXTAREA
 ======================================================== */

 if (type === "textarea") {

 return `
 <div class="apdp-field">

 <label for="field-${escapeHtml(name)}">
 ${escapeHtml(displayLabel)}
 </label>

 <textarea
 id="field-${escapeHtml(name)}"
 name="${escapeHtml(name)}"
 data-apdp-key="${escapeHtml(name)}"
 rows="4"
 ></textarea>

 </div>
 `;
 }


 /* ========================================================
 CHAMP SIMPLE
 ======================================================== */

 return `
 <div class="apdp-field">

 <label for="field-${escapeHtml(name)}">
 ${escapeHtml(displayLabel)}
 </label>

 <input
 id="field-${escapeHtml(name)}"
 type="${escapeHtml(type)}"
 name="${escapeHtml(name)}"
 data-apdp-key="${escapeHtml(name)}"
 >

 </div>
 `;
}


function saveCurrentPageValues() {
 const fields = pageContainer.querySelectorAll(
 'input, textarea, select'
 );

 fields.forEach(field => {
 if (field.type === 'checkbox') {
 field.dataset.savedChecked = field.checked ? '1' : '0';
 } else if (field.type === 'radio') {
 field.dataset.savedChecked = field.checked ? '1' : '0';
 } else {
 field.dataset.savedValue = field.value;
 }
 });
 }

 function restorePageValues() {
 const fields = pageContainer.querySelectorAll(
 'input, textarea, select'
 );

 fields.forEach(field => {
 if (field.type === 'checkbox' || field.type === 'radio') {
 field.checked = field.dataset.savedChecked === '1';
 } else if (field.dataset.savedValue !== undefined) {
 field.value = field.dataset.savedValue;
 }
 });
 }

 
function normalizeExclusiveAPDPChoices() {
 const groups = [
 {
 selectors: [
 'Secteur prive',
 'Secteur public',
 'Secteur institutions etrangeres',
 'Privé',
 'Public',
 'Institutions étrangères'
 ],
 name: 'secteur'
 }
 ];

 groups.forEach(group => {
 const radios = [];

 document.querySelectorAll('input[type="radio"], input[type="checkbox"]').forEach(input => {
 const label = document.querySelector(`label[for="${input.id}"]`);
 const parentText = input.closest('label')?.textContent || '';
 const text = (label?.textContent || parentText || '').trim();

 const normalized = text
 .normalize('NFD')
 .replace(/[\u0300-\u036f]/g, '')
 .toLowerCase()
 .replace(/\s+/g, ' ')
 .trim();

 if (group.selectors.some(value => {
 const v = value
 .normalize('NFD')
 .replace(/[\u0300-\u036f]/g, '')
 .toLowerCase()
 .replace(/\s+/g, ' ')
 .trim();

 return normalized === v || normalized.includes(v);
 })) {
 radios.push(input);
 }
 });

 if (radios.length < 2) return;

 // Tous les choix appartiennent au même groupe radio.
 radios.forEach(input => {
 input.type = 'radio';
 input.name = group.name;
 });

 // Un seul choix peut rester sélectionné.
 const checked = radios.filter(input => input.checked);

 if (checked.length > 1) {
 // On conserve le premier choix sélectionné.
 checked.slice(1).forEach(input => {
 input.checked = false;
 });
 }

 radios.forEach(input => {
 input.addEventListener('change', () => {
 radios.forEach(other => {
 if (other !== input) {
 other.checked = false;
 }
 });
 });
 });
 });
}


/* ============================================================
 * APDP — STYLE DES CHOIX
 * ============================================================ */

function injectAPDPChoiceStyles() {

 if (document.getElementById("apdp-choice-style-final")) {
 return;
 }

 const style =
 document.createElement("style");

 style.id =
 "apdp-choice-style-final";

 style.textContent = `

 
 /* ============================================================
  * APDP — MISE EN PAGE COMPACTE
  * Les blocs s'enchaînent sans espaces artificiels.
  * Aucun impact sur les données ou le mapping PDF.
  * ============================================================ */

 .apdp-page {
   display: block;
   width: 100%;
   margin: 0;
   padding: 0;
 }

 .apdp-page-title {
   margin: 0 0 12px 0;
   padding: 0;
 }

 .apdp-page-title h3 {
   margin: 0;
   padding: 0 0 8px 0;
 }

 .apdp-field {
   margin-top: 0;
   margin-bottom: 10px;
 }

 .apdp-field:last-child {
   margin-bottom: 4px;
 }

 .apdp-section-title {
   margin: 12px 0 8px 0 !important;
   padding: 0 !important;
 }

 .apdp-empty-page {
   display: none !important;
   height: 0 !important;
   min-height: 0 !important;
   margin: 0 !important;
   padding: 0 !important;
 }

 .apdp-page + .apdp-page {
   margin-top: 10px;
 }

 .apdp-radio-field {
   margin-bottom: 8px;
 }

 .apdp-checkbox-field {
   margin-top: 2px;
   margin-bottom: 2px;
 }

  .apdp-radio-group,
 .apdp-checkbox-group {
 display: flex;
 flex-wrap: wrap;
 gap: 10px;
 margin-top: 8px;
 }

 .apdp-choice-card {
 display: inline-flex;
 align-items: center;
 gap: 8px;
 padding: 9px 14px;
 border: 1px solid #d9dee8;
 border-radius: 10px;
 background: #ffffff;
 cursor: pointer;
 font-size: 14px;
 color: #263244;
 transition:
 border-color .15s ease,
 background .15s ease,
 box-shadow .15s ease;
 }

 .apdp-choice-card:hover {
 border-color: #2563eb;
 background: #f8fbff;
 }

 .apdp-choice-card input {
 width: 16px;
 height: 16px;
 margin: 0;
 flex: 0 0 auto;
 cursor: pointer;
 }

 .apdp-choice-card:has(input:checked) {
 border-color: #2563eb;
 background: #eff6ff;
 box-shadow: 0 1px 3px rgba(37, 99, 235, .12);
 }

 .apdp-choice-label {
 font-weight: 600;
 color: #263244;
 margin-bottom: 4px;
 }

 .apdp-checkbox-field {
 display: inline-block;
 width: auto;
 margin: 4px 6px 4px 0;
 vertical-align: top;
 }

 .apdp-radio-field {
 margin-bottom: 14px;
 }

 .apdp-checkbox-field > label {
 margin: 0;
 }

 `;

 document.head.appendChild(style);
}

injectAPDPChoiceStyles();



/* ============================================================
 * APDP — FORMULAIRE CONTINU
 * ============================================================ */

function injectAPDPContinuousFormStyles() {

 if (document.getElementById("apdp-continuous-form-style")) {
   return;
 }

 const style = document.createElement("style");

 style.id = "apdp-continuous-form-style";

 style.textContent = `

 .apdp-business-section {
   display: block !important;
   width: 100%;
   margin: 0 !important;
   padding: 0 !important;
   min-height: 0 !important;
   height: auto !important;
   box-sizing: border-box;
 }

 .apdp-business-section + .apdp-business-section {
   margin-top: 12px !important;
 }

 .apdp-business-section .apdp-page-title {
   margin: 0 0 8px 0 !important;
   padding: 0 !important;
 }

 .apdp-business-section .apdp-page-title h3 {
   margin: 0 0 8px 0 !important;
   padding: 0 0 5px 0 !important;
 }

 .apdp-business-fields {
   margin: 0 !important;
   padding: 0 !important;
 }

 .apdp-business-fields .apdp-field {
   margin-top: 0 !important;
 }

 .apdp-business-fields
 .apdp-field[style*="display: none"] {
   display: none !important;
   height: 0 !important;
   min-height: 0 !important;
   margin: 0 !important;
   padding: 0 !important;
 }

 .apdp-empty-page {
   display: none !important;
 }

 `;

 document.head.appendChild(style);
}

injectAPDPContinuousFormStyles();

function renderPage(index) {

 currentPage = 0;

 /*
  * FORMULAIRE CONTINU
  *
  * Toutes les rubriques métier sont affichées à la suite.
  * "pages" reste conservé comme structure logique interne.
  * Aucun mapping PDF n'est modifié.
  */

 const renderedGroups = pages.map((page, groupIndex) => {

   const pageTitle =
     page.title ||
     page.label ||
     `Section ${groupIndex + 1}`;

   const fields =
     Array.isArray(page.fields)
       ? page.fields
       : [];

   if (!fields.length) {
     return "";
   }

   return `
     <section
       class="apdp-business-section"
       data-page="${escapeHtml(page.page)}"
       data-section-index="${groupIndex}"
     >

       <div class="apdp-page-title">
         <h3>${escapeHtml(pageTitle)}</h3>
       </div>

       <div class="apdp-business-fields">
         ${fields.map(renderField).join("")}
       </div>

     </section>
   `;
 }).join("");

 pageContainer.innerHTML = renderedGroups;

 restorePageValues();

 /*
  * Les champs masqués/automatiques ne doivent
  * réserver aucun espace.
  */
 pageContainer
   .querySelectorAll(".apdp-field")
   .forEach(wrapper => {

     if (
       wrapper.style.display === "none" ||
       wrapper.hidden ||
       wrapper.classList.contains("apdp-field-auto")
     ) {

       wrapper.style.display = "none";
       wrapper.style.margin = "0";
       wrapper.style.padding = "0";
       wrapper.style.height = "0";
       wrapper.style.minHeight = "0";
       wrapper.style.maxHeight = "0";
       wrapper.style.overflow = "hidden";
     }

   });

 /*
  * Toutes les rubriques sont dans le même flux.
  */
 pageContainer
   .querySelectorAll(".apdp-business-section")
   .forEach(section => {

     section.style.display = "block";
     section.style.width = "100%";
     section.style.margin = "0";
     section.style.padding = "0";
     section.style.minHeight = "0";
     section.style.height = "auto";
     section.style.boxSizing = "border-box";

   });

 /*
  * Réduction des espacements entre les rubriques.
  */
 pageContainer
   .querySelectorAll(".apdp-business-section + .apdp-business-section")
   .forEach(section => {

     section.style.marginTop = "12px";

   });

 apdpRestoreState(pageContainer);

 if (typeof apdpBindConditionalRules === "function") {
   apdpBindConditionalRules();
 }

 if (typeof apdpApplyConditionalRules === "function") {
   apdpApplyConditionalRules();
 }

 normalizeExclusiveAPDPChoices();

 /*
  * Plus de pagination entre les rubriques.
  */
 pageNumber.textContent = "Formulaire complet";
 progressBar.style.width = "100%";

 generateButton.style.display = "inline-block";

 window.scrollTo({
   top: 0,
   behavior: "smooth"
 });
}



 /* Les champs obligatoires masqués ne peuvent pas être remplis : on ne les valide pas. */
 generateButton.addEventListener('click', () => {
 form.querySelectorAll('[required]').forEach(el => {
 if (!el.offsetParent) { el.required = false; }
 });
 }, true);

 form.addEventListener('invalid', (e) => {
 console.warn("[ComplianceForge] Champ invalide :", e.target.name || e.target.id);
 }, true);

 form.addEventListener('submit', async (event) => {
 event.preventDefault();
 console.info("[ComplianceForge] Formulaire soumis");

 try {
 apdpRememberCurrentPage(pageContainer);
 saveCurrentPageValues();
 } catch (erreur) {
 console.error("[ComplianceForge] Sauvegarde de la page :", erreur);
 }

 await generateAPDPDocument(documentId, form);
 });

 renderPage(0);

 } catch (error) {
 console.error('Erreur chargement formulaire APDP:', error);

 container.innerHTML = `
 <div class="apdp-error">
 <h2>Erreur</h2>

 <p>
 Impossible de charger le formulaire APDP.
 </p>

 <pre>${error.message}</pre>

 <button
 type="button"
 onclick="openAPDPForm('${documentId}')">
 Réessayer
 </button>
 </div>
 `;
 }
}

async function generateAPDPDocument(documentId, form) {
 console.info("[ComplianceForge] Génération demandée :", documentId);
 let message = document.getElementById("apdp-generation-message");
 if (!message) {
 message = document.createElement("div");
 message.id = "apdp-generation-message";
 const ancre = document.getElementById("apdp-generate") || form;
 ancre.insertAdjacentElement("afterend", message);
 }

 const data = {};

/*
 * Toutes les sections ont été remplies dans l'interface.
 * On fusionne leur état avant génération.
 */
Object.entries(window.apdpUIState || {})
 .forEach(([key, value]) => {

 if (
 value &&
 Array.isArray(value.values)
 ) {
 data[key] = [
 ...value.values
 ];
 } else if (value) {
 data[key] =
 value.value ?? "";
 }
 });

 const elements = form.querySelectorAll("input, textarea, select");

 elements.forEach(function(input) {

 if (input.name) {
 if (
 input.type === "checkbox" ||
 input.type === "radio"
 ) {
 window.apdpUIState[input.name] =
 window.apdpUIState[input.name] || {
 type: input.type,
 values: []
 };

 if (input.checked) {
 if (
 !window.apdpUIState[input.name]
 .values
 .includes(input.value)
 ) {
 window.apdpUIState[input.name]
 .values
 .push(input.value);
 }
 }
 } else {
 window.apdpUIState[input.name] = {
 type: input.type,
 value: input.value
 };
 }
 }
 if (!input.name) {
 return;
 }

 /*
 * Les groupes checkbox restent des tableaux.
 */
 if (input.type === "checkbox") {
 if (!Array.isArray(data[input.name])) {
 data[input.name] = [];
 }

 if (input.checked) {
 data[input.name].push(input.value);
 }

 return;
 }

 /*
 * Les radios sont des choix uniques.
 *
 * Pour les groupes issus du schema builder, pdf_mapping
 * permet de convertir :
 *
 * sous_traitance = "oui"
 *
 * en :
 *
 * sous_traitance_oui = ["oui"]
 *
 * sans modifier le mapping officiel du PDF.
 */
 if (input.type === "radio") {
 if (!input.checked) {
 return;
 }

 const field = input.closest(".apdp-field");
 const fieldKey = input.dataset.apdpKey || input.name;

 if (
 field &&
 window.apdpSchemaFields &&
 window.apdpSchemaFields[fieldKey] &&
 window.apdpSchemaFields[fieldKey].pdf_mapping
 ) {
 const mapping =
 window.apdpSchemaFields[fieldKey].pdf_mapping;

 Object.entries(mapping).forEach(function([value, pdfKey]) {
 data[pdfKey] = value === input.value;
 });

 return;
 }

 data[fieldKey] = input.value;
 return;
 }

 data[input.name] = input.value;
 });

 updateAPDPCommonData(documentId, data);

 message.className = "form-message";
 message.textContent = "Génération du document en cours...";

 try {
 const response = await fetch(
 "https://api.complianceforge.test/apdp/generer",
 {
 method: "POST",
 headers: {
 "Content-Type": "application/json"
 },
 body: JSON.stringify({
 document_id: documentId,

 output_name:
 "ComplianceForge_" +
 documentId +
 "_" +
 (
 window.complianceForgeContext?.traitementId ||
 "traitement"
 ) +
 ".pdf",

 dossier: getAPDPDossier(),

 data: {
 ...data,

 organisation_id:
 window.complianceForgeContext?.organisationId ||
 null,

 traitement_id:
 window.complianceForgeContext?.traitementId ||
 null
 }
 })
 }
 );

 const result = await response.json();

 if (!response.ok) {
 throw new Error(
 result.detail ||
 "Erreur lors de la génération du document."
 );
 }

 message.className = "form-message success";

 message.innerHTML =
 "<strong> Document généré avec succès</strong>" +
 "<p>" +
 result.nom_fichier +
 "</p>" +
 "<div style=\"margin-top:12px;\">" +
 "<button type=\"button\" " +
 "class=\"btn-primary\" " +
 "onclick=\"openGeneratedAPDPDocument('" +
 result.nom_fichier +
 "')\">" +
 "Ouvrir le PDF" +
 "</button>" +
 "</div>";

 } catch (error) {

 console.error(
 "Erreur génération APDP :",
 error
 );

 message.className = "form-message error";

 message.innerHTML =
 "<strong>Erreur</strong>" +
 "<p>" +
 error.message +
 "</p>";
 }
}


function openGeneratedAPDPDocument(filename) {
 const url =
 "https://api.complianceforge.test/generated/apdp/" +
 encodeURIComponent(filename);

 window.open(
 url,
 "_blank"
 );
}

function closeAPDPForm() {
 const editor = document.getElementById("apdp-form-editor");

 if (editor) {
 editor.innerHTML = "";
 }
}


(function injectComplianceForgeScoringCSS() {

 if (document.getElementById("complianceforge-scoring-css")) {
 return;
 }

 const style = document.createElement("style");

 style.id = "complianceforge-scoring-css";

 style.textContent = `

 .dashboard-scoring-section {
 margin-top: 24px;
 padding: 24px;
 background: #ffffff;
 border: 1px solid #e5e7eb;
 border-radius: 14px;
 }

 .dashboard-scoring-header {
 display: flex;
 justify-content: space-between;
 align-items: center;
 gap: 20px;
 margin-bottom: 20px;
 }

 .dashboard-scoring-header h2 {
 margin: 0 0 6px;
 }

 .dashboard-scoring-header p {
 margin: 0;
 color: #64748b;
 }

 .dashboard-scoring-grid {
 display: grid;
 grid-template-columns:
 repeat(4, minmax(0, 1fr));
 gap: 16px;
 }

 .dashboard-score-card {
 padding: 18px;
 background: #f8fafc;
 border: 1px solid #e5e7eb;
 border-radius: 12px;
 }

 .dashboard-score-card span {
 display: block;
 font-size: 13px;
 color: #64748b;
 margin-bottom: 8px;
 }

 .dashboard-score-card strong {
 display: block;
 font-size: 25px;
 margin-bottom: 7px;
 }

 .dashboard-score-card small {
 color: #64748b;
 }

 .scoring-result-card {
 margin-top: 18px;
 padding: 22px;
 background: #ffffff;
 border: 1px solid #e5e7eb;
 border-radius: 14px;
 }

 .scoring-result-header h3 {
 margin: 0 0 5px;
 }

 .scoring-result-header p {
 margin: 0;
 color: #64748b;
 }

 .scoring-result-grid {
 display: grid;
 grid-template-columns:
 repeat(3, minmax(0, 1fr));
 gap: 15px;
 margin-top: 18px;
 }

 .scoring-result-item {
 padding: 16px;
 background: #f8fafc;
 border-radius: 10px;
 }

 .scoring-result-item span {
 display: block;
 color: #64748b;
 font-size: 13px;
 margin-bottom: 8px;
 }

 .scoring-result-item strong {
 font-size: 22px;
 }

 .scoring-loading {
 padding: 30px;
 text-align: center;
 color: #64748b;
 }

 @media (max-width: 900px) {

 .dashboard-scoring-grid,
 .scoring-result-grid {
 grid-template-columns:
 repeat(2, minmax(0, 1fr));
 }
 }

 @media (max-width: 600px) {

 .dashboard-scoring-header {
 flex-direction: column;
 align-items: flex-start;
 }

 .dashboard-scoring-grid,
 .scoring-result-grid {
 grid-template-columns: 1fr;
 }
 }

 `;

 document.head.appendChild(style);

})();


document.addEventListener("keydown", (event) => {
 const card = event.target.closest(".dashboard-card-clickable");

 if (!card) {
 return;
 }

 if (event.key === "Enter" || event.key === " ") {
 event.preventDefault();
 card.click();
 }
});


/* Réinitialisation du sélecteur APDP après navigation */
const apdpContextObserver =
 new MutationObserver(() => {

 const selector =
 document.getElementById(
 "apdp-organisation-select"
 );

 if (
 selector &&
 !selector.dataset.initialized
 ) {

 selector.dataset.initialized = "1";

 initAPDPContextSelector();
 }
 });

document.addEventListener(
 "DOMContentLoaded",
 () => {

 const main =
 document.querySelector(
 ".main-content"
 );

 if (main) {

 apdpContextObserver.observe(
 main,
 {
 childList: true,
 subtree: true
 }
 );
 }
 }
);



/* ============================================================
   COMPLIANCEFORGE — DASHBOARD / CONTRÔLES UTILISATEUR
   ============================================================ */

(function initComplianceForgeDashboardUI() {

    function init() {

        /* -----------------------------------------------------
           Déterminer l'état initial du dashboard
           ----------------------------------------------------- */

        function setDashboardState(page) {

            document.body.classList.toggle(
                "dashboard-active",
                page === "dashboard"
            );
        }

        setDashboardState("dashboard");

        /* -----------------------------------------------------
           Intercepter navigate() sans modifier son fonctionnement
           ----------------------------------------------------- */

        if (
            typeof window.navigate === "function" &&
            !window.navigate.__complianceForgeWrapped
        ) {

            const originalNavigate =
                window.navigate;

            function wrappedNavigate() {

                const page =
                    arguments.length
                        ? arguments[0]
                        : null;

                setDashboardState(page);

                return originalNavigate.apply(
                    this,
                    arguments
                );
            }

            wrappedNavigate.__complianceForgeWrapped = true;
            wrappedNavigate.__original = originalNavigate;

            window.navigate = wrappedNavigate;
        }

        /* -----------------------------------------------------
           Menu utilisateur
           ----------------------------------------------------- */

        const userButton =
            document.getElementById(
                "user-menu-button"
            );

        const userMenu =
            document.getElementById(
                "user-menu"
            );

        if (!userButton || !userMenu) {
            return;
        }

        function closeUserMenu() {

            userMenu.classList.remove(
                "user-menu-open"
            );

            userButton.setAttribute(
                "aria-expanded",
                "false"
            );

            userMenu.setAttribute(
                "aria-hidden",
                "true"
            );
        }

        function toggleUserMenu() {

            const open =
                userMenu.classList.toggle(
                    "user-menu-open"
                );

            userButton.setAttribute(
                "aria-expanded",
                String(open)
            );

            userMenu.setAttribute(
                "aria-hidden",
                String(!open)
            );
        }

        userButton.addEventListener(
            "click",
            event => {

                event.stopPropagation();

                toggleUserMenu();

            }
        );

        document.addEventListener(
            "click",
            event => {

                if (
                    !userMenu.contains(event.target) &&
                    !userButton.contains(event.target)
                ) {
                    closeUserMenu();
                }

            }
        );

        document.addEventListener(
            "keydown",
            event => {

                if (event.key === "Escape") {
                    closeUserMenu();
                }

            }
        );
    }

    if (document.readyState === "loading") {

        document.addEventListener(
            "DOMContentLoaded",
            init,
            { once: true }
        );

    } else {

        init();

    }

})();




/* ============================================================
   COMPLIANCEFORGE — ESPACE UTILISATEUR
   Profil / Paramètres / Sécurité
   ============================================================ */

(function () {

    const USER_PROFILE_KEY = "complianceforge_user_profile";
    const USER_SETTINGS_KEY = "complianceforge_user_settings";

    const defaultProfile = {
        nom: "Utilisateur",
        prenoms: "",
        email: "",
        fonction: "",
        role: "Administrateur",
        organisation: ""
    };

    const defaultSettings = {
        notifications: true,
        affichage: "standard",
        langue: "fr"
    };

    function getUserProfile() {
        try {
            return {
                ...defaultProfile,
                ...JSON.parse(
                    localStorage.getItem(USER_PROFILE_KEY) || "{}"
                )
            };
        } catch {
            return { ...defaultProfile };
        }
    }

    function saveUserProfile(profile) {
        localStorage.setItem(
            USER_PROFILE_KEY,
            JSON.stringify(profile)
        );
    }

    function getUserSettings() {
        try {
            return {
                ...defaultSettings,
                ...JSON.parse(
                    localStorage.getItem(USER_SETTINGS_KEY) || "{}"
                )
            };
        } catch {
            return { ...defaultSettings };
        }
    }

    function saveUserSettings(settings) {
        localStorage.setItem(
            USER_SETTINGS_KEY,
            JSON.stringify(settings)
        );
    }

    function fermerMenuUtilisateur() {
        const menu = document.getElementById("user-menu");

        if (menu) {
            menu.setAttribute("aria-hidden", "true");
        }
    }

    function getMainContent() {
        return document.querySelector(".main-content");
    }

    function afficherBoutonRetour() {
        return `
            <button
                type="button"
                class="user-page-back"
                onclick="navigate('dashboard')"
            >
                ← Retour au tableau de bord
            </button>
        `;
    }

    function afficherPageUtilisateur(titre, sousTitre, contenu) {

        const main = getMainContent();

        if (!main) {
            return;
        }

        fermerMenuUtilisateur();

        main.innerHTML = `
            <div class="user-page">

                <div class="user-page-top">
                    <div>
                        <div class="user-page-kicker">
                            COMPLIANCEFORGE
                        </div>

                        <h1>${titre}</h1>

                        <p>${sousTitre}</p>
                    </div>

                    ${afficherBoutonRetour()}
                </div>

                ${contenu}

            </div>
        `;

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }

    /* ========================================================
       👤 MON PROFIL
       ======================================================== */

    window.afficherMonProfil = function afficherMonProfil() {

        const profile = getUserProfile();

        afficherPageUtilisateur(
            "👤 Mon profil",
            "Gérez les informations associées à votre compte utilisateur.",
            `

            <div class="user-profile-layout">

                <section class="user-panel user-profile-card">

                    <div class="user-panel-header">
                        <div class="user-big-avatar">Y</div>

                        <div>
                            <h2>${profile.nom || "Utilisateur"}</h2>
                            <p>${profile.role}</p>
                        </div>
                    </div>

                    <div class="user-form-grid">

                        <label>
                            <span>Nom</span>
                            <input
                                id="profile-nom"
                                type="text"
                                value="${escapeUserValue(profile.nom)}"
                            >
                        </label>

                        <label>
                            <span>Prénoms</span>
                            <input
                                id="profile-prenoms"
                                type="text"
                                value="${escapeUserValue(profile.prenoms)}"
                            >
                        </label>

                        <label>
                            <span>Adresse e-mail</span>
                            <input
                                id="profile-email"
                                type="email"
                                value="${escapeUserValue(profile.email)}"
                            >
                        </label>

                        <label>
                            <span>Fonction</span>
                            <input
                                id="profile-fonction"
                                type="text"
                                value="${escapeUserValue(profile.fonction)}"
                                placeholder="Ex. Responsable conformité"
                            >
                        </label>

                        <label>
                            <span>Rôle</span>
                            <input
                                type="text"
                                value="${escapeUserValue(profile.role)}"
                                disabled
                            >
                        </label>

                        <label>
                            <span>Organisation</span>
                            <input
                                id="profile-organisation"
                                type="text"
                                value="${escapeUserValue(profile.organisation)}"
                                placeholder="Organisation associée"
                            >
                        </label>

                    </div>

                    <div class="user-form-actions">

                        <button
                            type="button"
                            class="user-btn-secondary"
                            onclick="navigate('dashboard')"
                        >
                            Annuler
                        </button>

                        <button
                            type="button"
                            class="user-btn-primary"
                            onclick="enregistrerProfilUtilisateur()"
                        >
                            ✓ Enregistrer
                        </button>

                    </div>

                    <div
                        id="profile-save-message"
                        class="user-save-message"
                        hidden
                    >
                        ✓ Profil enregistré avec succès.
                    </div>

                </section>

                <aside class="user-panel user-info-panel">

                    <h3>Informations du compte</h3>

                    <div class="user-info-row">
                        <span>Statut</span>
                        <strong class="user-status-active">
                            ● Actif
                        </strong>
                    </div>

                    <div class="user-info-row">
                        <span>Rôle</span>
                        <strong>${profile.role}</strong>
                    </div>

                    <div class="user-info-row">
                        <span>Type de compte</span>
                        <strong>Administrateur</strong>
                    </div>

                </aside>

            </div>
            `
        );
    }

    window.enregistrerProfilUtilisateur = function () {

        const profile = getUserProfile();

        profile.nom =
            document.getElementById("profile-nom")?.value.trim()
            || "Utilisateur";

        profile.prenoms =
            document.getElementById("profile-prenoms")?.value.trim()
            || "";

        profile.email =
            document.getElementById("profile-email")?.value.trim()
            || "";

        profile.fonction =
            document.getElementById("profile-fonction")?.value.trim()
            || "";

        profile.organisation =
            document.getElementById("profile-organisation")?.value.trim()
            || "";

        saveUserProfile(profile);

        const msg =
            document.getElementById("profile-save-message");

        if (msg) {
            msg.hidden = false;

            setTimeout(() => {
                msg.hidden = true;
            }, 3000);
        }
    };

    /* ========================================================
       ⚙️ PARAMÈTRES
       ======================================================== */

    window.afficherParametres = function afficherParametres() {

        const settings = getUserSettings();

        afficherPageUtilisateur(
            "⚙️ Paramètres",
            "Configurez les préférences de votre espace ComplianceForge.",
            `

            <div class="user-settings-grid">

                <section class="user-panel">

                    <div class="user-panel-title">
                        <span>🔔</span>

                        <div>
                            <h2>Notifications</h2>
                            <p>
                                Contrôlez les notifications de la plateforme.
                            </p>
                        </div>
                    </div>

                    <label class="user-toggle-row">

                        <div>
                            <strong>Notifications activées</strong>
                            <small>
                                Recevoir les alertes importantes
                                de conformité et de pilotage.
                            </small>
                        </div>

                        <input
                            id="setting-notifications"
                            type="checkbox"
                            ${settings.notifications ? "checked" : ""}
                        >

                    </label>

                </section>

                <section class="user-panel">

                    <div class="user-panel-title">
                        <span>🎨</span>

                        <div>
                            <h2>Affichage</h2>
                            <p>
                                Choisissez le niveau d'affichage
                                de votre espace.
                            </p>
                        </div>
                    </div>

                    <label class="user-setting-field">
                        <span>Mode d'affichage</span>

                        <select id="setting-affichage">
                            <option value="standard"
                                ${settings.affichage === "standard" ? "selected" : ""}>
                                Standard
                            </option>

                            <option value="compact"
                                ${settings.affichage === "compact" ? "selected" : ""}>
                                Compact
                            </option>
                        </select>
                    </label>

                </section>

                <section class="user-panel">

                    <div class="user-panel-title">
                        <span>🌐</span>

                        <div>
                            <h2>Langue</h2>
                            <p>
                                Langue utilisée dans l'interface.
                            </p>
                        </div>
                    </div>

                    <label class="user-setting-field">
                        <span>Langue</span>

                        <select id="setting-langue">
                            <option value="fr"
                                ${
                                    (
                                        settings.langue === "fr" ||
                                        settings.langue === "Français" ||
                                        !settings.langue
                                    )
                                    ? "selected"
                                    : ""
                                }>
                                🇫🇷 Français
                            </option>

                            <option value="en"
                                ${
                                    (
                                        settings.langue === "en" ||
                                        settings.langue === "English"
                                    )
                                    ? "selected"
                                    : ""
                                }>
                                🇬🇧 English
                            </option>
                        </select>
                    </label>

                </section>

                <section class="user-panel">

                    <div class="user-panel-title">
                        <span>🏢</span>

                        <div>
                            <h2>Organisation</h2>
                            <p>
                                Organisation utilisée par défaut
                                dans votre espace de travail.
                            </p>
                        </div>
                    </div>

                    <label class="user-setting-field">
                        <span>Organisation par défaut</span>

                        <input
                            id="setting-organisation"
                            type="text"
                            placeholder="Organisation associée"
                        >
                    </label>

                </section>

            </div>

            <div class="user-settings-actions">

                <button
                    type="button"
                    class="user-btn-primary"
                    onclick="enregistrerParametresUtilisateur()"
                >
                    ✓ Enregistrer les paramètres
                </button>

            </div>

            <div
                id="settings-save-message"
                class="user-save-message"
                hidden
            >
                ✓ Paramètres enregistrés.
            </div>
            `
        );
    }

    window.enregistrerParametresUtilisateur = function () {

        const settings = getUserSettings();

        settings.notifications =
            Boolean(
                document.getElementById(
                    "setting-notifications"
                )?.checked
            );

        settings.affichage =
            document.getElementById(
                "setting-affichage"
            )?.value || "standard";

        settings.langue =
            document.getElementById(
                "setting-langue"
            )?.value || "fr";

        const organisation =
            document.getElementById(
                "setting-organisation"
            )?.value.trim() || "";

        saveUserSettings(settings);

        const profile = getUserProfile();

        profile.organisation = organisation;

        saveUserProfile(profile);

        const msg =
            document.getElementById("settings-save-message");

        if (msg) {
            msg.hidden = false;

            setTimeout(() => {
                msg.hidden = true;
            }, 3000);
        }
    };

    /* ========================================================
       🔐 SÉCURITÉ
       ======================================================== */

    window.afficherSecurite = function afficherSecurite() {

        afficherPageUtilisateur(
            "🔐 Sécurité",
            "Consultez et gérez les principaux paramètres de sécurité du compte.",
            `

            <div class="security-grid">

                <section class="user-panel">

                    <div class="security-status-card">

                        <div class="security-icon">
                            🔐
                        </div>

                        <div>
                            <strong>Session actuelle</strong>

                            <span class="security-active">
                                ● Session active
                            </span>

                            <small>
                                Votre session ComplianceForge
                                est actuellement active.
                            </small>
                        </div>

                    </div>

                </section>

                <section class="user-panel">

                    <div class="user-panel-title">
                        <span>🔑</span>

                        <div>
                            <h2>Mot de passe</h2>
                            <p>
                                La modification du mot de passe
                                nécessite un mécanisme d'authentification
                                côté serveur.
                            </p>
                        </div>
                    </div>

                    <button
                        type="button"
                        class="user-btn-secondary"
                        id="cf-change-password-button"
                    >
                        Modifier le mot de passe
                    </button>

                </section>

                <section class="user-panel">

                    <div class="user-panel-title">
                        <span>🛡️</span>

                        <div>
                            <h2>Authentification renforcée</h2>
                            <p>
                                État de l'authentification multifacteur.
                            </p>
                        </div>
                    </div>

                    <div class="security-state">
                        <span class="security-state-badge">
                            Non configurée
                        </span>

                        <small>
                            Cette fonctionnalité pourra être
                            activée lors de l'intégration
                            d'un système d'authentification.
                        </small>
                    </div>

                </section>

                <section class="user-panel">

                    <div class="user-panel-title">
                        <span>💻</span>

                        <div>
                            <h2>Sessions</h2>
                            <p>
                                Gestion des sessions ouvertes.
                            </p>
                        </div>
                    </div>

                    <div class="security-session cf-current-session">

                        <div class="cf-session-main">

                            <strong>Session actuelle</strong>

                            <small id="cf-session-device">
                                Navigateur courant
                            </small>

                            <small id="cf-session-started">
                                Session active depuis : —
                            </small>

                            <small id="cf-session-last-activity">
                                Dernière activité : —
                            </small>

                        </div>

                        <div class="cf-session-actions">

                            <span class="security-active">
                                Active
                            </span>

                            <button
                                type="button"
                                class="user-btn-secondary"
                                id="cf-dedicated-logout"
                            >
                                Se déconnecter
                            </button>

                        </div>

                    </div>

                </section>

                <section class="user-panel security-full">

                    <div class="user-panel-title">
                        <span>📋</span>

                        <div>
                            <h2>Journal de sécurité</h2>
                            <p>
                                Historique des événements de sécurité
                                liés à votre compte.
                            </p>
                        </div>
                    </div>

                    <div
                        id="cf-security-log-container"
                        class="security-log-list"
                    >
                        <div class="security-empty">
                            Chargement du journal de sécurité...
                        </div>
                    </div>

                </section>

            </div>
            `
        );
    }

    /* ========================================================
       UTILITAIRE
       ======================================================== */

    function escapeUserValue(value) {

        return String(value || "")
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    window.escapeUserValue = escapeUserValue;

    /* ========================================================
       BIND DES 3 BOUTONS DU MENU
       ======================================================== */

    function initialiserMenuUtilisateur() {

        const menu = document.getElementById("user-menu");

        if (!menu) {
            return;
        }

        const items =
            menu.querySelectorAll(".user-menu-item");

        if (!items.length) {
            return;
        }

        /* Mon profil */
        if (items[0]) {
            items[0].onclick = function (event) {
                event.preventDefault();
                event.stopPropagation();

                afficherMonProfil();
            };
        }

        /* Paramètres */
        if (items[1]) {
            items[1].onclick = function (event) {
                event.preventDefault();
                event.stopPropagation();

                afficherParametres();
            };
        }

        /* Sécurité */
        if (items[2]) {
            items[2].onclick = function (event) {
                event.preventDefault();
                event.stopPropagation();

                afficherSecurite();
            };
        }
    }

    if (document.readyState === "loading") {

        document.addEventListener(
            "DOMContentLoaded",
            initialiserMenuUtilisateur
        );

    } else {

        initialiserMenuUtilisateur();
    }

    /*
       Le menu peut être recréé ou modifié par d'autres
       éléments de l'application : on réinitialise légèrement
       après le chargement.
    */

    setTimeout(
        initialiserMenuUtilisateur,
        500
    );

})();




/* ============================================================
   COMPLIANCEFORGE — PARAMÈTRES RÉELS
   Langue / Mode / Affichage / Déconnexion
   ============================================================ */

(function () {

    const SETTINGS_KEY =
        "complianceforge_user_settings";

    const SESSION_KEY =
        "complianceforge_session";

    const LANGUAGES = {
        fr: {
            name: "Français",
            flag: "🇫🇷"
        },
        en: {
            name: "English",
            flag: "🇬🇧"
        }
    };

    const translations = {

        fr: {
            profile: "Mon profil",
            settings: "Paramètres",
            security: "Sécurité",
            logout: "Se déconnecter",
            language: "Langue",
            appearance: "Apparence",
            display: "Affichage",
            light: "Clair",
            dark: "Sombre",
            standard: "Standard",
            compact: "Compact",
            save: "✓ Enregistrer les paramètres",
            saved: "✓ Paramètres enregistrés.",
            back: "← Retour au tableau de bord"
        },

        en: {
            profile: "My profile",
            settings: "Settings",
            security: "Security",
            logout: "Log out",
            language: "Language",
            appearance: "Appearance",
            display: "Display",
            light: "Light",
            dark: "Dark",
            standard: "Standard",
            compact: "Compact",
            save: "✓ Save settings",
            saved: "✓ Settings saved.",
            back: "← Back to dashboard"
        },

        es: {
            profile: "Mi perfil",
            settings: "Configuración",
            security: "Seguridad",
            logout: "Cerrar sesión",
            language: "Idioma",
            appearance: "Apariencia",
            display: "Visualización",
            light: "Claro",
            dark: "Oscuro",
            standard: "Estándar",
            compact: "Compacto",
            save: "✓ Guardar configuración",
            saved: "✓ Configuración guardada.",
            back: "← Volver al panel"
        },

        pt: {
            profile: "Meu perfil",
            settings: "Configurações",
            security: "Segurança",
            logout: "Terminar sessão",
            language: "Idioma",
            appearance: "Aparência",
            display: "Exibição",
            light: "Claro",
            dark: "Escuro",
            standard: "Padrão",
            compact: "Compacto",
            save: "✓ Guardar configurações",
            saved: "✓ Configurações guardadas.",
            back: "← Voltar ao painel"
        }
    };

    function getSettings() {

        try {

            return {
                language: "fr",
                theme: "light",
                display: "standard",
                ...JSON.parse(
                    localStorage.getItem(SETTINGS_KEY) || "{}"
                )
            };

        } catch {

            return {
                language: "fr",
                theme: "light",
                display: "standard"
            };
        }
    }

    function saveSettings(settings) {

        localStorage.setItem(
            SETTINGS_KEY,
            JSON.stringify(settings)
        );
    }

    function applyTheme(theme) {

        document.documentElement
            .setAttribute(
                "data-theme",
                theme
            );

        document.body.classList.toggle(
            "theme-dark",
            theme === "dark"
        );
    }

    function applyDisplay(display) {

        document.body.classList.toggle(
            "display-compact",
            display === "compact"
        );

        document.body.classList.toggle(
            "display-standard",
            display !== "compact"
        );
    }

    function applyLanguage(language) {

        document.documentElement
            .setAttribute(
                "lang",
                language
            );

        const t =
            translations[language]
            || translations.fr;

        /*
         * Menu utilisateur
         */

        const menuItems =
            document.querySelectorAll(
                "#user-menu .user-menu-item"
            );

        if (menuItems[0]) {
            menuItems[0].textContent =
                "👤 " + t.profile;
        }

        if (menuItems[1]) {
            menuItems[1].textContent =
                "⚙️ " + t.settings;
        }

        if (menuItems[2]) {
            menuItems[2].textContent =
                "🔐 " + t.security;
        }

        /*
         * Bouton déconnexion
         */

        const logoutButton =
            document.getElementById(
                "user-logout-button"
            );

        if (logoutButton) {
            logoutButton.textContent =
                "🚪 " + t.logout;
        }
    }

    function applyAllSettings() {

        const settings = getSettings();

        applyTheme(settings.theme);
        applyDisplay(settings.display);
        applyLanguage(settings.language);

        return settings;
    }

    window.complianceForgeApplySettings =
        applyAllSettings;

    window.complianceForgeSaveSettings =
        function () {

            const settings = {
                ...getSettings(),

                language:
                    document.getElementById(
                        "setting-langue"
                    )?.value
                    || "fr",

                theme:
                    document.getElementById(
                        "setting-theme"
                    )?.value
                    || "light",

                display:
                    document.getElementById(
                        "setting-affichage"
                    )?.value
                    || "standard"
            };

            saveSettings(settings);

            applyTheme(settings.theme);
            applyDisplay(settings.display);
            applyLanguage(settings.language);

            const msg =
                document.getElementById(
                    "settings-save-message"
                );

            if (msg) {

                const t =
                    translations[
                        settings.language
                    ] || translations.fr;

                msg.textContent =
                    t.saved;

                msg.hidden = false;

                setTimeout(
                    () => {
                        msg.hidden = true;
                    },
                    2500
                );
            }
        };

    /*
     * Déconnexion locale.
     *
     * Tant que l'authentification serveur n'est pas
     * branchée, cette fonction ferme la session locale.
     */

    window.complianceForgeLogout =
        function () {

            localStorage.removeItem(
                SESSION_KEY
            );

            sessionStorage.clear();

            fermerMenuUtilisateur();

            /*
             * Retour à l'écran de connexion.
             */

            const main =
                document.querySelector(
                    ".main-content"
                );

            if (!main) {
                return;
            }

            main.innerHTML = `
                <div class="logout-page">

                    <div class="logout-card">

                        <div class="logout-icon">
                            ✓
                        </div>

                        <h1>Session terminée</h1>

                        <p>
                            Vous avez été déconnecté
                            de ComplianceForge.
                        </p>

                        <button
                            type="button"
                            class="user-btn-primary"
                            onclick="complianceForgeShowLogin()"
                        >
                            Se reconnecter
                        </button>

                    </div>

                </div>
            `;

        };

    

    function fermerMenuUtilisateur() {

        const menu =
            document.getElementById(
                "user-menu"
            );

        const button =
            document.getElementById(
                "user-menu-button"
            );

        if (menu) {

            menu.classList.remove(
                "user-menu-open"
            );

            menu.setAttribute(
                "aria-hidden",
                "true"
            );
        }

        if (button) {

            button.setAttribute(
                "aria-expanded",
                "false"
            );
        }
    }

    /*
     * Ajout du bouton de déconnexion
     */

    function ajouterDeconnexion() {
        return;

        const menu =
            document.getElementById(
                "user-menu"
            );

        if (!menu) {
            return;
        }

        if (
            document.getElementById(
                "user-logout-button"
            )
        ) {
            return;
        }

        const separator =
            document.createElement("div");

        separator.className =
            "user-menu-separator";

        const button =
            document.createElement("button");

        button.type = "button";

        button.id =
            "user-logout-button";

        button.className =
            "user-menu-item user-menu-logout";

        button.textContent =
            "🚪 Se déconnecter";

        
        menu.appendChild(separator);
        menu.appendChild(button);
    }

    /*
     * Mise à jour de la page Paramètres existante.
     */

    function enrichirPageParametres() {

        const settings =
            getSettings();

        const language =
            document.getElementById(
                "setting-langue"
            );

        if (language) {

            language.innerHTML = `
                <option value="fr">🇫🇷 Français</option>
                <option value="en">🇬🇧 English</option>
            `;

            language.value =
                settings.language;
        }

        const display =
            document.getElementById(
                "setting-affichage"
            );

        if (display) {

            display.innerHTML = `
                <option value="standard">
                    ${translations[settings.language]?.standard || "Standard"}
                </option>

                <option value="compact">
                    ${translations[settings.language]?.compact || "Compact"}
                </option>
            `;

            display.value =
                settings.display;
        }

        /*
         * Nouveau sélecteur de thème
         */

        const oldTheme =
            document.getElementById(
                "setting-theme"
            );

        if (!oldTheme) {

            const field =
                document.createElement(
                    "label"
                );

            field.className =
                "user-setting-field";

            field.innerHTML = `
                <span>🎨 ${
                    translations[
                        settings.language
                    ]?.appearance || "Apparence"
                }</span>

                <select id="setting-theme">

                    <option value="light">
                        ☀️ ${
                            translations[
                                settings.language
                            ]?.light || "Clair"
                        }
                    </option>

                    <option value="dark">
                        🌙 ${
                            translations[
                                settings.language
                            ]?.dark || "Sombre"
                        }
                    </option>

                </select>
            `;

            const panels =
                document.querySelectorAll(
                    ".user-settings-grid .user-panel"
                );

            if (panels[1]) {
                panels[1].appendChild(field);
            }

        }

        const theme =
            document.getElementById(
                "setting-theme"
            );

        if (theme) {
            theme.value =
                settings.theme;
        }
    }

    /*
     * Surveille l'ouverture de la page Paramètres.
     */

    /*
     * IMPORTANT :
     * Ne pas observer continuellement le DOM.
     *
     * L'ancienne version provoquait une boucle :
     * modification DOM -> observer -> modification DOM -> ...
     *
     * Les paramètres sont maintenant enrichis uniquement
     * lorsque la page Paramètres est effectivement ouverte.
     */
    function enrichirParametresUneFois() {

        if (!document.querySelector(".user-settings-grid")) {
            return;
        }

        if (
            document.getElementById("setting-theme") &&
            document.getElementById("setting-langue") &&
            document.getElementById("setting-affichage")
        ) {
            return;
        }

        enrichirPageParametres();
    }

    window.enrichirParametresUneFois =
        enrichirParametresUneFois;

    /*
     * Appliquer les préférences au chargement.
     */

    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            () => {

                applyAllSettings();
                ajouterDeconnexion();

            }
        );

    } else {

        applyAllSettings();
        ajouterDeconnexion();
    }

})();




/* ============================================================
   COMPLIANCEFORGE — MENU UTILISATEUR — CORRECTION FINALE
   Un seul gestionnaire prioritaire pour Profil / Paramètres /
   Sécurité.
   ============================================================ */

(function () {

    function bindUserMenuFinal() {

        const menu =
            document.getElementById("user-menu");

        if (!menu) {
            return;
        }

        const items =
            menu.querySelectorAll(".user-menu-item");

        if (!items.length) {
            return;
        }

        /*
         * Ajouter des identifiants stables.
         */

        if (items[0]) {
            items[0].id = "user-menu-profile";
        }

        if (items[1]) {
            items[1].id = "user-menu-settings";
        }

        if (items[2]) {
            items[2].id = "user-menu-security";
        }

        /*
         * Déconnexion éventuelle déjà présente.
         */

        const logout =
            document.getElementById(
                "user-logout-button"
            );

        if (logout) {
            logout.id = "user-logout-button";
        }
    }

    /*
     * Gestionnaire en CAPTURE :
     * il passe avant les anciens gestionnaires.
     */

    if (!window.__complianceForgeUserMenuFinal) {

        window.__complianceForgeUserMenuFinal = true;

        document.addEventListener(
            "click",
            function (event) {

                const button =
                    event.target.closest(
                        "#user-menu .user-menu-item"
                    );

                if (!button) {
                    return;
                }

                /*
                 * Ne pas intercepter la déconnexion.
                 */
                if (
                    button.id ===
                    "user-logout-button"
                ) {
                    return;
                }

                event.preventDefault();
                event.stopPropagation();
                event.stopImmediatePropagation();

                /*
                 * Profil
                 */
                if (
                    button.id ===
                    "user-menu-profile"
                ) {

                    if (
                        typeof window.afficherMonProfil ===
                        "function"
                    ) {
                        window.afficherMonProfil();
                    }

                    return;
                }

                /*
                 * Paramètres
                 */
                if (
                    button.id ===
                    "user-menu-settings" ||
                    button.id ===
                    "user-menu-settings-final"
                ) {

                    if (
                        typeof window.afficherParametres ===
                        "function"
                    ) {
                        window.afficherParametres();
                    }

                    /*
                     * Les champs Langue / Mode /
                     * Affichage sont ajoutés après
                     * le rendu de la page.
                     */
                    setTimeout(
                        function () {

                            if (
                                typeof window.enrichirPageParametres ===
                                "function"
                            ) {
                                window.enrichirPageParametres();
                            }

                        },
                        50
                    );

                    return;
                }

                /*
                 * Sécurité
                 */
                if (
                    button.id ===
                    "user-menu-security"
                ) {

                    if (
                        typeof window.afficherSecurite ===
                        "function"
                    ) {
                        window.afficherSecurite();
                    }

                    return;
                }

            },
            true
        );
    }

    /*
     * Le menu existe déjà dans index.html,
     * mais on attend quand même le DOM.
     */

    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            bindUserMenuFinal,
            { once: true }
        );

    } else {

        bindUserMenuFinal();

    }

    /*
     * Sécurité supplémentaire si le DOM du menu
     * est recréé.
     */

    setTimeout(
        bindUserMenuFinal,
        300
    );

})();




/* ============================================================
   COMPLIANCEFORGE — PARAMÈTRES — FORÇAGE DU CLIC
   ============================================================ */

(function () {

    function forceParametresButton() {

        const menu = document.getElementById("user-menu");

        if (!menu) {
            return;
        }

        const items = menu.querySelectorAll(".user-menu-item");

        if (items.length < 2) {
            return;
        }

        const settingsButton = items[1];

        /*
         * Cloner le bouton supprime TOUS les anciens
         * addEventListener attachés dessus.
         */

        const cleanButton = settingsButton.cloneNode(true);

        cleanButton.id = "user-menu-settings";
        cleanButton.removeAttribute("onclick");

        settingsButton.parentNode.replaceChild(
            cleanButton,
            settingsButton
        );

        /*
         * Un seul clic propre.
         */

        cleanButton.addEventListener("click", function (event) {

            event.preventDefault();
            event.stopPropagation();

            console.log(
                "[ComplianceForge] Ouverture Paramètres"
            );

            if (
                typeof window.afficherParametres ===
                "function"
            ) {
                window.afficherParametres();
            } else {
                console.error(
                    "[ComplianceForge] afficherParametres introuvable"
                );
            }

        });

        console.log(
            "[ComplianceForge] Bouton Paramètres réparé"
        );
    }

    /*
     * Exposer pour pouvoir le relancer.
     */

    window.forceParametresButton =
        forceParametresButton;

    /*
     * Attendre que le menu existe.
     */

    function init() {

        forceParametresButton();

        setTimeout(
            forceParametresButton,
            500
        );

        setTimeout(
            forceParametresButton,
            1200
        );
    }

    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            init,
            { once: true }
        );

    } else {

        init();
    }

})();


/* =========================================================
   COMPLIANCEFORGE — I18N GLOBAL UNIQUE
   ========================================================= */

/* =========================================================
   COMPLIANCEFORGE — I18N GLOBAL UNIQUE
   ---------------------------------------------------------
   TRADUIT :
   - toute l'interface ComplianceForge
   - contenu dynamique
   - Dashboard
   - menus
   - Paramètres
   - formulaires visibles
   - boutons
   - messages
   - labels
   - choix affichés

   NE TRADUIT PAS :
   - valeurs saisies par l'utilisateur
   - input.value
   - textarea.value
   - données métier
   - objets de génération PDF
   - mappings APDP
   - backend
   ========================================================= */

(function ComplianceForgeGlobalI18N() {

    "use strict";

    const LANGUAGES = ["fr", "en"];

    const CATALOG_PATH =
        "i18n_interface";

    const SETTINGS_KEY =
        "complianceforge_user_settings";

    const state = {
        language: "fr",
        catalogs: {},
        loaded: false,
        applying: false
    };

    /*
     * ---------------------------------------------------------
     * LANGUE
     * ---------------------------------------------------------
     */

    function getSavedLanguage() {

        try {

            const raw =
                localStorage.getItem(
                    SETTINGS_KEY
                );

            if (!raw) {
                return "fr";
            }

            const settings =
                JSON.parse(raw);

            const language =
                settings.language ||
                settings.lang ||
                "fr";

            return LANGUAGES.includes(language)
                ? language
                : "fr";

        } catch (_) {

            return "fr";
        }
    }

    function saveLanguage(language) {

        try {

            let settings = {};

            const raw =
                localStorage.getItem(
                    SETTINGS_KEY
                );

            if (raw) {

                try {
                    settings =
                        JSON.parse(raw) || {};
                } catch (_) {
                    settings = {};
                }
            }

            settings.language = language;
            settings.lang = language;

            localStorage.setItem(
                SETTINGS_KEY,
                JSON.stringify(settings)
            );

        } catch (_) {}
    }

    /*
     * ---------------------------------------------------------
     * CATALOGUES
     * ---------------------------------------------------------
     */

    async function loadCatalogs() {

        if (state.loaded) {
            return true;
        }

        for (
            const language
            of LANGUAGES
        ) {

            try {

                const response =
                    await fetch(
                        `${CATALOG_PATH}/${language}.json`,
                        {
                            cache: "no-store"
                        }
                    );

                if (!response.ok) {
                    throw new Error(
                        `HTTP ${response.status}`
                    );
                }

                state.catalogs[language] =
                    await response.json();

            } catch (error) {

                console.error(
                    `[ComplianceForge i18n] Catalogue ${language} inaccessible`,
                    error
                );

                state.catalogs[language] = {};
            }
        }

        state.loaded = true;

        return true;
    }

    /*
     * ---------------------------------------------------------
     * NORMALISATION
     * ---------------------------------------------------------
     */

    function normalize(value) {

        return String(
            value ?? ""
        )
        .replace(/\u00A0/g, " ")
        .replace(/\s+/g, " ")
        .trim();
    }

    /*
     * Conserve les espaces autour du texte.
     */
    function translateText(
        original,
        language
    ) {

        const clean =
            normalize(original);

        if (!clean) {
            return null;
        }

        const catalog =
            state.catalogs[language] || {};

        if (
            Object.prototype.hasOwnProperty.call(
                catalog,
                clean
            )
        ) {
            return catalog[clean];
        }

        /*
         * Gestion des emojis au début :
         *
         * 🏢 Organisation
         *
         * devient
         *
         * 🏢 Organization
         */
        const match =
            clean.match(
                /^((?:[\u{1F000}-\u{1FAFF}\u2600-\u27BF])\s*)(.*)$/u
            );

        if (match) {

            const translated =
                catalog[
                    normalize(match[2])
                ];

            if (
                translated !== undefined
            ) {

                return (
                    match[1] +
                    translated
                );
            }
        }

        return null;
    }

    /*
     * ---------------------------------------------------------
     * ÉLÉMENTS À NE JAMAIS TRADUIRE
     * ---------------------------------------------------------
     */

    function ignored(element) {

        if (
            !element ||
            element.nodeType !== 1
        ) {
            return true;
        }

        /*
         * IMPORTANT :
         * input et textarea ne sont jamais modifiés.
         * Cela protège les données saisies.
         */
        if (
            element.matches(
                "input, textarea"
            )
        ) {
            return true;
        }

        if (
            element.closest(
                "script, style, noscript, template, pre, code"
            )
        ) {
            return true;
        }

        /*
         * Protection explicite possible.
         */
        if (
            element.closest(
                "[data-cf-i18n-ignore]"
            )
        ) {
            return true;
        }

        return false;
    }

    /*
     * ---------------------------------------------------------
     * TEXTES VISIBLES
     * ---------------------------------------------------------
     */

    function translateTextNode(
        node,
        language
    ) {

        if (
            !node ||
            node.nodeType !== Node.TEXT_NODE
        ) {
            return;
        }

        const parent =
            node.parentElement;

        if (
            !parent ||
            ignored(parent)
        ) {
            return;
        }

        /*
         * Ne mémorise le texte source qu'une seule fois.
         * Ainsi EN → ES → PT → FR fonctionne.
         */
        if (
            node.__cfOriginalText === undefined
        ) {

            node.__cfOriginalText =
                node.nodeValue;
        }

        const source =
            node.__cfOriginalText;

        const leading =
            String(source)
                .match(/^\s*/)?.[0] || "";

        const trailing =
            String(source)
                .match(/\s*$/)?.[0] || "";

        const clean =
            normalize(source);

        if (!clean) {
            return;
        }

        let translated =
            translateText(
                clean,
                language
            );

        /*
         * FR = source original.
         */
        if (
            language === "fr"
        ) {
            translated =
                clean;
        }

        if (
            translated === null ||
            translated === undefined
        ) {
            /*
             * Si aucune traduction n'existe,
             * on conserve le texte affiché.
             */
            return;
        }

        node.nodeValue =
            leading +
            translated +
            trailing;
    }

    /*
     * ---------------------------------------------------------
     * ATTRIBUTS D'INTERFACE
     * ---------------------------------------------------------
     */

    function translateAttribute(
        element,
        attribute,
        language
    ) {

        if (
            ignored(element)
        ) {
            return;
        }

        const value =
            element.getAttribute(
                attribute
            );

        if (!value) {
            return;
        }

        /*
         * Clé dataset sûre :
         * title       -> cfOriginalTitle
         * aria-label  -> cfOriginalAriaLabel
         * placeholder -> cfOriginalPlaceholder
         *
         * Les noms dataset ne doivent pas contenir
         * de tiret.
         */
        const normalizedAttribute =
            attribute.replace(
                /-([a-z])/g,
                (_, letter) => letter.toUpperCase()
            );

        const key =
            `cfOriginal${normalizedAttribute
                .charAt(0)
                .toUpperCase()}${normalizedAttribute.slice(1)}`;

        if (
            element.dataset[key] === undefined
        ) {

            element.dataset[key] =
                value;
        }

        const source =
            element.dataset[key];

        let translated =
            translateText(
                source,
                language
            );

        if (
            language === "fr"
        ) {
            translated =
                normalize(source);
        }

        if (
            translated !== null &&
            translated !== undefined
        ) {

            element.setAttribute(
                attribute,
                translated
            );
        }
    }

    /*
     * ---------------------------------------------------------
     * TRADUCTION D'UN CONTENEUR
     * ---------------------------------------------------------
     */

    function translateContainer(
        container,
        language
    ) {

        if (
            !container ||
            !state.loaded ||
            state.applying
        ) {
            return;
        }

        state.applying = true;

        try {

            /*
             * Attributs d'interface.
             */
            translateAttribute(
                container,
                "title",
                language
            );

            translateAttribute(
                container,
                "aria-label",
                language
            );

            translateAttribute(
                container,
                "placeholder",
                language
            );

            /*
             * Textes visibles.
             */
            const walker =
                document.createTreeWalker(
                    container,
                    NodeFilter.SHOW_TEXT,
                    {
                        acceptNode(node) {

                            const parent =
                                node.parentElement;

                            if (
                                !parent ||
                                ignored(parent)
                            ) {
                                return NodeFilter.FILTER_REJECT;
                            }

                            return NodeFilter.FILTER_ACCEPT;
                        }
                    }
                );

            const nodes = [];

            let node;

            while (
                (node = walker.nextNode())
            ) {
                nodes.push(node);
            }

            nodes.forEach(
                textNode =>
                    translateTextNode(
                        textNode,
                        language
                    )
            );

            /*
             * Attributs sur tous les éléments.
             */
            const elements =
                container.querySelectorAll(
                    "*"
                );

            elements.forEach(
                element => {

                    if (
                        ignored(element)
                    ) {
                        return;
                    }

                    translateAttribute(
                        element,
                        "title",
                        language
                    );

                    translateAttribute(
                        element,
                        "aria-label",
                        language
                    );

                    translateAttribute(
                        element,
                        "placeholder",
                        language
                    );
                }
            );

        } finally {

            state.applying = false;
        }
    }

    /*
     * ---------------------------------------------------------
     * APPLICATION GLOBALE
     * ---------------------------------------------------------
     */

    async function applyLanguage(
        language
    ) {

        if (
            !LANGUAGES.includes(language)
        ) {
            language = "fr";
        }

        await loadCatalogs();

        state.language =
            language;

        saveLanguage(
            language
        );

        document.documentElement.lang =
            language;

        translateContainer(
            document.body,
            language
        );

        /*
         * Les fonctions dynamiques peuvent avoir
         * ajouté du contenu juste après le rendu.
         */
        requestAnimationFrame(
            () => {

                translateContainer(
                    document.body,
                    language
                );
            }
        );

        console.info(
            `[ComplianceForge i18n] ${language}`
        );
    }

    /*
     * ---------------------------------------------------------
     * API PUBLIQUE
     * ---------------------------------------------------------
     */

    window.complianceForgeSetLanguage =
        applyLanguage;

    window.complianceForgeTranslatePage =
        function() {

            return applyLanguage(
                state.language
            );
        };

    window.complianceForgeGetLanguage =
        function() {

            return state.language;
        };

    /*
     * ---------------------------------------------------------
     * NOUVEAU CONTENU DYNAMIQUE
     *
     * IMPORTANT :
     * on observe uniquement childList.
     * On n'observe PAS les modifications de texte.
     * Donc aucune boucle infinie.
     * ---------------------------------------------------------
     */

    function installObserver() {

        if (!document.body) {
            return;
        }

        if (
            window.__complianceForgeI18NObserver
        ) {
            return;
        }

        const observer =
            new MutationObserver(
                mutations => {

                    if (
                        state.applying
                    ) {
                        return;
                    }

                    const added =
                        mutations.some(
                            mutation =>
                                mutation.addedNodes &&
                                mutation.addedNodes.length
                        );

                    if (!added) {
                        return;
                    }

                    /*
                     * Petit délai pour laisser
                     * innerHTML terminer son rendu.
                     */
                    setTimeout(
                        () => {

                            translateContainer(
                                document.body,
                                state.language
                            );

                        },
                        0
                    );
                }
            );

        observer.observe(
            document.body,
            {
                childList: true,
                subtree: true
            }
        );

        window.__complianceForgeI18NObserver =
            observer;
    }

    /*
     * ---------------------------------------------------------
     * CHANGEMENT DE LANGUE
     * ---------------------------------------------------------
     *
     * Le sélecteur des Paramètres est détecté
     * par ses valeurs FR/EN/ES/PT.
     */

    document.addEventListener(
        "change",
        async event => {

            const target =
                event.target;

            if (
                !target ||
                target.tagName !== "SELECT"
            ) {
                return;
            }

            const values =
                Array.from(
                    target.options || []
                ).map(
                    option =>
                        String(
                            option.value
                        ).toLowerCase()
                );

            const isLanguage =
                values.includes("fr") &&
                values.includes("en");

            if (!isLanguage) {
                return;
            }

            const language =
                String(
                    target.value
                ).toLowerCase();

            if (
                !LANGUAGES.includes(language)
            ) {
                return;
            }

            await applyLanguage(
                language
            );
        },
        true
    );

    /*
     * ---------------------------------------------------------
     * INITIALISATION
     * ---------------------------------------------------------
     */

    async function initialize() {

        await loadCatalogs();

        state.language =
            getSavedLanguage();

        installObserver();

        await applyLanguage(
            state.language
        );

        console.info(
            "[ComplianceForge i18n] Global actif."
        );
    }

    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            initialize,
            {
                once: true
            }
        );

    } else {

        initialize();
    }

})();



/* CF — SYNC SETTING LANGUE FR EN */

/* CF — SYNC SETTING LANGUE FR EN */
(function () {

    "use strict";

    document.addEventListener(
        "change",
        function (event) {

            const target =
                event.target;

            if (
                !target ||
                target.id !== "setting-langue"
            ) {
                return;
            }

            const language =
                target.value === "en"
                    ? "en"
                    : "fr";

            /*
             * Synchronisation avec le moteur i18n global.
             */
            if (
                typeof window.complianceForgeSetLanguage ===
                "function"
            ) {

                window.complianceForgeSetLanguage(
                    language
                );
            }

            /*
             * Synchronisation avec les paramètres.
             */
            try {

                const key =
                    "complianceforge_user_settings";

                let settings = {};

                const raw =
                    localStorage.getItem(key);

                if (raw) {
                    settings =
                        JSON.parse(raw) || {};
                }

                settings.langue =
                    language;

                settings.language =
                    language;

                localStorage.setItem(
                    key,
                    JSON.stringify(settings)
                );

            } catch (_) {}

        },
        true
    );

})();


/* ============================================================
   COMPLIANCEFORGE — PARAMETRES ET MENU UTILISATEUR FINAL
   ============================================================ */

/* ============================================================
   COMPLIANCEFORGE — PARAMETRES ET MENU UTILISATEUR FINAL
   ------------------------------------------------------------
   - Français / English uniquement
   - Clair / Sombre
   - Standard / Compact
   - Notifications
   - Préférences persistantes
   - Menu utilisateur traduit
   - Aucun impact APDP / PDF
   ============================================================ */

(function ComplianceForgeFinalUserSettings() {

    "use strict";

    const SETTINGS_KEY =
        "complianceforge_user_settings";

    function getSettings() {

        try {

            const raw =
                localStorage.getItem(
                    SETTINGS_KEY
                );

            const saved =
                raw
                    ? JSON.parse(raw)
                    : {};

            return {
                language:
                    saved.language ||
                    saved.lang ||
                    saved.langue ||
                    "fr",

                langue:
                    saved.language ||
                    saved.lang ||
                    saved.langue ||
                    "fr",

                theme:
                    saved.theme ||
                    "light",

                display:
                    saved.display ||
                    saved.affichage ||
                    "standard",

                notifications:
                    saved.notifications !== false
            };

        } catch (_) {

            return {
                language: "fr",
                langue: "fr",
                theme: "light",
                display: "standard",
                notifications: true
            };
        }
    }

    function saveSettings(settings) {

        const normalized = {
            ...settings,

            language:
                settings.language === "en"
                    ? "en"
                    : "fr",

            langue:
                settings.language === "en"
                    ? "en"
                    : "fr",

            theme:
                settings.theme === "dark"
                    ? "dark"
                    : "light",

            display:
                settings.display === "compact"
                    ? "compact"
                    : "standard",

            notifications:
                settings.notifications !== false
        };

        localStorage.setItem(
            SETTINGS_KEY,
            JSON.stringify(normalized)
        );

        return normalized;
    }

    function applyTheme(theme) {

        const dark =
            theme === "dark";

        document.documentElement.classList.toggle(
            "dark-mode",
            dark
        );

        document.body.classList.toggle(
            "dark-mode",
            dark
        );

        document.documentElement.dataset.theme =
            dark
                ? "dark"
                : "light";

        document.body.dataset.theme =
            dark
                ? "dark"
                : "light";

        localStorage.setItem(
            "complianceforge_theme",
            dark
                ? "dark"
                : "light"
        );
    }

    function applyDisplay(display) {

        const compact =
            display === "compact";

        document.body.classList.toggle(
            "compact-mode",
            compact
        );

        document.documentElement.classList.toggle(
            "compact-mode",
            compact
        );

        document.body.dataset.display =
            compact
                ? "compact"
                : "standard";
    }

    function getLanguage() {

        const settings =
            getSettings();

        return settings.language === "en"
            ? "en"
            : "fr";
    }

    const UI = {

        fr: {

            title:
                "Paramètres",

            subtitle:
                "Configurez les préférences de votre espace ComplianceForge.",

            back:
                "← Retour au tableau de bord",

            languageTitle:
                "Langue",

            languageText:
                "Choisissez la langue de l'interface.",

            languageLabel:
                "Langue de l'interface",

            french:
                "🇫🇷 Français",

            english:
                "🇬🇧 English",

            appearanceTitle:
                "Apparence",

            appearanceText:
                "Choisissez l'apparence de l'application.",

            themeLabel:
                "Mode d'apparence",

            light:
                "☀️ Clair",

            dark:
                "🌙 Sombre",

            displayTitle:
                "Affichage",

            displayText:
                "Adaptez la densité des informations affichées.",

            displayLabel:
                "Mode d'affichage",

            standard:
                "Standard",

            compact:
                "Compact",

            notificationTitle:
                "Notifications",

            notificationText:
                "Gestion des notifications de la plateforme.",

            notificationLabel:
                "Notifications activées",

            notificationHelp:
                "Recevoir les alertes importantes de conformité et de pilotage.",

            save:
                "Enregistrer les préférences",

            reset:
                "Réinitialiser",

            logout:
                "Se déconnecter",

            saved:
                "✓ Préférences enregistrées.",

            resetDone:
                "✓ Préférences réinitialisées."
        },

        en: {

            title:
                "⚙️ Settings",

            subtitle:
                "Configure your ComplianceForge workspace preferences.",

            back:
                "← Back to dashboard",

            languageTitle:
                "🌐 Language",

            languageText:
                "Choose the interface language.",

            languageLabel:
                "Interface language",

            french:
                "🇫🇷 French",

            english:
                "🇬🇧 English",

            appearanceTitle:
                "🎨 Appearance",

            appearanceText:
                "Choose the application appearance.",

            themeLabel:
                "Appearance mode",

            light:
                "☀️ Light",

            dark:
                "🌙 Dark",

            displayTitle:
                "📐 Display",

            displayText:
                "Adjust the density of displayed information.",

            displayLabel:
                "Display mode",

            standard:
                "Standard",

            compact:
                "Compact",

            notificationTitle:
                "🔔 Notifications",

            notificationText:
                "Manage platform notifications.",

            notificationLabel:
                "Notifications enabled",

            notificationHelp:
                "Receive important compliance and management alerts.",

            save:
                "💾 Save preferences",

            reset:
                "↩️ Reset",

            logout:
                "🚪 Log out",

            saved:
                "✓ Preferences saved.",

            resetDone:
                "✓ Preferences reset."
        }
    };

    window.afficherParametres =
        function () {

            const settings =
                getSettings();

            const lang =
                getLanguage();

            const t =
                UI[lang];

            const container =
                document.querySelector(
                    ".main-content"
                ) ||
                document.querySelector(
                    "#main-content"
                ) ||
                document.querySelector(
                    "main"
                );

            if (!container) {
                console.error(
                    "[ComplianceForge] Conteneur principal introuvable."
                );
                return;
            }

            container.innerHTML = `

                <div class="cf-settings-page">

                    <div class="cf-settings-header">

                        <div>

                            <div class="cf-brand-small">
                                <span class="cf-brand-mark">CF</span>
                                <span>COMPLIANCEFORGE</span>
                            </div>

                            <h1>
                                ${t.title}
                            </h1>

                            <p>
                                ${t.subtitle}
                            </p>

                        </div>

                        <button
                            type="button"
                            class="cf-settings-back"
                            id="cf-settings-back"
                        >
                            ${t.back}
                        </button>

                    </div>


                    <div class="cf-settings-grid">


                        <!-- LANGUE -->

                        <section class="cf-settings-card">

                            <div class="cf-settings-card-head">

                                <div class="cf-settings-icon">
                                    🌐
                                </div>

                                <div>

                                    <h2>
                                        ${t.languageTitle}
                                    </h2>

                                    <p>
                                        ${t.languageText}
                                    </p>

                                </div>

                            </div>

                            <label
                                class="cf-setting-field"
                            >

                                <span>
                                    ${t.languageLabel}
                                </span>

                                <select
                                    id="setting-langue-final"
                                >

                                    <option
                                        value="fr"
                                        ${lang === "fr" ? "selected" : ""}
                                    >
                                        ${t.french}
                                    </option>

                                    <option
                                        value="en"
                                        ${lang === "en" ? "selected" : ""}
                                    >
                                        ${t.english}
                                    </option>

                                </select>

                            </label>

                        </section>


                        <!-- APPARENCE -->

                        <section class="cf-settings-card">

                            <div class="cf-settings-card-head">

                                <div class="cf-settings-icon">
                                    🎨
                                </div>

                                <div>

                                    <h2>
                                        ${t.appearanceTitle}
                                    </h2>

                                    <p>
                                        ${t.appearanceText}
                                    </p>

                                </div>

                            </div>

                            <label
                                class="cf-setting-field"
                            >

                                <span>
                                    ${t.themeLabel}
                                </span>

                                <select
                                    id="setting-theme-final"
                                >

                                    <option
                                        value="light"
                                        ${settings.theme !== "dark" ? "selected" : ""}
                                    >
                                        ${t.light}
                                    </option>

                                    <option
                                        value="dark"
                                        ${settings.theme === "dark" ? "selected" : ""}
                                    >
                                        ${t.dark}
                                    </option>

                                </select>

                            </label>

                        </section>


                        <!-- AFFICHAGE -->

                        <section class="cf-settings-card">

                            <div class="cf-settings-card-head">

                                <div class="cf-settings-icon">
                                    📐
                                </div>

                                <div>

                                    <h2>
                                        ${t.displayTitle}
                                    </h2>

                                    <p>
                                        ${t.displayText}
                                    </p>

                                </div>

                            </div>

                            <label
                                class="cf-setting-field"
                            >

                                <span>
                                    ${t.displayLabel}
                                </span>

                                <select
                                    id="setting-display-final"
                                >

                                    <option
                                        value="standard"
                                        ${settings.display !== "compact" ? "selected" : ""}
                                    >
                                        ${t.standard}
                                    </option>

                                    <option
                                        value="compact"
                                        ${settings.display === "compact" ? "selected" : ""}
                                    >
                                        ${t.compact}
                                    </option>

                                </select>

                            </label>

                        </section>


                        <!-- NOTIFICATIONS -->

                        <section class="cf-settings-card">

                            <div class="cf-settings-card-head">

                                <div class="cf-settings-icon">
                                    🔔
                                </div>

                                <div>

                                    <h2>
                                        ${t.notificationTitle}
                                    </h2>

                                    <p>
                                        ${t.notificationText}
                                    </p>

                                </div>

                            </div>

                            <label
                                class="cf-notification-row"
                            >

                                <div>

                                    <strong>
                                        ${t.notificationLabel}
                                    </strong>

                                    <p>
                                        ${t.notificationHelp}
                                    </p>

                                </div>

                                <input
                                    type="checkbox"
                                    id="setting-notifications-final"
                                    ${settings.notifications ? "checked" : ""}
                                >

                            </label>

                        </section>

                    </div>


                    <div class="cf-settings-actions">

                        <button
                            type="button"
                            class="cf-btn-primary"
                            id="cf-settings-save"
                        >
                            ${t.save}
                        </button>

                        <button
                            type="button"
                            class="cf-btn-secondary"
                            id="cf-settings-reset"
                        >
                            ${t.reset}
                        </button>

                        <button
                            type="button"
                            class="cf-btn-danger"
                            id="cf-settings-logout"
                        >
                            ${t.logout}
                        </button>

                    </div>

                    <div
                        id="cf-settings-message"
                        class="cf-settings-message"
                        aria-live="polite"
                    ></div>

                </div>
            `;

            applyTheme(
                settings.theme
            );

            applyDisplay(
                settings.display
            );


            document
                .getElementById(
                    "cf-settings-back"
                )
                ?.addEventListener(
                    "click",
                    () => {

                        if (
                            typeof window.navigate ===
                            "function"
                        ) {

                            window.navigate(
                                "dashboard"
                            );

                        } else {

                            location.hash =
                                "#dashboard";
                        }
                    }
                );


            document
                .getElementById(
                    "setting-langue-final"
                )
                ?.addEventListener(
                    "change",
                    async event => {

                        const language =
                            event.target.value === "en"
                                ? "en"
                                : "fr";

                        const current =
                            getSettings();

                        saveSettings({
                            ...current,
                            language,
                            langue: language
                        });

                        if (
                            typeof window.complianceForgeSetLanguage ===
                            "function"
                        ) {

                            await window
                                .complianceForgeSetLanguage(
                                    language
                                );
                        }

                        /*
                         * Reconstruit la page Paramètres
                         * dans la nouvelle langue.
                         */
                        window.afficherParametres();
                    }
                );


            document
                .getElementById(
                    "setting-theme-final"
                )
                ?.addEventListener(
                    "change",
                    event => {

                        const theme =
                            event.target.value === "dark"
                                ? "dark"
                                : "light";

                        const current =
                            getSettings();

                        saveSettings({
                            ...current,
                            theme
                        });

                        applyTheme(
                            theme
                        );
                    }
                );


            document
                .getElementById(
                    "setting-display-final"
                )
                ?.addEventListener(
                    "change",
                    event => {

                        const display =
                            event.target.value === "compact"
                                ? "compact"
                                : "standard";

                        const current =
                            getSettings();

                        saveSettings({
                            ...current,
                            display
                        });

                        applyDisplay(
                            display
                        );
                    }
                );


            document
                .getElementById(
                    "setting-notifications-final"
                )
                ?.addEventListener(
                    "change",
                    event => {

                        const current =
                            getSettings();

                        saveSettings({
                            ...current,
                            notifications:
                                event.target.checked
                        });
                    }
                );


            document
                .getElementById(
                    "cf-settings-save"
                )
                ?.addEventListener(
                    "click",
                    () => {

                        const current =
                            getSettings();

                        const language =
                            document
                                .getElementById(
                                    "setting-langue-final"
                                )
                                ?.value === "en"
                                ? "en"
                                : "fr";

                        const theme =
                            document
                                .getElementById(
                                    "setting-theme-final"
                                )
                                ?.value === "dark"
                                ? "dark"
                                : "light";

                        const display =
                            document
                                .getElementById(
                                    "setting-display-final"
                                )
                                ?.value === "compact"
                                ? "compact"
                                : "standard";

                        const notifications =
                            document
                                .getElementById(
                                    "setting-notifications-final"
                                )
                                ?.checked !== false;

                        saveSettings({
                            ...current,
                            language,
                            langue: language,
                            theme,
                            display,
                            notifications
                        });

                        applyTheme(
                            theme
                        );

                        applyDisplay(
                            display
                        );

                        const message =
                            document.getElementById(
                                "cf-settings-message"
                            );

                        if (message) {
                            message.textContent =
                                UI[
                                    language
                                ].saved;
                        }
                    }
                );


            document
                .getElementById(
                    "cf-settings-reset"
                )
                ?.addEventListener(
                    "click",
                    () => {

                        const defaults = {
                            language: "fr",
                            langue: "fr",
                            theme: "light",
                            display: "standard",
                            notifications: true
                        };

                        saveSettings(
                            defaults
                        );

                        applyTheme(
                            "light"
                        );

                        applyDisplay(
                            "standard"
                        );

                        if (
                            typeof window.complianceForgeSetLanguage ===
                            "function"
                        ) {

                            window
                                .complianceForgeSetLanguage(
                                    "fr"
                                );
                        }

                        window.afficherParametres();
                    }
                );


            document
                .getElementById(
                    "cf-settings-logout"
                )
                ?.addEventListener(
                    "click",
                    () => {

                        try {
                            localStorage.removeItem(
                                "complianceforge_session"
                            );
                        } catch (_) {}

                        if (
                            typeof window.afficherPageDeconnexion ===
                            "function"
                        ) {

                            window.afficherPageDeconnexion();

                        } else {

                            location.hash =
                                "#logout";
                        }
                    }
                );
        };


    /*
     * ---------------------------------------------------------
     * MENU UTILISATEUR
     * ---------------------------------------------------------
     */

    window.complianceForgeTranslateUserMenu =
        function () {

            const lang =
                getLanguage();

            const labels = {

                fr: {
                    profile: "Mon profil",
                    settings: "Paramètres",
                    security: "Sécurité",
                    logout: "Se déconnecter"
                },

                en: {
                    profile: "My profile",
                    settings: "Settings",
                    security: "Security",
                    logout: "Log out"
                }

            }[lang];

            const items =
                document.querySelectorAll(
                    ".user-menu-item"
                );

            items.forEach(
                item => {

                    const id =
                        String(
                            item.id || ""
                        ).toLowerCase();

                    const text =
                        String(
                            item.textContent || ""
                        ).trim().toLowerCase();

                    if (
                        id.includes("profile") ||
                        text.includes("mon profil") ||
                        text.includes("my profile")
                    ) {

                        item.innerHTML =
                            `👤 ${labels.profile}`;

                    } else if (
                        id.includes("settings") ||
                        id.includes("param") ||
                        text.includes("paramètres") ||
                        text.includes("settings")
                    ) {

                        item.innerHTML =
                            `⚙️ ${labels.settings}`;

                    } else if (
                        id.includes("security") ||
                        text.includes("sécurité") ||
                        text.includes("security")
                    ) {

                        item.innerHTML =
                            `🔐 ${labels.security}`;

                    } else if (
                        id.includes("logout") ||
                        text.includes("déconnecter") ||
                        text.includes("log out")
                    ) {

                        item.innerHTML =
                            `🚪 ${labels.logout}`;
                    }
                }
            );
        };


    /*
     * Application initiale du thème.
     */
    const initial =
        getSettings();

    applyTheme(
        initial.theme
    );

    applyDisplay(
        initial.display
    );

    /*
     * Le menu peut être recréé dynamiquement.
     */
    setTimeout(
        () => {

            if (
                typeof window
                    .complianceForgeTranslateUserMenu ===
                "function"
            ) {

                window
                    .complianceForgeTranslateUserMenu();
            }

        },
        300
    );

})();



/* ============================================================
   COMPLIANCEFORGE — BOUTONS PARAMETRES FINAL
   ============================================================ */

/* ============================================================
   COMPLIANCEFORGE — BOUTONS PARAMETRES FINAL
   ------------------------------------------------------------
   Réinitialiser + Déconnexion
   ============================================================ */

(function ComplianceForgeSettingsButtonsFinal() {

    "use strict";

    const SETTINGS_KEY =
        "complianceforge_user_settings";

    let resetRunning = false;
    let logoutRunning = false;

    /*
     * ---------------------------------------------------------
     * RÉINITIALISATION
     * ---------------------------------------------------------
     */

    async function resetSettings() {

        if (resetRunning) {
            return;
        }

        resetRunning = true;

        const defaults = {
            language: "fr",
            langue: "fr",
            theme: "light",
            display: "standard",
            affichage: "standard",
            notifications: true
        };

        try {

            localStorage.setItem(
                SETTINGS_KEY,
                JSON.stringify(defaults)
            );

            /*
             * Nettoyage des anciennes clés pouvant
             * maintenir un ancien état.
             */
            localStorage.removeItem(
                "complianceforge_theme"
            );

            /*
             * Appliquer le thème clair.
             */
            document.documentElement.classList.remove(
                "dark-mode"
            );

            document.body.classList.remove(
                "dark-mode"
            );

            document.documentElement.dataset.theme =
                "light";

            document.body.dataset.theme =
                "light";

            /*
             * Appliquer le mode standard.
             */
            document.documentElement.classList.remove(
                "compact-mode"
            );

            document.body.classList.remove(
                "compact-mode"
            );

            document.body.dataset.display =
                "standard";

            /*
             * Remettre la langue française.
             */
            if (
                typeof window.complianceForgeSetLanguage ===
                "function"
            ) {

                await window.complianceForgeSetLanguage(
                    "fr"
                );
            }

            /*
             * Recharger les paramètres avec les
             * valeurs par défaut.
             */
            if (
                typeof window.afficherParametres ===
                "function"
            ) {

                window.afficherParametres();
            }

            console.info(
                "[ComplianceForge] Préférences réinitialisées."
            );

        } catch (error) {

            console.error(
                "[ComplianceForge] Erreur réinitialisation :",
                error
            );

        } finally {

            setTimeout(
                () => {
                    resetRunning = false;
                },
                300
            );
        }
    }

    /*
     * ---------------------------------------------------------
     * PAGE DE DÉCONNEXION
     * ---------------------------------------------------------
     */

    function showLogoutPage() {

        const container =
            document.querySelector(
                ".main-content"
            ) ||
            document.querySelector(
                "#main-content"
            ) ||
            document.querySelector(
                "main"
            );

        if (!container) {
            location.hash = "#logout";
            return;
        }

        container.innerHTML = `
            <div class="cf-logout-page">

                <div class="cf-logout-card">

                    <div class="cf-logout-icon">
                        ✓
                    </div>

                    <h1>
                        Déconnexion réussie
                    </h1>

                    <p>
                        Vous avez été déconnecté de votre espace
                        ComplianceForge.
                    </p>

                    <button
                        type="button"
                        id="cf-logout-return"
                        class="cf-btn-primary"
                    >
                        Retour à l'accueil
                    </button>

                </div>

            </div>
        `;

        document
            .getElementById(
                "cf-logout-return"
            )
            ?.addEventListener(
                "click",
                () => {

                    location.hash = "";

                    if (
                        typeof window.navigate ===
                        "function"
                    ) {

                        window.navigate(
                            "dashboard"
                        );
                    } else {

                        location.reload();
                    }
                }
            );
    }

    /*
     * ---------------------------------------------------------
     * DÉCONNEXION
     * ---------------------------------------------------------
     */

    function logout() {

        if (logoutRunning) {
            return;
        }

        logoutRunning = true;

        try {

            /*
             * Suppression complète de la session locale.
             * Aucun compte ne doit rester considéré comme connecté.
             */
            const sessionKeys = [
                "complianceforge_session",
                "complianceforge_auth",
                "complianceforge_token",
                "complianceforge_access_token",
                "complianceforge_authenticated_user",
                "complianceforge_current_user",
                "access_token",
                "token"
            ];

            sessionKeys.forEach(
                key => {
                    localStorage.removeItem(key);
                    sessionStorage.removeItem(key);
                }
            );

            /*
             * Nettoyage de l'utilisateur connecté en mémoire.
             */
            window.currentUser = null;
            window.currentUserProfile = null;
            window.complianceForgeUser = null;
            window.userProfile = null;

            /*
             * Retour DIRECT à la page de connexion.
             * Aucun retour au dashboard.
             */
            if (
                typeof window.complianceForgeShowLogin ===
                "function"
            ) {

                window.complianceForgeShowLogin();

            } else {

                console.error(
                    "[ComplianceForge] Écran de connexion introuvable."
                );

                /*
                 * Sécurité : si la fonction de connexion
                 * n'est pas disponible, on recharge la page
                 * après suppression du token.
                 */
                window.location.reload();
            }

            console.info(
                "[ComplianceForge] Déconnexion effectuée."
            );

        } catch (error) {

            console.error(
                "[ComplianceForge] Erreur déconnexion :",
                error
            );

            /*
             * Même en cas d'erreur, le token est supprimé.
             * On tente ensuite de présenter la connexion.
             */
            try {

                if (
                    typeof window.complianceForgeShowLogin ===
                    "function"
                ) {
                    window.complianceForgeShowLogin();
                } else {
                    window.location.reload();
                }

            } catch (loginError) {

                console.error(
                    "[ComplianceForge] Impossible d'afficher la connexion :",
                    loginError
                );

                window.location.reload();
            }

        } finally {

            setTimeout(
                () => {
                    logoutRunning = false;
                },
                500
            );
        }
    }

    /*
     * ---------------------------------------------------------
     * GESTIONNAIRE GLOBAL
     *
     * Utilise la capture pour prendre la priorité
     * sur les anciens listeners éventuellement présents.
     * ---------------------------------------------------------
     */

    if (
        !window.__cfFinalSettingsButtonsInstalled
    ) {

        document.addEventListener(
            "click",
            event => {

                const target =
                    event.target?.closest?.(
                        "#cf-settings-reset, #cf-settings-logout"
                    );

                if (!target) {
                    return;
                }

                /*
                 * Empêche les anciens gestionnaires
                 * de provoquer une deuxième action.
                 */
                event.preventDefault();
                event.stopPropagation();
                event.stopImmediatePropagation();

                if (
                    target.id ===
                    "cf-settings-reset"
                ) {

                    resetSettings();

                } else if (
                    target.id ===
                    "cf-settings-logout"
                ) {

                    logout();
                }

            },
            true
        );

        window.__cfFinalSettingsButtonsInstalled =
            true;
    }

    /*
     * API publique utile pour les tests.
     */
    window.complianceForgeResetSettings =
        resetSettings;

    window.complianceForgeLogout =
        logout;

})();






/* ============================================================
   COMPLIANCEFORGE — AVATAR DU COMPTE CONNECTÉ
   ============================================================ */

(function () {

    "use strict";

    function getConnectedUser() {

        /*
         * Priorité au compte/session actuellement connecté.
         */
        const candidates = [
            window.currentUser,
            window.currentUserProfile,
            window.complianceForgeUser,
            window.userProfile
        ];

        for (const user of candidates) {

            if (
                user &&
                typeof user === "object" &&
                (
                    user.nom ||
                    user.prenoms ||
                    user.prenom ||
                    user.name ||
                    user.firstName
                )
            ) {
                return user;
            }
        }

        /*
         * Session ComplianceForge.
         */
        const sessionKeys = [
            "complianceforge_session",
            "complianceforge_current_user",
            "currentUser"
        ];

        for (const key of sessionKeys) {

            try {

                const raw =
                    localStorage.getItem(key);

                if (!raw) {
                    continue;
                }

                const data =
                    JSON.parse(raw);

                const user =
                    data?.user ||
                    data?.utilisateur ||
                    data;

                if (
                    user &&
                    typeof user === "object" &&
                    (
                        user.nom ||
                        user.prenoms ||
                        user.prenom ||
                        user.name ||
                        user.firstName
                    )
                ) {
                    return user;
                }

            } catch (_) {}
        }

        /*
         * Profil local sauvegardé.
         */
        try {

            const raw =
                localStorage.getItem(
                    "complianceforge_user_profile"
                );

            if (raw) {

                const profile =
                    JSON.parse(raw);

                if (
                    profile &&
                    typeof profile === "object"
                ) {
                    return profile;
                }
            }

        } catch (_) {}

        return {};
    }


    function getInitiales(user) {

        const prenom = String(
            user.prenoms ||
            user.prenom ||
            user.firstName ||
            user.firstname ||
            ""
        ).trim();

        const nom = String(
            user.nom ||
            user.lastName ||
            user.lastname ||
            ""
        ).trim();

        /*
         * Exemple :
         * Yasmine + GATTA = YG
         */
        if (prenom && nom) {

            return (
                prenom.charAt(0) +
                nom.charAt(0)
            ).toUpperCase();
        }

        /*
         * Si uniquement le prénom.
         */
        if (prenom) {

            const mots =
                prenom
                    .split(/\s+/)
                    .filter(Boolean);

            if (mots.length >= 2) {

                return (
                    mots[0].charAt(0) +
                    mots[1].charAt(0)
                ).toUpperCase();
            }

            return mots[0]
                .charAt(0)
                .toUpperCase();
        }

        /*
         * Si uniquement le nom.
         */
        if (nom) {

            const mots =
                nom
                    .split(/\s+/)
                    .filter(Boolean);

            if (mots.length >= 2) {

                return (
                    mots[0].charAt(0) +
                    mots[1].charAt(0)
                ).toUpperCase();
            }

            return mots[0]
                .charAt(0)
                .toUpperCase();
        }

        return "U";
    }


    function updateConnectedUserAvatar() {

        const user =
            getConnectedUser();

        const initials =
            getInitiales(user);

        /*
         * Tous les avatars de l'interface.
         */
        document
            .querySelectorAll(
                ".user-avatar, " +
                ".user-avatar-large, " +
                "#user-avatar, " +
                "#user-avatar-button"
            )
            .forEach(
                avatar => {

                    if (
                        avatar.textContent.trim() !==
                        initials
                    ) {
                        avatar.textContent =
                            initials;
                    }

                    avatar.dataset.initials =
                        initials;
                }
            );

        /*
         * Nom affiché dans le menu utilisateur.
         */
        const name =
            [
                user.prenoms ||
                user.prenom ||
                user.firstName ||
                "",
                user.nom ||
                user.lastName ||
                user.lastname ||
                ""
            ]
            .filter(Boolean)
            .join(" ")
            .trim();

        if (name) {

            document
                .querySelectorAll(
                    ".user-menu-header strong"
                )
                .forEach(
                    element => {

                        if (
                            element.textContent.trim() !==
                            name
                        ) {
                            element.textContent =
                                name;
                        }
                    }
                );
        }

        window.complianceForgeUserInitials =
            initials;
    }


    /*
     * Fonction publique.
     * On pourra l'appeler après une connexion,
     * une modification du profil ou une reconnexion.
     */
    window.complianceForgeUpdateAvatar =
        updateConnectedUserAvatar;


    /*
     * UNE SEULE exécution au chargement.
     * Aucun MutationObserver permanent :
     * cela évite la boucle qui ralentissait Firefox.
     */
    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            updateConnectedUserAvatar,
            { once: true }
        );

    } else {

        updateConnectedUserAvatar();
    }

})();



/* ============================================================
   COMPLIANCEFORGE — AUTHENTIFICATION API
   ============================================================ */

(function () {

    "use strict";

    const API_BASE =
        window.COMPLIANCEFORGE_API_URL ||
        "https://api.complianceforge.test";

    const AUTH_TOKEN_KEY =
        "complianceforge_access_token";

    const AUTH_USER_KEY =
        "complianceforge_authenticated_user";


    function getToken() {
        return localStorage.getItem(
            AUTH_TOKEN_KEY
        );
    }


    function setToken(token) {

        if (!token) {
            return;
        }

        localStorage.setItem(
            AUTH_TOKEN_KEY,
            token
        );
    }


    function clearAuth() {

        localStorage.removeItem(
            AUTH_TOKEN_KEY
        );

        localStorage.removeItem(
            AUTH_USER_KEY
        );

        window.currentUser = null;
        window.currentUserProfile = null;
        window.complianceForgeUser = null;
    }


    async function getCurrentUser() {

        const token = getToken();

        /*
         * Aucun token = aucune session.
         */
        if (!token) {
            clearAuth();
            return null;
        }

        try {

            const response =
                await fetch(
                    `${API_BASE}/auth/me`,
                    {
                        method: "GET",
                        headers: {
                            "Authorization":
                                `Bearer ${token}`,
                            "Accept":
                                "application/json"
                        }
                    }
                );

            /*
             * Token absent, invalide ou expiré.
             */
            if (!response.ok) {

                clearAuth();

                return null;
            }

            const user =
                await response.json();

            /*
             * Utilisateur réellement authentifié.
             */
            window.currentUser = user;
            window.currentUserProfile = user;
            window.complianceForgeUser = user;

            localStorage.setItem(
                AUTH_USER_KEY,
                JSON.stringify(user)
            );

            localStorage.setItem(
                "complianceforge_current_user",
                JSON.stringify(user)
            );

            if (
                typeof window.complianceForgeUpdateAvatar ===
                "function"
            ) {
                window.complianceForgeUpdateAvatar();
            }

            return user;

        } catch (error) {

            /*
             * API inaccessible :
             * on ne considère jamais l'utilisateur
             * comme authentifié localement.
             */
            console.error(
                "[ComplianceForge] Vérification de session impossible :",
                error
            );

            clearAuth();

            return null;
        }
    }

    /*
     * API publique.
     */
    window.complianceForgeAuth = {
        getToken,
        setToken,
        getCurrentUser,
        login: (typeof login === "function") ? login : undefined,
        logout: (typeof logoutAuth === "function") ? logoutAuth : undefined,
        clearAuth
    };


    /*
     * Restaurer automatiquement la session
     * lorsqu'une session existe.
     */
    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            function () {
                try { Promise.resolve(getCurrentUser()).catch(function (e) { console.warn("[ComplianceForge] Session non restaurée :", e); }); } catch (e) { console.warn("[ComplianceForge] Session non restaurée :", e); }
            },
            { once: true }
        );

    } else {

        try { Promise.resolve(getCurrentUser()).catch(function (e) { console.warn("[ComplianceForge] Session non restaurée :", e); }); } catch (e) { console.warn("[ComplianceForge] Session non restaurée :", e); }
    }

})();


/* ============================================================
   COMPLIANCEFORGE — ÉCRAN CONNEXION / INSCRIPTION
   ============================================================ */

(function () {

    "use strict";

    const AUTH_TOKEN_KEY =
        "complianceforge_access_token";

    const API_BASE =
        window.COMPLIANCEFORGE_API_URL ||
        "https://api.complianceforge.test";


    function createAuthScreen() {

        if (
            document.getElementById(
                "cf-auth-overlay"
            )
        ) {
            return;
        }

        const overlay =
            document.createElement("div");

        overlay.id =
            "cf-auth-overlay";

        overlay.className =
            "cf-auth-overlay";

        overlay.innerHTML = `

            <div class="cf-auth-card">

                <div class="cf-auth-brand">

                    <div class="cf-auth-logo">
                        CF
                    </div>

                    <h1>ComplianceForge</h1>

                    <p>
                        Plateforme GRC-as-Code
                    </p>

                </div>


                <!-- CONNEXION -->

                <section
                    id="cf-login-section"
                >

                    <form
                        id="cf-login-form"
                        class="cf-auth-form"
                    >

                        <div class="cf-auth-field">

                            <label for="cf-login-email">
                                Adresse e-mail
                            </label>

                            <input
                                id="cf-login-email"
                                type="email"
                                autocomplete="email"
                                required
                            >

                        </div>


                        <div class="cf-auth-field">

                            <label for="cf-login-password">
                                Mot de passe
                            </label>

                            <input
                                id="cf-login-password"
                                type="password"
                                autocomplete="current-password"
                                required
                            >

                        </div>


                        <div
                            id="cf-login-message"
                            class="cf-auth-message"
                        ></div>


                        <button
                            type="submit"
                            class="cf-auth-submit"
                            id="cf-login-submit"
                        >
                            Se connecter
                        </button>

                    </form>


                    <div class="cf-auth-footer">

                        Pas encore de compte ?

                        <button
                            type="button"
                            class="cf-auth-link"
                            id="cf-show-register"
                        >
                            Créer un compte
                        </button>

                    </div>

                </section>


                <!-- INSCRIPTION -->

                <section
                    id="cf-register-section"
                    class="cf-auth-section-hidden"
                >

                    <form
                        id="cf-register-form"
                        class="cf-auth-form"
                    >

                        <div class="cf-auth-field">

                            <label for="cf-register-nom">
                                Nom
                            </label>

                            <input
                                id="cf-register-nom"
                                type="text"
                                autocomplete="family-name"
                                required
                            >

                        </div>


                        <div class="cf-auth-field">

                            <label for="cf-register-prenoms">
                                Prénoms
                            </label>

                            <input
                                id="cf-register-prenoms"
                                type="text"
                                autocomplete="given-name"
                            >

                        </div>


                        <div class="cf-auth-field">

                            <label for="cf-register-email">
                                Adresse e-mail
                            </label>

                            <input
                                id="cf-register-email"
                                type="email"
                                autocomplete="email"
                                required
                            >

                            <small>
                                L'adresse e-mail doit être entièrement en minuscules.
                            </small>

                        </div>


                        <div class="cf-auth-field">

                            <label for="cf-register-fonction">
                                Fonction
                            </label>

                            <input
                                id="cf-register-fonction"
                                type="text"
                                autocomplete="organization-title"
                            >

                        </div>


                        <div class="cf-auth-field">

                            <label for="cf-register-password">
                                Mot de passe
                            </label>

                            <input
                                id="cf-register-password"
                                type="password"
                                minlength="8"
                                autocomplete="new-password"
                                required
                            >

                            <small>
                                Minimum 8 caractères : 1 lettre, 1 chiffre et 1 caractère spécial.
                            </small>

                        </div>


                        <div
                            id="cf-register-message"
                            class="cf-auth-message"
                        ></div>


                        <button
                            type="submit"
                            class="cf-auth-submit"
                            id="cf-register-submit"
                        >
                            Créer mon compte
                        </button>

                    </form>


                    <div class="cf-auth-footer">

                        Déjà un compte ?

                        <button
                            type="button"
                            class="cf-auth-link"
                            id="cf-show-login"
                        >
                            Se connecter
                        </button>

                    </div>

                </section>


                <!-- VERIFICATION -->

                <section
                    id="cf-verify-section"
                    class="cf-auth-section-hidden"
                >

                    <div class="cf-auth-form">

                        <div>

                            <h2
                                style="
                                    margin:0 0 8px;
                                    color:#172033;
                                    font-size:20px;
                                "
                            >
                                Vérifiez votre adresse e-mail
                            </h2>

                            <p
                                style="
                                    margin:0;
                                    color:#64748b;
                                    font-size:14px;
                                    line-height:1.5;
                                "
                            >
                                Votre compte a été créé.
                                Vérifiez votre adresse e-mail
                                avant de vous connecter.
                            </p>

                        </div>


                        <div class="cf-auth-field">

                            <label for="cf-verify-token">
                                Token de vérification
                            </label>

                            <input
                                id="cf-verify-token"
                                type="text"
                                autocomplete="off"
                                required
                            >

                        </div>


                        <div
                            id="cf-verify-message"
                            class="cf-auth-message"
                        ></div>


                        <button
                            type="button"
                            class="cf-auth-submit"
                            id="cf-verify-submit"
                        >
                            Vérifier mon adresse
                        </button>


                        <button
                            type="button"
                            class="cf-auth-secondary"
                            id="cf-verify-back"
                        >
                            Retour à la connexion
                        </button>

                    </div>

                </section>

            </div>
        `;

        document.body.appendChild(
            overlay
        );

        bindAuthEvents();

    }


    function showSection(section) {

        const sections = [
            "cf-login-section",
            "cf-register-section",
            "cf-verify-section"
        ];

        sections.forEach(id => {

            const element =
                document.getElementById(id);

            if (!element) {
                return;
            }

            element.classList.toggle(
                "cf-auth-section-hidden",
                id !== section
            );
        });

        clearMessages();

    }


    function clearMessages() {

        document
            .querySelectorAll(
                ".cf-auth-message"
            )
            .forEach(element => {

                element.textContent = "";

                element.classList.remove(
                    "show",
                    "error",
                    "success"
                );

            });
    }


    function showMessage(
        id,
        message,
        type
    ) {

        const element =
            document.getElementById(id);

        if (!element) {
            return;
        }

        element.textContent =
            message;

        element.classList.add(
            "show",
            type
        );
    }


    async function apiLogin(
        email,
        password
    ) {

        const response =
            await fetch(
                `${API_BASE}/auth/login`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/json",
                        "Accept":
                            "application/json"
                    },
                    body: JSON.stringify({
                        email,
                        mot_de_passe: password
                    })
                }
            );

        const data =
            await response.json();

        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Connexion impossible."
            );
        }

        localStorage.setItem(
            AUTH_TOKEN_KEY,
            data.access_token
        );

        return data;
    }


    async function apiCurrentUser() {

        const token =
            localStorage.getItem(
                AUTH_TOKEN_KEY
            );

        if (!token) {
            return null;
        }

        const response =
            await fetch(
                `${API_BASE}/auth/me`,
                {
                    headers: {
                        "Authorization":
                            `Bearer ${token}`,
                        "Accept":
                            "application/json"
                    }
                }
            );

        if (!response.ok) {

            localStorage.removeItem(
                AUTH_TOKEN_KEY
            );

            return null;
        }

        return response.json();
    }


    async function apiRegister(data) {

        const response =
            await fetch(
                `${API_BASE}/auth/register`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/json",
                        "Accept":
                            "application/json"
                    },
                    body: JSON.stringify(data)
                }
            );

        const result =
            await response.json();

        if (!response.ok) {

            const detail =
                Array.isArray(result.detail)
                    ? result.detail
                        .map(item => item.msg)
                        .join(" ")
                    : result.detail;

            throw new Error(
                detail ||
                "Création du compte impossible."
            );
        }

        return result;
    }


    async function apiVerifyEmail(
        token
    ) {

        const response =
            await fetch(
                `${API_BASE}/auth/verify-email?token=${encodeURIComponent(token)}`
            );

        const result =
            await response.json();

        if (!response.ok) {

            throw new Error(
                result.detail ||
                "Vérification impossible."
            );
        }

        return result;
    }


    async function loginSubmit(
        event
    ) {

        event.preventDefault();

        const email =
            document
                .getElementById(
                    "cf-login-email"
                )
                .value
                .trim();

        const password =
            document
                .getElementById(
                    "cf-login-password"
                )
                .value;

        const button =
            document.getElementById(
                "cf-login-submit"
            );

        try {

            button.disabled = true;

            clearMessages();

            await apiLogin(
                email,
                password
            );

            const user =
                await apiCurrentUser();

            if (!user) {

                throw new Error(
                    "Impossible de récupérer le compte connecté."
                );
            }

            /*
             * Alimente le système d'avatar
             * déjà présent dans ComplianceForge.
             */
            window.currentUser =
                user;

            window.currentUserProfile =
                user;

            window.complianceForgeUser =
                user;

            localStorage.setItem(
                "complianceforge_current_user",
                JSON.stringify(user)
            );

            if (
                typeof window.complianceForgeUpdateAvatar ===
                "function"
            ) {
                window.complianceForgeUpdateAvatar();
            }

            hideAuth();

        } catch (error) {

            showMessage(
                "cf-login-message",
                error.message,
                "error"
            );

        } finally {

            button.disabled = false;

        }
    }


    async function registerSubmit(
        event
    ) {

        event.preventDefault();

        const button =
            document.getElementById(
                "cf-register-submit"
            );

        const data = {
            nom:
                document
                    .getElementById(
                        "cf-register-nom"
                    )
                    .value
                    .trim(),

            prenoms:
                document
                    .getElementById(
                        "cf-register-prenoms"
                    )
                    .value
                    .trim() || null,

            email:
                document
                    .getElementById(
                        "cf-register-email"
                    )
                    .value
                    .trim(),

            fonction:
                document
                    .getElementById(
                        "cf-register-fonction"
                    )
                    .value
                    .trim() || null,

            mot_de_passe:
                document
                    .getElementById(
                        "cf-register-password"
                    )
                    .value
        };

        const emailCheck =
            window.complianceForgeValidateEmail(
                data.email
            );

        if (!emailCheck.valid) {
            showMessage(
                "cf-register-message",
                emailCheck.message,
                "error"
            );
            return;
        }

        const passwordCheck =
            window.complianceForgeValidatePassword(
                data.mot_de_passe
            );

        if (!passwordCheck.valid) {
            showMessage(
                "cf-register-message",
                passwordCheck.message,
                "error"
            );
            return;
        }


        try {

            button.disabled = true;

            clearMessages();

            await apiRegister(
                data
            );

            /*
             * Le backend est actuellement
             * en mode développement :
             * le token est dans les logs API.
             */
            showSection(
                "cf-verify-section"
            );

            showMessage(
                "cf-verify-message",
                "Compte créé. Récupérez le token de vérification dans les logs de l'API pour le test en mode développement.",
                "success"
            );

        } catch (error) {

            showMessage(
                "cf-register-message",
                error.message,
                "error"
            );

        } finally {

            button.disabled = false;

        }
    }


    async function verifySubmit() {

        const token =
            document
                .getElementById(
                    "cf-verify-token"
                )
                .value
                .trim();

        if (!token) {
            return;
        }

        const button =
            document.getElementById(
                "cf-verify-submit"
            );

        try {

            button.disabled = true;

            clearMessages();

            await apiVerifyEmail(
                token
            );

            showMessage(
                "cf-verify-message",
                "Adresse e-mail vérifiée. Vous pouvez maintenant vous connecter.",
                "success"
            );

            setTimeout(
                () => {
                    showSection(
                        "cf-login-section"
                    );
                },
                1200
            );

        } catch (error) {

            showMessage(
                "cf-verify-message",
                error.message,
                "error"
            );

        } finally {

            button.disabled = false;

        }
    }


    function bindAuthEvents() {

        document
            .getElementById(
                "cf-login-form"
            )
            .addEventListener(
                "submit",
                loginSubmit
            );

        document
            .getElementById(
                "cf-register-form"
            )
            .addEventListener(
                "submit",
                registerSubmit
            );

        document
            .getElementById(
                "cf-show-register"
            )
            .addEventListener(
                "click",
                () => showSection(
                    "cf-register-section"
                )
            );

        document
            .getElementById(
                "cf-show-login"
            )
            .addEventListener(
                "click",
                () => showSection(
                    "cf-login-section"
                )
            );

        document
            .getElementById(
                "cf-verify-submit"
            )
            .addEventListener(
                "click",
                verifySubmit
            );

        document
            .getElementById(
                "cf-verify-back"
            )
            .addEventListener(
                "click",
                () => showSection(
                    "cf-login-section"
                )
            );

    }


    /*
     * Éléments du shell masqués pendant l'authentification.
     */
    const CF_AUTH_HIDDEN_ELEMENTS = new Map();


    function hideApplicationShell() {

        const overlay =
            document.getElementById(
                "cf-auth-overlay"
            );

        /*
         * L'overlay doit être directement dans BODY
         * afin de pouvoir rester visible lorsque le shell
         * est masqué.
         */
        if (
            overlay &&
            overlay.parentElement !== document.body
        ) {
            document.body.appendChild(overlay);
        }

        /*
         * Masquer tous les éléments directs du BODY
         * sauf l'écran d'authentification.
         */
        Array.from(
            document.body.children
        ).forEach(
            element => {

                if (
                    element === overlay ||
                    element.tagName === "SCRIPT" ||
                    element.tagName === "STYLE"
                ) {
                    return;
                }

                if (
                    !CF_AUTH_HIDDEN_ELEMENTS.has(
                        element
                    )
                ) {
                    CF_AUTH_HIDDEN_ELEMENTS.set(
                        element,
                        {
                            display:
                                element.style.display,
                            visibility:
                                element.style.visibility,
                            pointerEvents:
                                element.style.pointerEvents
                        }
                    );
                }

                element.style.display =
                    "none";

                element.style.visibility =
                    "hidden";

                element.style.pointerEvents =
                    "none";
            }
        );
    }


    function restoreApplicationShell() {

        CF_AUTH_HIDDEN_ELEMENTS.forEach(
            (styles, element) => {

                element.style.display =
                    styles.display;

                element.style.visibility =
                    styles.visibility;

                element.style.pointerEvents =
                    styles.pointerEvents;
            }
        );

        CF_AUTH_HIDDEN_ELEMENTS.clear();
    }


    function hideAuth() {

        const overlay =
            document.getElementById(
                "cf-auth-overlay"
            );

        /*
         * Cacher complètement l'écran de connexion.
         */
        if (overlay) {

            overlay.classList.add(
                "cf-auth-hidden"
            );

            overlay.style.setProperty(
                "display",
                "none",
                "important"
            );
        }

        /*
         * Restaurer le shell de ComplianceForge.
         */
        if (
            Array.isArray(
                window.__cfAuthHiddenElements
            )
        ) {

            window.__cfAuthHiddenElements.forEach(
                item => {

                    if (
                        item.element &&
                        item.element.isConnected
                    ) {

                        item.element.style.display =
                            item.display;

                        item.element.style.visibility =
                            item.visibility;

                        item.element.style.pointerEvents =
                            item.pointerEvents;
                    }
                }
            );

            window.__cfAuthHiddenElements = [];
        }

        document.body.classList.remove(
            "cf-auth-locked"
        );

        document.body.style.overflow =
            "";

        if (
            typeof window.complianceForgeUpdateAvatar ===
            "function"
        ) {
            window.complianceForgeUpdateAvatar();
        }
    }


    function showAuth() {

        const overlay =
            document.getElementById(
                "cf-auth-overlay"
            );

        if (!overlay) {
            console.error(
                "[ComplianceForge] Overlay de connexion introuvable."
            );
            return;
        }

        /*
         * L'overlay doit être directement dans BODY.
         */
        if (
            overlay.parentElement !== document.body
        ) {
            document.body.appendChild(overlay);
        }

        /*
         * Mémoriser les éléments du BODY que nous masquons.
         */
        window.__cfAuthHiddenElements = [];

        Array.from(
            document.body.children
        ).forEach(
            element => {

                if (
                    element === overlay ||
                    element.tagName === "SCRIPT" ||
                    element.tagName === "STYLE"
                ) {
                    return;
                }

                window.__cfAuthHiddenElements.push({
                    element: element,
                    display: element.style.display,
                    visibility: element.style.visibility,
                    pointerEvents: element.style.pointerEvents
                });

                element.style.setProperty(
                    "display",
                    "none",
                    "important"
                );

                element.style.setProperty(
                    "visibility",
                    "hidden",
                    "important"
                );

                element.style.setProperty(
                    "pointer-events",
                    "none",
                    "important"
                );
            }
        );

        /*
         * Afficher l'authentification.
         */
        overlay.classList.remove(
            "cf-auth-hidden"
        );

        overlay.style.setProperty(
            "display",
            "flex",
            "important"
        );

        overlay.style.setProperty(
            "position",
            "fixed",
            "important"
        );

        overlay.style.setProperty(
            "top",
            "0",
            "important"
        );

        overlay.style.setProperty(
            "right",
            "0",
            "important"
        );

        overlay.style.setProperty(
            "bottom",
            "0",
            "important"
        );

        overlay.style.setProperty(
            "left",
            "0",
            "important"
        );

        overlay.style.setProperty(
            "width",
            "100vw",
            "important"
        );

        overlay.style.setProperty(
            "height",
            "100vh",
            "important"
        );

        overlay.style.setProperty(
            "visibility",
            "visible",
            "important"
        );

        overlay.style.setProperty(
            "opacity",
            "1",
            "important"
        );

        overlay.style.setProperty(
            "pointer-events",
            "auto",
            "important"
        );

        overlay.style.setProperty(
            "z-index",
            "2147483647",
            "important"
        );

        overlay.style.setProperty(
            "background",
            "#f4f7fb",
            "important"
        );

        document.body.classList.add(
            "cf-auth-locked"
        );

        document.body.style.overflow =
            "hidden";
    }


    async function initializeAuth() {

        createAuthScreen();

        const user =
            await apiCurrentUser();

        if (user) {

            window.currentUser =
                user;

            window.currentUserProfile =
                user;

            window.complianceForgeUser =
                user;

            localStorage.setItem(
                "complianceforge_current_user",
                JSON.stringify(user)
            );

            hideAuth();

            if (
                typeof window.complianceForgeUpdateAvatar ===
                "function"
            ) {
                window.complianceForgeUpdateAvatar();
            }

            return;
        }

        showAuth();

    }


    /*
     * Vérification automatique d'un token passé
     * dans l'URL :
     *
     * ?verify=TOKEN
     */
    async function handleVerificationUrl() {

        const params =
            new URLSearchParams(
                window.location.search
            );

        const token =
            params.get("verify");

        if (!token) {
            return;
        }

        showSection(
            "cf-verify-section"
        );

        document
            .getElementById(
                "cf-verify-token"
            )
            .value = token;

        await verifySubmit();

        window.history.replaceState(
            {},
            document.title,
            window.location.pathname +
            window.location.hash
        );

    }


    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            async () => {
                await initializeAuth();
                await handleVerificationUrl();
            },
            { once: true }
        );

    } else {

        initializeAuth()
            .then(
                handleVerificationUrl
            );

    }


    /*
     * API publique.
     */
    window.complianceForgeShowLogin =
        () => {
            showSection(
                "cf-login-section"
            );
            showAuth();
        };

    window.complianceForgeShowRegister =
        () => {
            showSection(
                "cf-register-section"
            );
            showAuth();
        };

})();


/* ============================================================
   COMPLIANCEFORGE — CHANGEMENT DU MOT DE PASSE
   ============================================================ */

(function () {

    "use strict";

    const API_BASE =
        window.COMPLIANCEFORGE_API_URL ||
        "https://api.complianceforge.test";

    const TOKEN_KEY =
        "complianceforge_access_token";


    function createPasswordModal() {

        if (
            document.getElementById(
                "cf-password-modal"
            )
        ) {
            return;
        }

        const modal =
            document.createElement("div");

        modal.id =
            "cf-password-modal";

        modal.className =
            "cf-security-modal";

        modal.innerHTML = `

            <div
                class="cf-security-modal-card"
                role="dialog"
                aria-modal="true"
                aria-labelledby="cf-password-title"
            >

                <div class="cf-security-modal-header">

                    <div>
                        <h2 id="cf-password-title">
                            Modifier le mot de passe
                        </h2>

                        <p>
                            Choisissez un nouveau mot de passe
                            pour votre compte.
                        </p>
                    </div>

                    <button
                        type="button"
                        class="cf-security-modal-close"
                        id="cf-password-close"
                        aria-label="Fermer"
                    >
                        ×
                    </button>

                </div>


                <form
                    id="cf-password-form"
                    class="cf-security-password-form"
                >

                    <div class="cf-security-field">

                        <label for="cf-old-password">
                            Ancien mot de passe
                        </label>

                        <input
                            id="cf-old-password"
                            type="password"
                            autocomplete="current-password"
                            required
                        >

                    </div>


                    <div class="cf-security-field">

                        <label for="cf-new-password">
                            Nouveau mot de passe
                        </label>

                        <input
                            id="cf-new-password"
                            type="password"
                            minlength="8"
                            maxlength="128"
                            autocomplete="new-password"
                            required
                        >

                        <small>
                            Minimum 8 caractères.
                        </small>

                    </div>


                    <div class="cf-security-field">

                        <label for="cf-confirm-password">
                            Confirmer le nouveau mot de passe
                        </label>

                        <input
                            id="cf-confirm-password"
                            type="password"
                            minlength="8"
                            maxlength="128"
                            autocomplete="new-password"
                            required
                        >

                    </div>


                    <div
                        id="cf-password-message"
                        class="cf-security-message"
                    ></div>


                    <div class="cf-security-modal-actions">

                        <button
                            type="button"
                            class="user-btn-secondary"
                            id="cf-password-cancel"
                        >
                            Annuler
                        </button>

                        <button
                            type="submit"
                            class="user-btn-primary"
                            id="cf-password-submit"
                        >
                            Modifier le mot de passe
                        </button>

                    </div>

                </form>

            </div>
        `;

        document.body.appendChild(modal);

        bindPasswordModal();

    }


    function showPasswordModal() {

        createPasswordModal();

        const modal =
            document.getElementById(
                "cf-password-modal"
            );

        modal.classList.add("is-open");

        document.body.style.overflow =
            "hidden";

        const oldPassword =
            document.getElementById(
                "cf-old-password"
            );

        setTimeout(
            () => oldPassword?.focus(),
            50
        );
    }


    function hidePasswordModal() {

        const modal =
            document.getElementById(
                "cf-password-modal"
            );

        if (!modal) {
            return;
        }

        modal.classList.remove(
            "is-open"
        );

        document.body.style.overflow =
            "";

        document
            .getElementById(
                "cf-password-form"
            )
            ?.reset();

        const message =
            document.getElementById(
                "cf-password-message"
            );

        if (message) {
            message.textContent = "";
            message.className =
                "cf-security-message";
        }
    }


    function showPasswordMessage(
        message,
        type
    ) {

        const element =
            document.getElementById(
                "cf-password-message"
            );

        if (!element) {
            return;
        }

        element.textContent =
            message;

        element.className =
            `cf-security-message ${type}`;

    }


    async function changePassword(
        event
    ) {

        event.preventDefault();

        const token =
            localStorage.getItem(
                TOKEN_KEY
            );

        if (!token) {

            showPasswordMessage(
                "Votre session a expiré. Veuillez vous reconnecter.",
                "error"
            );

            return;
        }

        const oldPassword =
            document
                .getElementById(
                    "cf-old-password"
                )
                .value;

        const newPassword =
            document
                .getElementById(
                    "cf-new-password"
                )
                .value;

        const confirmPassword =
            document
                .getElementById(
                    "cf-confirm-password"
                )
                .value;

        const passwordCheck =
            window.complianceForgeValidatePassword(
                newPassword
            );

        if (!passwordCheck.valid) {
            showPasswordMessage(
                passwordCheck.message,
                "error"
            );
            return;
        }

        if (
            newPassword !==
            confirmPassword
        ) {

            showPasswordMessage(
                "Les deux nouveaux mots de passe ne correspondent pas.",
                "error"
            );

            return;
        }

        if (newPassword.length < 8) {

            showPasswordMessage(
                "Le nouveau mot de passe doit contenir au moins 8 caractères.",
                "error"
            );

            return;
        }

        const button =
            document.getElementById(
                "cf-password-submit"
            );

        try {

            button.disabled = true;

            const response =
                await fetch(
                    `${API_BASE}/auth/change-password`,
                    {
                        method: "POST",
                        headers: {
                            "Content-Type":
                                "application/json",
                            "Authorization":
                                `Bearer ${token}`,
                            "Accept":
                                "application/json"
                        },
                        body: JSON.stringify({
                            ancien_mot_de_passe:
                                oldPassword,
                            nouveau_mot_de_passe:
                                newPassword
                        })
                    }
                );

            const data =
                await response.json();

            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    "Impossible de modifier le mot de passe."
                );
            }

            showPasswordMessage(
                "Mot de passe modifié avec succès.",
                "success"
            );

            setTimeout(
                hidePasswordModal,
                1200
            );

        } catch (error) {

            showPasswordMessage(
                error.message,
                "error"
            );

        } finally {

            button.disabled = false;

        }
    }


    function bindPasswordModal() {

        document
            .getElementById(
                "cf-password-form"
            )
            .addEventListener(
                "submit",
                changePassword
            );

        document
            .getElementById(
                "cf-password-close"
            )
            .addEventListener(
                "click",
                hidePasswordModal
            );

        document
            .getElementById(
                "cf-password-cancel"
            )
            .addEventListener(
                "click",
                hidePasswordModal
            );

        document
            .getElementById(
                "cf-password-modal"
            )
            .addEventListener(
                "click",
                event => {

                    if (
                        event.target.id ===
                        "cf-password-modal"
                    ) {
                        hidePasswordModal();
                    }

                }
            );

    }


    function bindPasswordButton() {

        const button =
            document.getElementById(
                "cf-change-password-button"
            );

        if (!button) {
            return;
        }

        if (
            button.dataset.authBound ===
            "true"
        ) {
            return;
        }

        button.dataset.authBound =
            "true";

        button.addEventListener(
            "click",
            showPasswordModal
        );
    }


    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            () => {

                createPasswordModal();
                bindPasswordButton();

            },
            { once: true }
        );

    } else {

        createPasswordModal();
        bindPasswordButton();

    }


    window.complianceForgeShowPasswordModal =
        showPasswordModal;

})();


/* ============================================================
   COMPLIANCEFORGE — CORRECTION BOUTON MOT DE PASSE DYNAMIQUE
   ============================================================ */

(function () {

    "use strict";

    if (window.__cfPasswordDelegatedClick) {
        return;
    }

    window.__cfPasswordDelegatedClick = true;

    document.addEventListener(
        "click",
        function (event) {

            const button =
                event.target.closest(
                    "#cf-change-password-button"
                );

            if (!button) {
                return;
            }

            event.preventDefault();
            event.stopPropagation();

            if (
                typeof window.complianceForgeShowPasswordModal ===
                "function"
            ) {
                window.complianceForgeShowPasswordModal();
            }

        },
        true
    );

})();


/* ============================================================
   COMPLIANCEFORGE — POLITIQUE MOT DE PASSE / E-MAIL
   ============================================================ */

(function () {

    "use strict";

    window.complianceForgeValidatePassword =
        function (password) {

            if (password.length < 8) {
                return {
                    valid: false,
                    message:
                        "Le mot de passe doit contenir au moins 8 caractères."
                };
            }

            if (!/[A-Za-z]/.test(password)) {
                return {
                    valid: false,
                    message:
                        "Le mot de passe doit contenir au moins une lettre."
                };
            }

            if (!/[0-9]/.test(password)) {
                return {
                    valid: false,
                    message:
                        "Le mot de passe doit contenir au moins un chiffre."
                };
            }

            if (!/[^A-Za-z0-9]/.test(password)) {
                return {
                    valid: false,
                    message:
                        "Le mot de passe doit contenir au moins un caractère spécial."
                };
            }

            return {
                valid: true,
                message: ""
            };
        };


    window.complianceForgeValidateEmail =
        function (email) {

            const value =
                String(email || "").trim();

            if (value !== value.toLowerCase()) {
                return {
                    valid: false,
                    message:
                        "L'adresse e-mail doit être entièrement en minuscules."
                };
            }

            if (
                !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(
                    value
                )
            ) {
                return {
                    valid: false,
                    message:
                        "Veuillez saisir une adresse e-mail valide."
                };
            }

            return {
                valid: true,
                message: ""
            };
        };

})();


/* ============================================================
   COMPLIANCEFORGE — SESSION ACTUELLE
   ============================================================ */

(function initComplianceForgeCurrentSession() {

    const SESSION_STARTED_KEY =
        "complianceforge_session_started_at";

    function getBrowserName() {

        const ua = navigator.userAgent;

        if (ua.includes("Edg/")) {
            return "Microsoft Edge";
        }

        if (ua.includes("Firefox/")) {
            return "Mozilla Firefox";
        }

        if (ua.includes("Chrome/") && !ua.includes("Edg/")) {
            return "Google Chrome";
        }

        if (ua.includes("Safari/") && !ua.includes("Chrome/")) {
            return "Safari";
        }

        return "Navigateur web";
    }

    function getOperatingSystem() {

        const ua = navigator.userAgent;

        if (ua.includes("Windows")) {
            return "Windows";
        }

        if (ua.includes("Linux")) {
            return "Linux";
        }

        if (ua.includes("Mac OS")) {
            return "macOS";
        }

        if (ua.includes("Android")) {
            return "Android";
        }

        if (
            ua.includes("iPhone") ||
            ua.includes("iPad")
        ) {
            return "iOS";
        }

        return "Système inconnu";
    }

    function formatDate(value) {

        if (!value) {
            return "—";
        }

        const date = new Date(value);

        if (Number.isNaN(date.getTime())) {
            return "—";
        }

        return date.toLocaleString(
            "fr-FR",
            {
                day: "2-digit",
                month: "2-digit",
                year: "numeric",
                hour: "2-digit",
                minute: "2-digit"
            }
        );
    }

    function initializeSession() {

        const token =
            localStorage.getItem(
                "complianceforge_access_token"
            );

        if (!token) {
            return;
        }

        let started =
            localStorage.getItem(
                SESSION_STARTED_KEY
            );

        if (!started) {

            started =
                new Date().toISOString();

            localStorage.setItem(
                SESSION_STARTED_KEY,
                started
            );
        }

        const device =
            document.getElementById(
                "cf-session-device"
            );

        const startedElement =
            document.getElementById(
                "cf-session-started"
            );

        const activity =
            document.getElementById(
                "cf-session-last-activity"
            );

        if (device) {

            device.textContent =
                `${getBrowserName()} · ${getOperatingSystem()}`;
        }

        if (startedElement) {

            startedElement.textContent =
                `Session active depuis : ${formatDate(started)}`;
        }

        if (activity) {

            activity.textContent =
                `Dernière activité : ${formatDate(new Date())}`;
        }
    }



    document.addEventListener(
        "click",
        function(event) {

            if (
                event.target.closest(
                    "#cf-session-logout"
                )
            ) {
                return;
            }
        },
        true
    );

    document.addEventListener(
        "click",
        function(event) {

            if (
                event.target.closest(
                    "#cf-session-logout"
                )
            ) {
                return;
            }

            const token =
                localStorage.getItem(
                    "complianceforge_access_token"
                );

            if (token) {

                const activity =
                    document.getElementById(
                        "cf-session-last-activity"
                    );

                if (activity) {

                    activity.textContent =
                        `Dernière activité : ${formatDate(new Date())}`;
                }
            }
        },
        true
    );

    window.complianceForgeInitCurrentSession =
        initializeSession;

    initializeSession();

})();



/* ============================================================
   CORRECTION — INITIALISATION SESSION APRÈS RENDU DE LA PAGE
   ============================================================ */

(function fixComplianceForgeSessionRendering() {

    function refreshSessionDisplay() {

        if (
            typeof window.complianceForgeInitCurrentSession ===
            "function"
        ) {
            window.complianceForgeInitCurrentSession();
        }
    }

    document.addEventListener(
        "click",
        function(event) {

            const target =
                event.target.closest(
                    '[onclick*="securite"], ' +
                    '[data-page="securite"], ' +
                    '[data-section="securite"]'
                );

            if (!target) {
                return;
            }

            setTimeout(
                refreshSessionDisplay,
                100
            );
        },
        true
    );

    const observer =
        new MutationObserver(function() {

            const sessionDevice =
                document.getElementById(
                    "cf-session-device"
                );

            if (!sessionDevice) {
                return;
            }

            refreshSessionDisplay();

            observer.disconnect();
        });

    observer.observe(
        document.body,
        {
            childList: true,
            subtree: true
        }
    );

})();


// ============================================================
// JOURNAL DE SÉCURITÉ — API
// ============================================================

window.complianceForgeLoadSecurityLog = async function () {
    const container = document.getElementById(
        "cf-security-log-container"
    );

    if (!container) {
        return;
    }

    const token = localStorage.getItem(
        "complianceforge_access_token"
    );

    if (!token) {
        container.innerHTML = `
            <div class="security-empty">
                Aucune session authentifiée.
            </div>
        `;
        return;
    }

    try {
        const response = await fetch(
            "https://api.complianceforge.test/auth/security-log",
            {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }
        );

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const events = await response.json();

        if (!events.length) {
            container.innerHTML = `
                <div class="security-empty">
                    Aucun événement de sécurité enregistré.
                </div>
            `;
            return;
        }

        const labels = {
            CONNEXION_REUSSIE: "Connexion réussie",
            ECHEC_CONNEXION: "Échec de connexion",
            EMAIL_VERIFIE: "Adresse e-mail vérifiée",
            CHANGEMENT_MOT_DE_PASSE: "Mot de passe modifié",
            DEMANDE_RESET_MOT_DE_PASSE:
                "Demande de réinitialisation",
            RESET_MOT_DE_PASSE:
                "Mot de passe réinitialisé"
        };

        container.innerHTML = events.map((event) => {
            const date = new Date(event.date_evenement);

            const dateFormatee =
                date.toLocaleString("fr-FR", {
                    dateStyle: "short",
                    timeStyle: "medium"
                });

            const label =
                labels[event.evenement]
                || event.evenement;

            const userAgent =
                event.user_agent
                || "Navigateur non identifié";

            const ip = event.adresse_ip
                ? `IP : ${event.adresse_ip}`
                : "";

            return `
                <div class="security-log-item">
                    <div class="security-log-main">
                        <strong>${label}</strong>

                        <span>
                            ${event.description}
                        </span>

                        <small>
                            ${userAgent}
                        </small>
                    </div>

                    <div class="security-log-meta">
                        <span>${dateFormatee}</span>
                        <span>${ip}</span>
                    </div>
                </div>
            `;
        }).join("");

    } catch (error) {
        console.error(
            "Erreur chargement journal de sécurité :",
            error
        );

        container.innerHTML = `
            <div class="security-empty">
                Impossible de charger le journal de sécurité.
            </div>
        `;
    }
};


// Chargement du journal lorsque le panneau Sécurité
// est rendu dans le DOM.
(function () {
    let journalCharge = false;

    const chargerSiDisponible = () => {
        const container = document.getElementById(
            "cf-security-log-container"
        );

        if (!container || journalCharge) {
            return;
        }

        journalCharge = true;

        if (
            typeof window.complianceForgeLoadSecurityLog
            === "function"
        ) {
            window.complianceForgeLoadSecurityLog();
        }

        observer.disconnect();
    };

    const observer = new MutationObserver(
        chargerSiDisponible
    );

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    chargerSiDisponible();
})();



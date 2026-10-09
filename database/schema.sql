--
-- PostgreSQL database dump
--


-- Dumped from database version 16.15 (Debian 16.15-1.pgdg13+2)
-- Dumped by pg_dump version 16.15 (Debian 16.15-1.pgdg13+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: roleutilisateur; Type: TYPE; Schema: public; Owner: -
--

CREATE TYPE public.roleutilisateur AS ENUM (
    'dpo',
    'metier',
    'direction',
    'admin'
);


--
-- Name: statutincident; Type: TYPE; Schema: public; Owner: -
--

CREATE TYPE public.statutincident AS ENUM (
    'nouveau',
    'analyse',
    'notification_preparee',
    'notifie',
    'cloture'
);


--
-- Name: statuttraitement; Type: TYPE; Schema: public; Owner: -
--

CREATE TYPE public.statuttraitement AS ENUM (
    'brouillon',
    'actif',
    'archive'
);


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- Name: categories_donnees; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.categories_donnees (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    categorie character varying NOT NULL,
    sensible boolean
);


--
-- Name: documents_generes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.documents_generes (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    type_document character varying NOT NULL,
    chemin_fichier character varying NOT NULL,
    nom_fichier character varying NOT NULL,
    hash_integrite character varying NOT NULL,
    template_version character varying NOT NULL,
    date_generation timestamp without time zone
);


--
-- Name: droits_personnes_apdp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.droits_personnes_apdp (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    droit_acces text,
    droit_portabilite text,
    droit_opposition_retrait_consentement text,
    droit_interrogation text,
    droit_rectification_suppression text,
    droit_oubli_numerique text,
    modalites_exercice text,
    responsable_exercice text,
    delai_exercice text
);


--
-- Name: incidents; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.incidents (
    id uuid NOT NULL,
    organisation_id uuid NOT NULL,
    traitement_id uuid,
    sexe_declarant character varying,
    nom_famille character varying,
    prenoms character varying,
    adresse text,
    quartier_lieu_dit character varying,
    arrondissement character varying,
    commune character varying,
    pays character varying,
    telephone_portable character varying,
    boite_postale character varying,
    adresse_electronique character varying,
    types_violation json NOT NULL,
    violation_autre text,
    auteur_presume_nom text,
    auteur_presume_ville character varying,
    auteur_presume_pays character varying,
    auteur_presume_contact character varying,
    date_heure_violation timestamp without time zone,
    date_heure_constatation timestamp without time zone NOT NULL,
    lieu_violation text,
    resume_incident text,
    donnees_personnelles_concernees text,
    consequences_potentielles json NOT NULL,
    observations_techniques text,
    pieces json NOT NULL,
    statut public.statutincident NOT NULL,
    echeance_notification timestamp without time zone NOT NULL,
    date_notification timestamp without time zone,
    notification_dans_les_delais boolean,
    date_creation timestamp without time zone,
    derniere_revision timestamp without time zone
);


--
-- Name: journal_securite; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.journal_securite (
    id uuid NOT NULL,
    utilisateur_id uuid,
    evenement character varying NOT NULL,
    description text NOT NULL,
    adresse_ip character varying,
    user_agent text,
    date_evenement timestamp without time zone NOT NULL
);


--
-- Name: organisations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.organisations (
    id uuid NOT NULL,
    nom character varying NOT NULL,
    secteur_activite character varying,
    ifu_rccm character varying,
    adresse character varying,
    contact_dpo_email character varying,
    date_creation timestamp without time zone
);


--
-- Name: principes_apdp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.principes_apdp (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    "licéite_consentement" boolean,
    "licéite_contrat" boolean,
    "licéite_obligation_legale" boolean,
    "licéite_interet_legitime" boolean,
    "licéite_interet_public" boolean,
    "licéite_interets_vitaux" boolean,
    "licéite_exceptions" text,
    information_prealable boolean,
    information_exceptions text,
    information_modalites text,
    information_contenu text,
    information_preuve text,
    consentement_mode text,
    consentement_finalites text,
    consentement_duree text,
    pertinence_utilite text,
    pertinence_quantite text,
    pertinence_adequation text
);


--
-- Name: profils_responsables_apdp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.profils_responsables_apdp (
    id uuid NOT NULL,
    organisation_id uuid NOT NULL,
    nom_prenoms_raison_sociale text,
    npi_rccm character varying,
    carre_lot character varying,
    quartier character varying,
    ville character varying,
    adresse_postale text,
    adresse_electronique character varying,
    contact_telephonique character varying,
    autres_contacts text,
    activite text,
    secteur_activite character varying,
    representant_legal_nom_prenoms text,
    representant_legal_npi character varying,
    representant_legal_adresse text,
    representant_legal_contacts text
);


--
-- Name: scores_conformite; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scores_conformite (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    score_global double precision NOT NULL,
    version_grille character varying NOT NULL,
    details json NOT NULL,
    date_calcul timestamp without time zone
);


--
-- Name: scores_risque; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scores_risque (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    score_global double precision NOT NULL,
    niveau character varying NOT NULL,
    composantes json NOT NULL,
    date_calcul timestamp without time zone
);


--
-- Name: securites_apdp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.securites_apdp (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    personnes_autorisees text,
    protection_intervention_non_autorisee text,
    politique_acces_physique text,
    mesures_physiques text,
    mesures_electroniques text,
    autres_mesures text,
    protection_incendie text,
    protection_inondation text,
    protection_surtensions text,
    protection_phenomenes_magnetiques text,
    mesures_organisationnelles text,
    mesures_logiques text,
    tests text,
    certifications text,
    verification_identite text,
    journalisation text,
    authentification_multifacteur text,
    chiffrement text,
    sensibilisation_personnel text,
    mesures_juridiques text,
    confidentialite text,
    integrite text,
    disponibilite text,
    sauvegardes text,
    continuite_energie text,
    architecture_reseau text
);


--
-- Name: traitements; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.traitements (
    id uuid NOT NULL,
    organisation_id uuid NOT NULL,
    nom character varying NOT NULL,
    service_responsable character varying,
    statut public.statuttraitement,
    finalite text,
    base_legale character varying,
    justification_base_legale text,
    responsable_id uuid,
    dpo_id uuid,
    reference_apdp_anterieure character varying,
    date_mise_en_oeuvre timestamp without time zone,
    date_creation timestamp without time zone,
    derniere_revision timestamp without time zone,
    sensibilite_donnees integer,
    niveau_mesures_securite integer,
    sous_traitance_transferts integer,
    exposition integer,
    volume integer
);


--
-- Name: traitements_anterieurs_apdp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.traitements_anterieurs_apdp (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    enregistrement_apdp_anterieur text,
    reference_apdp_anterieure character varying,
    registre_activites_a_jour text,
    dpo_designe text,
    representant_legal_declaration text,
    declaration_sur_honneur text
);


--
-- Name: traitements_apdp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.traitements_apdp (
    id uuid NOT NULL,
    traitement_id uuid NOT NULL,
    donnees_personnelles text,
    origine_donnees text,
    personnes_salaries boolean,
    personnes_adherents boolean,
    personnes_usagers boolean,
    personnes_visiteurs boolean,
    personnes_patients boolean,
    personnes_clients boolean,
    personnes_eleves_etudiants boolean,
    personnes_autres text,
    nombre_personnes integer,
    operation_collecte boolean,
    operation_developpement boolean,
    operation_exposition_affichage boolean,
    operation_conservation boolean,
    operation_copie boolean,
    operation_traitement_image boolean,
    operation_exploitation boolean,
    operation_enregistrement boolean,
    operation_adaptation boolean,
    operation_modification boolean,
    operation_extraction boolean,
    operation_sauvegarde boolean,
    operation_consultation boolean,
    operation_utilisation boolean,
    operation_communication_transmission_diffusion boolean,
    operation_structuration_rapprochement_interconnexion boolean,
    operation_limitation boolean,
    operation_cryptage boolean,
    operation_effacement boolean,
    operation_destruction boolean,
    operation_organisation boolean,
    operation_autre text,
    type_video_photo boolean,
    type_site_web_application boolean,
    type_biometrique boolean,
    procedure_manuelle boolean,
    procedure_automatisee boolean,
    caracteristiques_techniques text,
    fonctionnalites text,
    duree_conservation text,
    texte_legal_reglementaire_conservation text,
    support_papier boolean,
    support_numerique boolean,
    autre_support text,
    lieu_stockage text,
    modalites_stockage text,
    responsable_stockage text,
    stockage_systeme_ordinaire boolean,
    stockage_cloud boolean,
    stockage_local_nas boolean,
    stockage_lvm boolean,
    sous_traitance_oui_non boolean,
    sous_traitance_annexe text,
    communication_oui_non boolean,
    communication_benin_cedeao text,
    communication_annexe text,
    interconnexion_oui_non boolean,
    interconnexion_annexe text,
    transfert_oui_non boolean,
    transfert_pays_tiers text,
    transfert_autorisation_annexe text
);


--
-- Name: utilisateurs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.utilisateurs (
    id uuid NOT NULL,
    organisation_id uuid,
    nom character varying NOT NULL,
    email character varying NOT NULL,
    fonction character varying,
    role public.roleutilisateur NOT NULL,
    mot_de_passe_hash character varying NOT NULL,
    date_creation timestamp without time zone,
    prenoms character varying,
    email_verifie boolean NOT NULL,
    token_verification_hash character varying,
    token_verification_expire_at timestamp without time zone,
    token_reset_hash character varying,
    token_reset_expire_at timestamp without time zone
);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories_donnees categories_donnees_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categories_donnees
    ADD CONSTRAINT categories_donnees_pkey PRIMARY KEY (id);


--
-- Name: documents_generes documents_generes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.documents_generes
    ADD CONSTRAINT documents_generes_pkey PRIMARY KEY (id);


--
-- Name: droits_personnes_apdp droits_personnes_apdp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.droits_personnes_apdp
    ADD CONSTRAINT droits_personnes_apdp_pkey PRIMARY KEY (id);


--
-- Name: droits_personnes_apdp droits_personnes_apdp_traitement_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.droits_personnes_apdp
    ADD CONSTRAINT droits_personnes_apdp_traitement_id_key UNIQUE (traitement_id);


--
-- Name: incidents incidents_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.incidents
    ADD CONSTRAINT incidents_pkey PRIMARY KEY (id);


--
-- Name: journal_securite journal_securite_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.journal_securite
    ADD CONSTRAINT journal_securite_pkey PRIMARY KEY (id);


--
-- Name: organisations organisations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.organisations
    ADD CONSTRAINT organisations_pkey PRIMARY KEY (id);


--
-- Name: principes_apdp principes_apdp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.principes_apdp
    ADD CONSTRAINT principes_apdp_pkey PRIMARY KEY (id);


--
-- Name: principes_apdp principes_apdp_traitement_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.principes_apdp
    ADD CONSTRAINT principes_apdp_traitement_id_key UNIQUE (traitement_id);


--
-- Name: profils_responsables_apdp profils_responsables_apdp_organisation_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profils_responsables_apdp
    ADD CONSTRAINT profils_responsables_apdp_organisation_id_key UNIQUE (organisation_id);


--
-- Name: profils_responsables_apdp profils_responsables_apdp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profils_responsables_apdp
    ADD CONSTRAINT profils_responsables_apdp_pkey PRIMARY KEY (id);


--
-- Name: scores_conformite scores_conformite_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scores_conformite
    ADD CONSTRAINT scores_conformite_pkey PRIMARY KEY (id);


--
-- Name: scores_risque scores_risque_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scores_risque
    ADD CONSTRAINT scores_risque_pkey PRIMARY KEY (id);


--
-- Name: securites_apdp securites_apdp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.securites_apdp
    ADD CONSTRAINT securites_apdp_pkey PRIMARY KEY (id);


--
-- Name: securites_apdp securites_apdp_traitement_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.securites_apdp
    ADD CONSTRAINT securites_apdp_traitement_id_key UNIQUE (traitement_id);


--
-- Name: traitements_anterieurs_apdp traitements_anterieurs_apdp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements_anterieurs_apdp
    ADD CONSTRAINT traitements_anterieurs_apdp_pkey PRIMARY KEY (id);


--
-- Name: traitements_anterieurs_apdp traitements_anterieurs_apdp_traitement_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements_anterieurs_apdp
    ADD CONSTRAINT traitements_anterieurs_apdp_traitement_id_key UNIQUE (traitement_id);


--
-- Name: traitements_apdp traitements_apdp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements_apdp
    ADD CONSTRAINT traitements_apdp_pkey PRIMARY KEY (id);


--
-- Name: traitements_apdp traitements_apdp_traitement_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements_apdp
    ADD CONSTRAINT traitements_apdp_traitement_id_key UNIQUE (traitement_id);


--
-- Name: traitements traitements_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements
    ADD CONSTRAINT traitements_pkey PRIMARY KEY (id);


--
-- Name: utilisateurs utilisateurs_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilisateurs
    ADD CONSTRAINT utilisateurs_email_key UNIQUE (email);


--
-- Name: utilisateurs utilisateurs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilisateurs
    ADD CONSTRAINT utilisateurs_pkey PRIMARY KEY (id);


--
-- Name: categories_donnees categories_donnees_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categories_donnees
    ADD CONSTRAINT categories_donnees_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: documents_generes documents_generes_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.documents_generes
    ADD CONSTRAINT documents_generes_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: droits_personnes_apdp droits_personnes_apdp_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.droits_personnes_apdp
    ADD CONSTRAINT droits_personnes_apdp_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: incidents incidents_organisation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.incidents
    ADD CONSTRAINT incidents_organisation_id_fkey FOREIGN KEY (organisation_id) REFERENCES public.organisations(id);


--
-- Name: incidents incidents_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.incidents
    ADD CONSTRAINT incidents_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: journal_securite journal_securite_utilisateur_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.journal_securite
    ADD CONSTRAINT journal_securite_utilisateur_id_fkey FOREIGN KEY (utilisateur_id) REFERENCES public.utilisateurs(id);


--
-- Name: principes_apdp principes_apdp_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.principes_apdp
    ADD CONSTRAINT principes_apdp_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: profils_responsables_apdp profils_responsables_apdp_organisation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.profils_responsables_apdp
    ADD CONSTRAINT profils_responsables_apdp_organisation_id_fkey FOREIGN KEY (organisation_id) REFERENCES public.organisations(id);


--
-- Name: scores_conformite scores_conformite_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scores_conformite
    ADD CONSTRAINT scores_conformite_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: scores_risque scores_risque_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scores_risque
    ADD CONSTRAINT scores_risque_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: securites_apdp securites_apdp_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.securites_apdp
    ADD CONSTRAINT securites_apdp_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: traitements_anterieurs_apdp traitements_anterieurs_apdp_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements_anterieurs_apdp
    ADD CONSTRAINT traitements_anterieurs_apdp_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: traitements_apdp traitements_apdp_traitement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements_apdp
    ADD CONSTRAINT traitements_apdp_traitement_id_fkey FOREIGN KEY (traitement_id) REFERENCES public.traitements(id);


--
-- Name: traitements traitements_dpo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements
    ADD CONSTRAINT traitements_dpo_id_fkey FOREIGN KEY (dpo_id) REFERENCES public.utilisateurs(id);


--
-- Name: traitements traitements_organisation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements
    ADD CONSTRAINT traitements_organisation_id_fkey FOREIGN KEY (organisation_id) REFERENCES public.organisations(id);


--
-- Name: traitements traitements_responsable_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.traitements
    ADD CONSTRAINT traitements_responsable_id_fkey FOREIGN KEY (responsable_id) REFERENCES public.utilisateurs(id);


--
-- Name: utilisateurs utilisateurs_organisation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilisateurs
    ADD CONSTRAINT utilisateurs_organisation_id_fkey FOREIGN KEY (organisation_id) REFERENCES public.organisations(id);


--
-- PostgreSQL database dump complete
--



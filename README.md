# Python Automation Boilerplate (Dockerized)

Ce projet est une base professionnelle et robuste pour le développement de bots, scripts d'automatisation et pipelines ETL.
Il est conçu pour être **sécurisé**, **portable** (via Docker) et **facilement observable** (Logs standardisés).

## Fonctionnalités Clés

* 100% Dockerisé : Fonctionne de manière identique en local, sur un VPS ou sur le Cloud (GCP/AWS).
* Sécurité native : Gestion des secrets (API Keys, Mots de passe) via variables d'environnement (`.env`), jamais hardcodés.
* Logging Professionnel : Système de logs horodatés et hiérarchisés (INFO, ERROR) pour le monitoring.
* Gestion d'erreurs : Structure `try/catch` globale pour éviter les crashs silencieux et permettre l'alerting.
* Architecture Modulaire : Séparation claire entre le lanceur (`main.py`) et la logique métier (`logic.py`).

##Stack Technique

* **Python 3.9 Slim** (Image légère)
* **Docker** (Conteneurisation)
* **Python-dotenv** (Configuration)
* **Requests / Pandas** (Traitement de données -- *selon besoins*)

## Structure du Projet

```bash
mon-bot-template/
├── Dockerfile           # Configuration de l'image Docker
├── requirements.txt     # Dépendances Python
├── .env                 # Variables secrètes (Non commité sur Git)
├── .dockerignore        # Exclusion des fichiers sensibles de l'image
└── src/
    ├── main.py          # Point d'entrée, gestion des erreurs et configs
    └── logic.py         # Logique métier (Scraping, ETL, API calls...)


1. Prérequis

Docker installé sur la machine.

2. Configuration des secrets

Créez un fichier .env à la racine du projet et ajoutez vos variables :

Ini, TOML
ENV_TYPE=Production
API_KEY=votre_cle_secrete_ici

3. Build & Run (Via Docker)

Étape 1 : Construire l'image

Bash
docker build -t mon-bot-auto .
Étape 2 : Lancer le bot Le flag --env-file injecte vos secrets de manière sécurisée au moment du lancement.

Bash
docker run --env-file .env mon-bot-auto

Personnalisation
Toute la logique métier se trouve dans src/logic.py. Pour adapter ce bot à un nouveau besoin (ex: Scraper un site immo, Appel API Finance) :

Modifiez la fonction executer_tache() dans src/logic.py.

Ajoutez les nouvelles librairies nécessaires dans requirements.txt.

Re-buildez l'image.

Auteur : Théo Vassal - Data Engineer Projet réalisé dans le cadre d'un portfolio d'automatisation professionnelle.
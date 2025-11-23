


import os
from dotenv import load_dotenv
import logging
from logic import executer_tache

load_dotenv()
#config des logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info('Démarrage du bot')

    try:
        api_key=os.getenv('API_KEY')
        env_type=os.getenv("ENV_TYPE","Prod")
        logging.info(f"Env : {env_type}")
        if not api_key:
            raise ValueError('Clé API manquante dans le .env')
            #Lancement logique métier
        logging.info("traitement en cours...")
        resultat= executer_tache()

        logging.info(f'Succès : {resultat}')
    except Exception as e:
        #gestion des erreurs (pour que le script ne meure pas en silence)
        logging.error(f"Erreur critique:{e}")

if __name__=="__main__":
    main()
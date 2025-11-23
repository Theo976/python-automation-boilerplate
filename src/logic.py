import time
import random

def executer_tache():
    """
    logique métier(scraping API call,ETL
    """

    print("[Logic] Connexion à la source de données...")
    time.sleep(1)

    print("Logic] Taitement des données en cours...")
    time.sleep(1)

    #simulation de résultat aléatoire
    lignes_traitees=random.randint(100,1000)
    return f"{lignes_traitees} lignes ont été importées et nettoyées"
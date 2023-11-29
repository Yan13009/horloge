import time


def afficher_heure(heure):
    print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")


def regler_heure(heure, heures, minutes, secondes):
    heure = (heures, minutes, secondes)
    return heure


def regler_alarme(alarme, heures, minutes, secondes):
    alarme = (heures, minutes, secondes)
    return alarme


def verifier_alarme(heure, alarme):
    if heure == alarme:
        print("Réveillez-vous ! L'alarme sonne !")


heure_actuelle = (0, 0, 0)


alarme = None


while True:
    
    afficher_heure(heure_actuelle)

    
    if alarme is not None:
        verifier_alarme(heure_actuelle, alarme)

    
    time.sleep(1)

    
    heure_actuelle = regler_heure(heure_actuelle, *time.localtime()[3:6])

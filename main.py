import time

# Fonction pour afficher l'heure et gérer une alarme
def afficher_heure(heure, heure_alarme, format_12h=True):
    while True:
         # Incrémente les secondes
        heure[2] += 1
        if heure[2] >= 60:
            heure[1] += 1
            heure[2] = 0
            # Gestion des minutes
        if heure[1] >= 60:
            heure[0] += 1
            heure[1] = 0
            # Si l'heure dépasse 23, revenir à 00
        if heure[0] >= 24:
            heure[0] = 0

             # Formatage de l'heure en 12h ou 24h
        if format_12h:
           heure_str = f"{(heure[0] % 12) or 12}:{heure[1]:02d}:{heure[2]:02d} {'AM' if heure[0] < 12 else 'PM'}"
        else:
             heure_str = f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}"

        print(heure_str)

          # Vérifie si l'heure correspond à l'heure de l'alarme
        if heure == heure_alarme:
            print("Alarme!")

        time.sleep(1)

# Fonction pour choisir le format de l'heure
def choisir_format():
    choix = input("Voulez-vous afficher l'heure en format 12H ? (oui/non): ")
    return choix.startswith("oui")

# Heure de l'alarme et heure initiale
heure_alarme = [16, 30, 5]
heure = [16, 30, 00]

format_24h = choisir_format()

# Appel de la fonction pour afficher l'heure avec l'alarme
afficher_heure(heure, heure_alarme, format_24h)
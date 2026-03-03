import math
print("=" * 60)
print("MODULE MATH")
print("=" * 60)
print(f"Pi: {math.pi}")
print(f"e: {math.e}")
print(f"Racine carrée de 144: {math.sqrt(144)}")
print(f"Plafond de 3.2: {math.ceil(3.2)}")
print(f"Plancher de 3.8: {math.floor(3.8)}")
print(f"Valeur absolue de -5: {math.fabs(-5)}")

# MODULE RANDOM : Nombres aléatoires
import random
print("\n" + "=" * 60)
print("MODULE RANDOM")
print("=" * 60)
print(f"Nombre aléatoire entre 0 et 1: {random.random()}")
print(f"Nombre aléatoire entre 1 et 10: {random.randint(1, 10)}")
print(f"Nombre aléatoire entre 1 et 100: {random.randint(1, 100)}")

# Choisir un élément aléatoire
couleurs = ["rouge", "vert", "bleu", "jaune"]
print(f"Couleur aléatoire: {random.choice(couleurs)}")

# Mélanger une liste
nombres = [1, 2, 3, 4, 5]
random.shuffle(nombres)
print(f"Liste mélangée: {nombres}")

# MODULE DATETIME : Dates et heures
import datetime
print("\n" + "=" * 60)
print("MODULE DATETIME")
print("=" * 60)
maintenant = datetime.datetime.now()
print(f"Date et heure actuelles: {maintenant}")
print(f"Année: {maintenant.year}")
print(f"Mois: {maintenant.month}")
print(f"Jour: {maintenant.day}")
print(f"Heure: {maintenant.hour}")
print(f"Minute: {maintenant.minute}")

# Créer une date spécifique
noel = datetime.datetime(2024, 12, 25)
print(f"\nNoël 2024: {noel}")

# Calculer la différence
difference = noel - maintenant
print(f"Jours jusqu'à Noël: {difference.days}")

# MODULE OS : Système d'exploitation
import os
print("\n" + "=" * 60)
print("MODULE OS")
print("=" * 60)
print(f"Répertoire actuel: {os.getcwd()}")
print(f"Système d'exploitation: {os.name}")

# Lister les fichiers
fichiers = os.listdir(".")
print(f"Fichiers dans le répertoire actuel:")
for fichier in fichiers[:5]:  # Afficher 5 premiers
    print(f"  - {fichier}")

# MODULE STRING : Constantes de chaînes
import string
print("\n" + "=" * 60)
print("MODULE STRING")
print("=" * 60)
print(f"Lettres minuscules: {string.ascii_lowercase}")
print(f"Lettres majuscules: {string.ascii_uppercase}")
print(f"Chiffres: {string.digits}")
print(f"Ponctuation: {string.punctuation}")

# MODULE TIME : Temps
import time
print("\n" + "=" * 60)
print("MODULE TIME")
print("=" * 60)
print("Compte à rebours de 3 secondes:")
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)  # Pause de 1 seconde
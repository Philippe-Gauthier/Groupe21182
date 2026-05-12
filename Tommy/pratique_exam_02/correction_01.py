"""
Code présenté par Tommy Brunelle
date:
"""
import caracteres as car

texte = open("texte.txt", "r")
validation = texte.read()
texte.close()

resultat = ""
erreurs = 0

# Parcourir chaque caractère. Chaque lettre, espace, caractere (Cest pas dans une liste avec read()).
for caractere in validation:
    if caractere.lower() in car.caracteres_autorises: # Si on enleve le .lower() les majuscules ne sont plus prises en compte.
        resultat += caractere
    else:
        resultat += "*"

for caractere in resultat:
    if caractere == "*":
        erreurs += 1

# Afficher le résultat.
print(resultat)
print(f"{erreurs} caractères non autorisés.")

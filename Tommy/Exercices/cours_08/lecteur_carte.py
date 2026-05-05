
fichier = open("carte_hex_02.csv", "r") #r pour lecture
liste_fichier = fichier.readlines()

liste_dictionnaire = []
for ligne in liste_fichier:
    ligne = ligne.strip()
    liste_element = ligne.split(",")
    dictionnaire = {
        "x": liste_element[0],
        "y": liste_element[1],
        "terrain": liste_element[2],
    }
    liste_dictionnaire.append(dictionnaire)

for i in liste_dictionnaire:
    print(f"Lheaxgone aux coordonnees ({i['x']}, {i['y']}) est de type {i['terrain']}")

fichier.close
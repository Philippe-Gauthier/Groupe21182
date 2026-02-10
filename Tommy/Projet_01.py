"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
page_01 = "Texte intro"
choix_01 = "1"
choix_02 = "2"
choix_03 = "3"

def choisir_deux_options(choix1, choix2):
    print("----------------------------------------------")
    print(f"1: {choix_01}")
    print(f"2: {choix_02}")
    decision = int(input("Que choisis-tu de faire?"))
    return decision

def choisir_trois_options(choix1, choix2, choix3):
    print("----------------------------------------------")
    print(f"1: {choix_01}")
    print(f"2: {choix_02}")
    print(f"3: {choix_03}")
    decision = int(input("Que choisis-tu de faire?"))
    return decision

print(f"{page_01}")
choisir_deux_options(choix_01, choix_02)
"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
page_01 = "Texte intro"
page_02 = "test if"
page_03 = "test if_02"
choix_01 = int("1")
choix_02 = int("2")
choix_03 = int("3")
choix_04 = int("4")
choix_05 = int("5")
choix_06 = int("6")

def choisir_deux_options(choix1, choix2):
    print("----------------------------------------------")
    print(f"1: {choix1}")
    print(f"2: {choix2}")
    decision = int(input("Que choisis-tu de faire?: "))
    return decision

def choisir_trois_options(choix1, choix2, choix3):
    print("----------------------------------------------")
    print(f"1: {choix1}")
    print(f"2: {choix2}")
    print(f"3: {choix3}")
    decision = int(input("Que choisis-tu de faire?: "))
    return decision

print(f"{page_01}")
choix = choisir_deux_options(choix_01, choix_02)

if choix == choix_02:
    print(f"{page_02}")
    choisir_deux_options(choix_03, choix_04)

else:
    print(f"{page_03}")
    choisir_deux_options(choix_05, choix_06)


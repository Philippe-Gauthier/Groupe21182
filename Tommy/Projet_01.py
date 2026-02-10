"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
page_01 = "Texte intro"
page_02 = "test if"
page_03 = "test else"
choix_01 = 1
choix_02 = 2
choix_03 = 3
choix_04 = 4
choix_05 = 5
choix_06 = 6


def choisir_deux_options(choix1, choix2):
    
    """
    Entrées: Deux choix (texte)
    Sortie: Option choisie (int)
    But: demander à l'utilisateur de choisir une option

    """
    print("----------------------------------------------")
    print(f"1: {choix1}")
    print(f"2: {choix2}")
    print("   ")
    decision = int(input("Que choisis-tu de faire?: "))
    return decision

def choisir_trois_options(choix1, choix2, choix3):
      
    """
    Entrées: Trois choix (texte)
    Sortie: Option choisie (int)
    But: demander à l'utilisateur de choisir une option

    """
    print("----------------------------------------------")
    print(f"1: {choix1}")
    print(f"2: {choix2}")
    print(f"3: {choix3}")
    print("   ")
    decision = int(input("Que choisis-tu de faire?: "))
    return decision

print("   ")
print(page_01)
choix = choisir_deux_options(choix_01, choix_02)

if choix == choix_02:
    print("   ")
    print(page_02)
    choisir_deux_options(choix_03, choix_04)

else:
    print("   ")
    print(page_03)
    choisir_deux_options(choix_05, choix_06)


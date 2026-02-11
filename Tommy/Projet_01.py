"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
page_01 = "C'est le grand jour, tes mensonges ont porté fruit.\nTu commences ton premier quart de travail en tant que chef cuisinier dans 1h.\nTu es remplis de remords face aux mensonges liés à cette embauche, mais il faut ce qu'il faut pour arriver hein?\nTu dois te préparer à partir, mais tu es terriblement stressé.\n\nQue fais tu?"
page_02 = "test if"
page_03 = "test else"
choix_01 = "AAAA"
choix_02 = "BBBB"
choix_03 = "CCCC"
choix_04 = "DDDD"
choix_05 = "EEEE"
choix_06 = "FFFF"
choix_07 = "GGGG"
choix_08 = "HHHH"


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
decision_01 = choisir_deux_options(choix_01, choix_02)

if decision_01 == 2:
    print("   ")
    print(page_02)
    choisir_deux_options(choix_03, choix_04)

else:
    print("   ")
    print(page_03)
    choisir_deux_options(choix_05, choix_06)



"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
intro = "C'est le grand jour, tes mensonges ont porté fruit.\nTu commences ton premier quart de travail en tant que chef cuisinier dans 1h.\nTu es remplis de remords face aux mensonges liés à cette embauche, mais il faut ce qu'il faut pour arriver hein?\nTu dois te préparer à partir, mais tu es terriblement stressé.\n\nQue fais tu?"
page_02 = "histoire_02"
page_03 = "histoire_03"
choix_respir = "Tu prends un bon grand respir et te dirige au travail, ça va passer."
choix_shooter = "Tu décides de prendre 2-3 shooters pour la confiance, il est midi quelque part comme on dit"
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
    while True: 

     print("----------------------------------------------")
     print(f"1: {choix1}")
     print(f"2: {choix2}")
     print("   ")
     decision = int(input("Que choisis-tu de faire?: "))

     if decision == 1:
         return decision
     elif decision == 2:
         return decision
     else:
         print("J'aime ton énergie, mais il faudrait choisir une des options proposées.")
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
print(intro)
decision_01 = choisir_deux_options(choix_respir, choix_shooter)

if decision_01 == 2:
    print("   ")
    print(page_02)
    choisir_deux_options(choix_03, choix_04)

if decision_01 == 1:
    print("   ")
    print(page_03)
    choisir_deux_options(choix_05, choix_06)


    



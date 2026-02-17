"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
intro = "C'est le grand jour, tes mensonges ont porté fruit.\nTu commences ton premier quart de travail en tant que chef cuisinier dans 1h.\nTu es remplis de remords face aux mensonges liés à cette embauche, mais il faut ce qu'il faut pour arriver hein?\nTu dois te préparer à partir, mais tu es terriblement stressé.\n\nQue fais tu?"
page_02 = "Tu arrives en cuisine et tout semble normal, personne ne mentionne l'odeur d'alcool. Le chef arrive et te salue. «On est dans le rush déjà en préparation, va blanchir des patates.»"
page_03 = "histoire_03"
page_04 = "histoire_04"
page_05 = "histoire_05"
page_06 = "histoire_06"
choix_intro_01 = "Tu prends un bon grand respir et te dirige au travail, ça va passer."
choix_intro_02 = "Tu décides de prendre 2-3 shooters pour la confiance, il est midi quelque part comme on dit"
choix_02_01 = "Tu décides d'aller remplir une chaudière d'eau bouillante salée et une chaudière d'eau glacée pour les patates."
choix_02_02 = "Tu restes immobile, paniqué. Tu vois un cuisinier au loin qui te fait signe d'approcher. Tu te rends vers lui."
choix_02_03 = "Tu fouilles partout à la recherche de peinture blanche."



def choisir_deux_options(choix1, choix2):
    
    """
    Entrées: Deux choix (texte)
    Sortie: Option choisie (texte interprete en int)
    But: demander à l'utilisateur de choisir une option

    """
    while True: 

     print("----------------------------------------------")
     print(f"1: {choix1}")
     print(f"2: {choix2}")
     print("   ")
     decision = (input("Que choisis-tu de faire?: "))

     if decision == "1":
         return int(decision)
     elif decision == "2":
         return int(decision)
     else:
         print("   ")
         print("J'aime ton énergie, mais il faudrait choisir une des options proposées.")
        
       
         


def choisir_trois_options(choix1, choix2, choix3):
      
    """
    Entrées: Trois choix (texte)
    Sortie: Option choisie (int)
    But: demander à l'utilisateur de choisir une option

    """
    while True: 

     print("----------------------------------------------")
     print(f"1: {choix1}")
     print(f"2: {choix2}")
     print(f"3: {choix3}")
     print("   ")
     decision = (input("Que choisis-tu de faire?: "))

     if decision == "1":
         return int(decision)
     elif decision == "2":
         return int(decision)
     elif decision == "3":
         return int(decision)
     else:
         print("   ")
         print("J'aime ton énergie, mais il faudrait choisir une des options proposées.")



print("   ")
print(intro)
decision_01 = choisir_deux_options(choix_intro_01, choix_intro_02)

if decision_01 == 2:
    print("   ")
    print(page_02)
    decision_02 = choisir_trois_options(choix_03, choix_04, choix_05)

if decision_01 == 1:
    print("   ")
    print(page_03)

if decision_02 == 1:
    print("   ")
    print(page_04)

if decision_02 == 2:
    print("   ")
    print(page_05)

if decision_02 == 3:
    print("   ")
    print(page_06)

    



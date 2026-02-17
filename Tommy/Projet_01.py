"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
intro = "C'est le grand jour, tes mensonges ont porté fruit.\nTu commences ton premier quart de travail en tant que chef cuisinier dans 1h.\nTu es remplis de remords face aux mensonges liés à cette embauche, mais il faut ce qu'il faut pour arriver hein?\nTu dois te préparer à partir, mais tu es terriblement stressé.\n\nQue fais tu?"
page_02 = "Tu arrives en cuisine et tout semble normal, personne ne mentionne l'odeur d'alcool. Le chef arrive et te salue. «On est dans le rush déjà en préparation, va blanchir des patates.»\n\n Que choisis-tu de faire?"
page_03 = "Une fois arrivé, le chef te dévisage instantanémment. Il te reniffle. «T'es clairement ajeun...T'es pas un vrai cook!» Il te crie dessus et te force à quitter les lieux.\n\n Game Over"
page_04 = "Il te faut des chaudières, tu cherches un peu et entre dans une chambre froide où il y a plein plein plein de chaudières.\n\nQue prends-tu? "
page_05 = "Le cuisinier te sourit. «Oublie les patates big, Marco s'en occupe. Aide moi à couper des légumes pour ce soir.»"
page_06 = "Le chef te voit se promener avec une cannette de peinture blanche, se fâche et te renvoi sur le champ.\n\nGame Over"
page_07 = ""
page_08 = ""
page_09 = ""
page_10 = ""
page_11 = ""
page_12 = ""
page_13 = ""
page_14 = ""
page_15 = ""
page_16 = ""
page_17 = ""
page_18 = ""

choix_intro_01 = "Tu prends un bon grand respir et te dirige au travail, ça va passer."
choix_intro_02 = "Tu décides de prendre 2-3 shooters pour la confiance, il est midi quelque part comme on dit"
choix_02_01 = "Tu décides d'aller remplir une chaudière d'eau bouillante salée et une chaudière d'eau glacée pour les patates."
choix_02_02 = "Tu restes immobile, paniqué. Tu vois un cuisinier au loin qui te fait signe d'approcher. Tu te rends vers lui."
choix_02_03 = "Tu fouilles partout à la recherche de peinture blanche."
choix_04_01 = "Tu vois deux chaudières remplies d'eau. Tu décides de sauver du temps pour mieux paraître. Tu pars avec."
choix_04_02 = "Tu prends les deux chaudières vides du bord et retourne en cuisine."
choix_05_01 = "Tu décides d'aiguiser ton couteau avant de couper quoi que ce soit."
choix_05_02 = "Tu prends un couteau et fixe la carotte devant toi."
choix_05_03 = "Tu lui avoue ne rien savoir et que tu as besoin d'aide pour ne pas que ça paraisse."
choix_08_01 = ""
choix_08_02 = ""
choix_10_01 = ""
choix_10_02 = ""
choix_11_01 = ""
choix_11_02 = ""


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
decision_intro = choisir_deux_options(choix_intro_01, choix_intro_02)

if decision_intro == 2:
    print("   ")
    print(page_02)
    decision_02 = choisir_trois_options(choix_02_01, choix_02_02, choix_02_03)

    if decision_02 == 1:
        print("   ")
        print(page_04)
        decision_04 = choisir_deux_options(choix_04_01, choix_04_02)

        if decision_04 == 1:
            print("   ")
            print(page_07)

        elif decision_04 == 2:
            print("   ")
            print(page_08)

    elif decision_02 == 2:
        print("   ")
        print(page_05)
        decision_05 = choisir_trois_options(choix_05_01, choix_05_02, choix_05_03)

        if decision_05 == 1:
            print("   ")
            print(page_09)

        elif decision_05 == 2:
            print("   ")
            print(page_10)

        elif decision_05 == 3:
            print("   ")
            print(page_11)

    elif decision_02 == 3:
        print("   ")
        print(page_06)

elif decision_intro == 1:
    print("   ")
    print(page_03)



    



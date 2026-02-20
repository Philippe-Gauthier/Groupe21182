"""
Tommy Brunelle
Fichier principal du projet de livre interactif

"""
# Pour intéragir avec le système d'exploitation Windows
import subprocess

# Pages du livre/Mises en situation.
page_01 = "\n\nC'est le grand jour. Tes mensonges ont porté fruit.\nTu commences ton premier quart de travail en tant que chef cuisinier dans 1h.\nTu es remplis de remords face aux mensonges liés à cette embauche, mais il faut ce qu'il faut pour arriver hein?\nTu dois te préparer à partir, mais tu es terriblement stressé."
page_02 = "\nTu arrives en cuisine et tout semble normal. Personne ne mentionne l'odeur d'alcool.\nLe chef arrive et te salue. «On est dans le rush déjà pour la préparation, va blanchir des patates.»"
page_03 = "\nUne fois arrivé, le chef te dévisage instantanémment. Il te reniffle. «T'es clairement ajeun...T'es pas un vrai cook!»\nIl te crie après et t'obliges à quitter les lieux.\n\nGame Over\n"
page_04 = "\nIl faut que tu trouves des chaudières. Tu cherches un peu et entre dans une chambre froide.\nMiracle, elle est remplie de chaudières."
page_05 = "\nLe cuisinier te sourit. «Oublie les patates big, Marco s'en occupe. Aide moi à couper des légumes pour ce soir.»"
page_06 = "\nLe chef te voit se promener avec une cannette de peinture blanche. Il se fâche et te renvoi sur le champ.\n\nGame Over\n"
page_07 = "\nBravo imbécile. Après avoir coupé plusieurs patates, le chef passe proche et voit tes chaudières.\nElles sont pour faire tremper les têtes de moppe, tu perds ton emploi.\n\nGame Over\n"
page_08 = "\nBien joué! Jusqu'à présent personne ne soupçonne ton manque extrême de connaissances culinaires.\nT'as réussi à blanchir une chaudière de patates."
page_09 = "\nTu ne sais pas aiguiser un couteau. Tu te coupe violemment la main et tu saignes dans tous les légumes déjà préparés.\nOn te renvoi et tu dois toi-même appeler l'ambulance.\n\n Game Over\n"
page_10 = "\nL'angoisse s'empare de toi, tu te mets à suer à profusion.\nTu regardes à nouveau le cuisinier, il a un tattoo de larme sous l'oeil, tu ne te sens pas très bien."
page_11 = "\nLa chance te sourit, il t'avoue lui aussi avoir menti sur son CV.\n«T'as juste à donner des ordres et les gens pensent que tu sais ce que tu fais.»"
page_12 = "\nLe chef passe près de toi et voit que tu ne fais rien.\nIl te demande avec un ton fâché d'aller chercher des culs de poule pour continuer la préparation."
page_13 = "\nTu viens de te tirer dans le pied.\n«Une pause? En cuisine? Je savais pas que les princesses se cherchaient de l'ouvrage!»\nLe chef te renvoie.\n\nGame Over\n"
page_14 = "\nLe chef te regardes avec dégoût.\n«Tu m'écoeures, remplis de jugement. On est en 2026, ce tattoo de larme représente sa sensibilité. Sors de ma cuisine.» \n\nGame Over\n"
page_15 = "\nIl te regarde confus. «Mon premier quoi?» Il essuie son visage. Oh oh, c'etait juste de la saleté."
page_16 = "\nUn des cuisinier sursaute , te regarde et se dépêche à aller blanchir des patates. «Wow ca marche pour vrai!» Tu prends tes aises."
page_17 = "\n«Est-ce que tu me donnes le même ordre que je viens juste de te donner? Fuck off man.»\nIl va voir le chef et lui apprend que tu ne sais rien. Il te renvoi.\n\nGame Over\n"
page_18 = "\nLe cuisinier te regarde. Il y a un long silence. Il répond: «Non»"
page_19 = "\nLe chef a un air contrarié. «Ça te fais rire la cuisine? Sais-tu c'est quoi un cul de poule?»"
page_20 = "\nLe chef te regarde confus. «Ok, t'as les oeufs...t'as pas pris les culs de poule pour les mettre dedans?»"
page_21 = "\nPar miracle tu es accidentellement tombé sur le bon item, fiou. Le chef enchaîne:\n«Parfait!, maintenant prend une langue de chat, on en a pas beaucoup, t'en auras besoin tantôt.» "
page_22 = "\nIl le prend comme une insulte, comme si tu le narguais. «Eille le nouveau! C'est quoi ton esti de problème?"
page_23 = "\nIl pense que tu parles de son tattoo sur la main. Il te sourit et réponds que non, il en a plein. «Tu veux les voir?»"
page_24 = "\nTu claquais des doigts tellement fort, le chef t'as entendu et t'as vu faire.\nIl se rend compte que tu fais n'importe quoi. Tu perds ton emploi.\n\nGame Over\n"
page_25 = "\nUn cuisinier te réponds: «T'as juste à te regarder dans le miroir big!» Il rit bien trop fort, tout le monde se retourne."
page_26 = "\nTu es surpris et stupéfait de voir à quel point énormément de cuisiniers ont des cigarettes sur eux.\nTu es encore plus impressionné de voir à quel point personne ne s'est posé de question en te lancant leur paquet."
page_27 = "\nIl s'approche et te pousse. Tu tombes contre le four et te brûle la main. Tu cries, tu as mal, personne ne t'aides.\nTu quittes sans avertir. Le chef te texte plus tard pour te dire qu'il n'aime pas les fuyards.\nTu es renvoyé.\n\nGame Over\n"
page_28 = "\nIl s'approche avec un air bête. «Si je te donne 5$, est-ce que t'arrêtes de me parler?» "
page_29 = "\nIl ne dit pas un mot. Il sait que tu ne sais pas. Il ne fait que pointer la sortie.\n\nGame Over\n"
page_30 = "\nTu n'as jamais vu un visage aussi rouge de colère. Il crie et t'obliges à quitter.\n\nGame Over\n"
page_31 = "\nÉtrangement il te crois et quittes. Tu passes un très beau fin de quart de travail.\n\nVictoire\n"
page_32 = "\nIl te réponds: «Je suis pas prof, je suis chef. Va-t'en.»\n\nGame Over\n"
page_33 = "\nLe chef te regardes intrigué. «Non... Peut-être que vous appeliez ça des maryses dans ton cours?»"
page_34 = "\nIl te réponds calmement: «Ok j'en ai vu assez, va-t'en.»\n\nGame Over\n"
page_35 = "\nSa question n'en était pas une vraie. Cet homme a un problème de tempérament.\nIl s'avance vers toi et il t'enligne une droite au visage. Le chef vous renvoi les deux sur le champs.\n\nGame Over\n"
page_36 = "\nTu te réveilles à l'hôpital.\n\nGame Over\n"
page_37 = "\nIl le prend super mal. Malheureusement pour toi, c'est le fils du chef. Il va voir son père et tu perds ta job.\n\nGame Over\n"
page_38 = "\nIl enlève son chandail et est maintenant torse nu dans la cuisine. Un inspecteur passe au même moment et oblige la cuisine à fermer.\nTechniquement, ce n'est pas un renvoi.\n\nVictoire\n"
page_39 = "\nPersonne ne rit. Cette blague est misogyne, irrespectueuse et de trop.\nTu es étrange, lourd et inconfortable à côtoyer. On te demande de partir.\n\nGame Over\n"
page_40 = "\nÉtrangement personne ne rentre dans ce frigo de tout le reste de ton quart de travail et personne ne remarque ton absence.\nTu sors à la fin de ton shift. Félicitations.\n\nVictoire\n"
page_41 = "\nCome on, la cigarette c'est vilain. Tu ne perds pas ton emploi, mais tu perds au jeu de la vie.\n\nGame Over\n"
page_42 = "\nToute la cuisine fume, tu deviens automatiquement la honte du restaurant.\nPlus personne ne te parle et t'aide, le chef se rend vite compte que tu ne sais pas quoi faire.\nIl te demande de quitter.\n\nGame Over\n"
page_43 = "\nIl prend ton 50$ et quitte. Tu passes le restant de ton quart de travail aux aguets, mais tout se passe à merveilles. Félicitations.\n\nVictoire\n"
page_44 = "\nIl te donne 5$ et te laisse tranquille. Le chef vient te voir et t'annonce que la préparation est maintenant terminée.\nFélicitation, tu as terminé la premiere partie de ton premier shift coupé.\n\nVictoire\n"
page_45 = "\nLe chef rit et quitte. Il pense que tu le niaises à 100%. Il se dit déjà qu'il va beaucoup t'apprécier.\nBravo, ton premier quart de travail est déjà terminé. Tu quittes la tête haute, mais tjrs aussi inutile.\n\nVictoire\n"
page_46 = "\nLe chef soupir fort. «Tu m'as dit que t'étais allé à l'école de cuisine...laisse ton tablier à l'entrée. t'es viré.»\n\nGame Over\n"

# Options disponibles pour chaque page.
# Nomenclature: choix_(# de page)_(choix # 01, 02 ou 03)
choix_01_01 = "Tu prends un bon grand respir et te dirige au travail, ça va passer."
choix_01_02 = "Tu décides de prendre 2-3 shooters pour la confiance. Il est midi quelque part comme on dit."
choix_02_01 = "Tu décides d'aller remplir une chaudière d'eau bouillante salée et une chaudière d'eau glacée pour les patates."
choix_02_02 = "Tu restes immobile, paniqué. Tu vois un cuisinier au loin qui te fait signe d'approcher. Tu te rends vers lui."
choix_02_03 = "Tu fouilles partout à la recherche de peinture blanche."
choix_04_01 = "Tu vois deux chaudières remplies d'eau. Tu décides de sauver du temps pour mieux paraître. Tu pars avec."
choix_04_02 = "Tu prends les deux chaudières vides du bord et retourne en cuisine."
choix_05_01 = "Tu décides d'aiguiser ton couteau avant de couper quoi que ce soit."
choix_05_02 = "Tu prends un couteau et fixe la carotte devant toi."
choix_05_03 = "Tu lui avoue ne rien savoir et que tu as besoin d'aide pour ne pas que ça paraisse."
choix_08_01 = "Tu te places au seul poste où il y n'y a personne...Tu attends."
choix_08_02 = "Tu demandes au chef quand est-ce qu'on prend la pause de 15 minutes"
choix_10_01 = "Tu paniques encore plus. Tu quittes la station et tu vas aviser ton chef que tu ne te sens pas en sécurité."
choix_10_02 = "Tu complimentes son tattoo et lui demande si c'est son premier."
choix_11_01 = "Tu dis: «Sérieux? Heille toi! Va blanchir des patates!»"
choix_11_02 = "Tu réponds: «D'accord...» Tu hésites. «Coupe les légumes pour ce soir!»"
choix_11_03 = "Tu dis: «Nice. Toi là-bas! donne moi 20$!»"
choix_12_01 = "Tu ris dans sa face en entendant cet enchainement de mots et tu penses qu'il te niaise."
choix_12_02 = "Tu pars chercher ce qu'on te demande. Tu reviens avec des oeufs."
choix_12_03 = "Tu regardes autour de toi et tu prends la première chose que tu vois: des bols en stainless."
choix_15_01 = "Tu tentes de sauver la situation: «C'est ton premier shift?»"
choix_15_02 = "Tu râcles ta gorge et répètes: «C'est ton premier tattoo?»"
choix_16_01 = "Tu fixes un autre employé et tu claques des doigts pour qu'il te regarde. «J'ai besoin de persil!»"
choix_16_02 = "Tu ajoutes: «Toi!, vite, j'ai besoin de lait!»"
choix_16_03 = "Tu demandes en blague une cigarette. «Vite, j'ai besoin d'une clope!»"
choix_18_01 = "Tu rétorques: «De quoi, non? Fais ce que je te dis!»"
choix_18_02 = "Tu renchéris avec un air baveux: «Ok...30$?»"
choix_19_01 = "Tu réponds avec un ton incertain: «Bin oui je sais c'est quoi...»"
choix_19_02 = "Tu le corriges: «Ça s'appelle un cloaque.»"
choix_20_01 = "Tu mens: «Pas besoin, je suis un pro. Fais-moi confiance.»"
choix_20_02 = "Tu décides d'être honnête: «Chef, je ne sais pas ce que je fais... Voulez-vous m'apprendre?»"
choix_21_01 = "Tu lui demandes tanné: «Est-ce que tu me niaises depuis tantôt? Des culs de poule, des langues de chats...»"
choix_21_02 = "Tu prends une louche près de toi."
choix_22_01 = "Tu lèves les mains dans les airs et réponds nerveux:«Woah! Pour vrai je cherche pas la marde, promis!»"
choix_22_02 = "Tu ne te laisses pas parler demême, tu réponds avec un ton hautain: «En ce-moment? Ton attitude.»"
choix_23_01 = "Tu lui réponds: «Honnêtement, Non.»"
choix_23_02 = "Tu lui dis en hésitant: «Euhmm Ok..Oui»"
choix_25_01 = "Tu fais semblant de rire. Tu lui réponds: «Tu pourrais aller chez ta mère et aller le prendre directement de la vache haha»"
choix_25_02 = "Tu fais semblant de rire et tu vas t'enfermer dans une des chambres froide. Cette blague t'as atteint."
choix_26_01 = "Tu commences à fumer."
choix_26_02 = "Tu ris et t'exclames: «Bin voyons gang, je niaisais. Ça m'écoeure la cigarette.»"
choix_28_01 = "Intimidé par sa carrure, tu sors 50$ de ton porte-feuille."
choix_28_02 = "Tu ne dis rien et ne fais que mimer une fermeture-éclair qui se ferme par-dessus ta bouche."
choix_33_01 = "Tu lui dis: «Mais c'est qui Maryse? Tout ce que vous dîtes ne fait aucun sens chef.»"
choix_33_02 = "Tu réponds rapidement: «J'ai pas eu de cours chef!»"

# Variable pour insérer dans la fonction choisir_options.
absence_choix = " "

# Fonction pour choix
def choisir_options(choix1, choix2, choix3):
      
    """
    Entrées: Deux ou Trois choix (texte)
    Sortie: Option choisie (int)
    But: demander à l'utilisateur de choisir une option

    """
    
    while True: 

        if choix3 == absence_choix:
            print("\nQue fais-tu?")
            print("-------------------------------------------------------------------------------------------------------------\n")
            print(f"1: {choix1}\n2: {choix2}\n")
            decision = (input("Choix: "))
            supprimer_vieux_texte()

            if decision == "1" or decision == "2":
             return int(decision)
          
            else:
                print("\nJ'aime ton énergie, mais il faudrait choisir une des options proposées.\n")

     
        else:
          print("\nQue fais-tu?")
          print("-------------------------------------------------------------------------------------------------------------\n")
          print(f"1: {choix1}\n2: {choix2}\n3: {choix3}\n")
          decision = (input("Choix: "))
          supprimer_vieux_texte()

          if decision == "1" or decision == "2" or decision == "3":
             return int(decision)
          
          else:
              print("\nJ'aime ton énergie, mais il faudrait choisir une des options proposées.\n")

def supprimer_vieux_texte():
    """
    Entrées: Aucune
    Sortie: commande
    But: effacer le texte dans le terminal.(Entrer la commande "clear" sans avoir à l'écrire.)

    """
    subprocess.run("cls", shell=True)
    # .run execute une commande
    # "cls" est la commande "clearscreen" pour Windows qu'on run == ecrire "clear" sur le terminal
    # shell=True execute la commande dans le cmd.exe de Windows. Sinon il cherche cls.exe et rien ne se passe.
    


# Début du jeu
supprimer_vieux_texte()
print(page_01)
decision_01 = choisir_options(choix_01_01, choix_01_02, absence_choix)

if decision_01 == 2:
    print(page_02)
    decision_02 = choisir_options(choix_02_01, choix_02_02, choix_02_03)

    if decision_02 == 1:
        print(page_04)
        decision_04 = choisir_options(choix_04_01, choix_04_02, absence_choix)

        if decision_04 == 1:
            print(page_07)

        elif decision_04 == 2:
            print(page_08)
            decision_08 = choisir_options(choix_08_01, choix_08_02, absence_choix)

            if decision_08 == 1:
                print(page_12)
                decision_12 = choisir_options(choix_12_01, choix_12_02, choix_12_03)

                if decision_12 == 1:
                    print(page_19)
                    decision_19 = choisir_options(choix_19_01, choix_19_02, absence_choix)

                    if decision_19 == 1:
                        print(page_29)
                    
                    elif decision_19 == 2:
                        print(page_30)

                elif decision_12 == 2:
                    print(page_20)
                    decision_20 = choisir_options(choix_20_01, choix_20_02, absence_choix)

                    if decision_20 == 1:
                        print(page_31)

                    elif decision_20 == 2:
                        print(page_32)

                elif decision_12 == 3:
                    print(page_21)
                    decision_21 = choisir_options(choix_21_01, choix_21_02, absence_choix)

                    if decision_21 == 1:
                        print(page_33)
                        decision_33 = choisir_options(choix_33_01, choix_33_02, absence_choix)

                        if decision_33 == 1:
                            print(page_45)
                        
                        elif decision_33 == 2:
                            print(page_46)

                    elif decision_21 == 2:
                        print(page_34)

            elif decision_08 == 2:
                  print(page_13)

    elif decision_02 == 2:
        print(page_05)
        decision_05 = choisir_options(choix_05_01, choix_05_02, choix_05_03)

        if decision_05 == 1:
            print(page_09)

        elif decision_05 == 2:
            print(page_10)
            decision_10 = choisir_options(choix_10_01, choix_10_02, absence_choix)

            if decision_10 == 1:
                print(page_14)

            elif decision_10 == 2:
                print(page_15)
                decision_15 = choisir_options(choix_15_01, choix_15_02, absence_choix)

                if decision_15 == 1:
                    print(page_22)
                    decision_22 = choisir_options(choix_22_01, choix_22_02, absence_choix)

                    if decision_22 == 1:
                        print(page_35)

                    elif decision_22 == 2:
                        print(page_36)

                elif decision_15 == 2:
                    print(page_23)
                    decision_23 = choisir_options(choix_23_01, choix_23_02, absence_choix)

                    if decision_23 == 1:
                        print(page_37)

                    elif decision_23 == 2:
                        print(page_38)

        elif decision_05 == 3:
            print(page_11)
            decision_11 = choisir_options(choix_11_01, choix_11_02, choix_11_03)

            if decision_11 == 1:
                print(page_16)
                decision_16 = choisir_options(choix_16_01, choix_16_02, choix_16_03)

                if decision_16 == 1:
                    print(page_24)

                elif decision_16 == 2:
                    print(page_25)
                    decision_25 = choisir_options(choix_25_01, choix_25_02, absence_choix)

                    if decision_25 == 1:
                        print(page_39)

                    elif decision_25 == 2:
                        print(page_40)

                elif decision_16 == 3:
                    print(page_26)
                    decision_26 = choisir_options(choix_26_01, choix_26_02, absence_choix)

                    if decision_26 == 1:
                        print(page_41)

                    elif decision_26 == 2:
                        print(page_42)

            elif decision_11 == 2:
                print(page_17)

            elif decision_11 == 3:
                print(page_18)
                decision_18 = choisir_options(choix_18_01, choix_18_02, absence_choix)

                if decision_18 == 1:
                    print(page_27)

                elif decision_18 == 2:
                    print(page_28)
                    decision_28 = choisir_options(choix_28_01, choix_28_02, absence_choix)

                    if decision_28 == 1:
                        print(page_43)

                    elif decision_28 == 2:
                        print(page_44)

    elif decision_02 == 3:
        print(page_06)

elif decision_01 == 1:
    print(page_03)



    



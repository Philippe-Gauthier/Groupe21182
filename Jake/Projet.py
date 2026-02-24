"""Projet Histoire interactive
LA REMISE FINALE DOIT ÊTRE FAITE DANS MON DOSSIER SUR LA BRANCHE MAIN - TITRE REMISE FINALE OU AUTRE
Par Jacob Chagnon"""
scene = "debut" #scene est une variable. elle stockera le nom de la scène à tout moment de l'histoire et elle me permet de réutiliser les chiffres 1 - 2 pour mes choix
jeu_actif = True #Permet d'arrêter le jeu si le personnage meurt ou arrête son aventure
import time #Permet de mettre sleep dans mes prints pour faire défiler le texte plutôt que tout l'envoyer d'un seul coup

while jeu_actif:
    if scene == "debut":
        print ("Un mur d'arbres se dresse devant toi. Les épines de conifères s'étendent jusqu'à l'horizon, et ce, de chaque côté.")
        time.sleep(2)
        print ("Une affiche à l'orée de la forêt te prévient que tu es sur le point de passer sur un terrain privé, mais une voix tente de t'attirer vers l'intérieur.")
        time.sleep(2) 
        print ("Tu t'avances vers la forêt (1) ou tu t`éloignes (2)") 
        #Premier choix de l'histoire, mais sûrement aussi décisif que le dernier de l'histoire *hint hint*

        choix = input("> ")
        if choix == "1":
            scene = "marche"
        elif choix == "2":
            scene = "fin1"
        else:
            print ("Choix invalide.")
    elif scene == "fin1":
        print ("L'aventure se termine avant d'avoir commencé.")
        jeu_actif = False #Jeu se termine. L'aventurier est une moumoune.
    elif scene == "marche":
        print ("Les feuilles craquent sous tes pieds. La voix se fait rassurante; comme un petit frère qui essaie d'avoir ton attention. ")
        time.sleep(2)
        print ("La voix se dédouble. La partie plus haute vient d'une clairière à gauche, et la partie basse vient d'un étang à droite.")
        time.sleep(2)
        print ("Où veux-tu aller? À gauche(1), ou à droite(2)?")
        choix = input ("> ")
        if choix == "1":
            scene = "clairiere"
        elif choix == "2":
            scene = "etang"
        else:
            print("Choix invalide.")

    elif scene == "clairiere":
        print("La clairière illuminée par la Lune te semble la plus invitante. En cherchant la source de la voix, tu tombes face-à-face avec un chevreuil.")
        time.sleep(2)
        print (" Il n'est pas effrayé. À ton choix, tu peux tenter de le flatter(1) ou le laisser tranquille(2).")
        choix = input("> ")
        if choix == "1":
            print ("Le chevreuil te mord et s'enfuit. Tu continues vers la source de la voix.")
            time.sleep(2)
            scene = "voix1"
        elif choix == "2":
            print("Tu continues vers la source de la voix.")
            scene = "voix1"
        else:
            print ("Choix invalide.")
    elif scene == "etang":
        print("L'étang semblait être le meilleur choix pour toi. La surface réflète la Lune avec un éclat presque éblouissant.")
        time.sleep(2)
        print("Tu cherches la source de la voix. Elle s'élève d'une colonne de bulles sortant du centre du corps d'eau.")
        time.sleep(2)
        print("Tu peux essayer d'aller rejoindre la voix (1) ou tu peux rebrousser chemin(2). Que fais-tu?")
        choix = input("> ")
        if choix == "1":
            scene = "noyade"
        elif choix == "2":
            scene == "loup"
        else:
            print ("Choix invalide.")
    elif scene == "noyade":
        print("Tu t'approches du centre de l'étang. L'eau est peu profonde.")
        time.sleep(2)
        print("Soudainement, une main sort de l'eau à très grande vitesse.")
        time.sleep(2)
        print("La main t'attrape par le visage et te tire sous l'eau. L'air sort de ta poitrine, et tu te prépares à une mort lente.")
        jeu_actif = False
    elif scene == "loup":
        print("Un loup bloque ton chemin, ses dents visibles entre ses lèvres retroussées.")
        time.sleep(2)
        print("Il te saute à la gorge. Tu t'éteins.")
        jeu_actif = False
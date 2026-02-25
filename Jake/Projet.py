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

    elif scene == "voix1":
        print("Tu trouves la source de la voix. C'est un petit chat blond. Il est couché sur une grande pile d'or.")
        time.sleep(2)
        print("À ta vue, il descent de son trône de dragon. Il grimpe sur ton épaule.")
        time.sleep(2)
        print("Il te chuchote: Ce n'est pas pour te faire peur, mais tout ceci est mon royaume. Vois-tu, cela fait plus de deux ans que je repose ici.")
        time.sleep(2)
        print("Je règne pour toujours dans cette forêt. J'aime bien mes sujets, mais la seule chose qui me tient ici est l'espoir qu'un jour mon propre roi revienne.")
        time.sleep(2)
        print("À tous les jours il pense à moi. C'est son amour qui me donne la force de rester dans cet endroit.")
        time.sleep(2)
        print("Je t'offre un choix pour finir cette histoire. Tu peux décider de rester dans ton rêve et vivre dans la forêt avec moi(1), tu peux te réveiller(2), ou rester un peu plus longtemps pour mieux me connaître(3).")
        choix = input("> ")
        if choix == "1":
            scene == "fin2"
        elif choix == "2":
            scene == "fin3"
        elif choix == "3":
            scene == "questions"
        else:
            print("Choix invalide.")

    elif scene == "fin2":
        print("Tu restes endormi. Avec le chat, tu apprends à chasser, à trouver de l'eau douce et lire les sons de la forêt.")
        time.sleep(2)
        print("Avec le temps, tu oublies ta vie à l'extérieur. Tu ne t'ennuies plus de ta famille. Chaque jour est difficile, mais, à force de te servir de tes mains, tu développes un véritable amour pour cet endroit.")
        time.sleep(2)
        print("Tu vis heureux avec le chat comme fidèle compagnon.")
        time.sleep(2)
        print("FIN")
        jeu_actif = False

    elif scene == "fin3":
        print("Tu te réveilles doucement dans ton lit.")
        time.sleep(2)
        print("Les souvenirs vivides de ton rêve ne quittent pas ton esprit.")
        time.sleep(2)
        print("Tu sens un poids sur tes genoux, mais, quand tu regardes, il n'y a rien.")
        time.sleep(2)
        print("La masse qui repose sur toi se soulève, et tu sens ses pattes descendre de ton lit.")
        time.sleep(2)
        print("Un miaulement doux se fait entendre. Tu te rendors.")
        time.sleep(2)
        print("FIN")
    
    elif scene == "questions":
        print("Que veux-tu connaître? Mon histoire(1), ou mon roi(2)?")
        choix = input("> ")
        if choix == "1":
            scene == "lancelot"
        elif choix == "2":
            scene == "roi"
        else:
            print("Choix invalide.")

    elif scene == "lancelot":
        print("Je m'appelle Lancelot. J'ai vécu dans ces bois pendant 10 ans avec mon roi. On chassait ensemble à presque tous les jours.")
        time.sleep(2)
        print("Il était un superbe archer. J'utilisais mes griffes, personnellement. On partageait toujours nos prises.")
        time.sleep(2)
        print("Il sortait de la mousse grise de son sac et nous allumait un petit feu, pour se réchauffer et pour cuire sa viande.")
        time.sleep(2)
        print("Il me gardait toujours quelques morceaux crus. Il choisissait chaque fois les meilleurs pièces avec le plus de gras.")
        time.sleep(2)
        print("Il est temps pour toi de retourner chez toi.")
        time.sleep(5)
        print("Tu te réveilles doucement dans ton lit.")
        time.sleep(2)
        print("Les souvenirs vivides de ton rêve ne quittent pas ton esprit.")
        time.sleep(2)
        print("Tu sens un poids sur tes genoux, mais, quand tu regardes, il n'y a rien.")
        time.sleep(2)
        print("La masse qui repose sur toi se soulève, et tu sens ses pattes descendre de ton lit.")
        time.sleep(2)
        print("Un miaulement doux se fait entendre. Tu te rendors.")
        time.sleep(2)
        print("FIN")
    
    elif scene == "roi":
        print("Mon roi était un humain comme toi. Il était grand et fort.")
        time.sleep(2)
        print("Il utilisait des outils qui me semblaient comme de la magie.")
        time.sleep(2)
        print("Il me portait sur ses épaules ou dans ses bras quand je me sentais fatigué ou quand j'avais froid.")
        time.sleep(2)
        print("À tous les jours on allait se promener ensemble, découvrir des nouveaux endroits dans la forêt.")
        time.sleep(2)
        print("Il sortait sa grande feuille de papier et il dessinait chaque pas qu'on prenait dans une nouvelle direction.")
        time.sleep(2)
        print("Il n'a jamais terminé son dessin de la forêt. Ses devoirs l'ont apporté ailleurs.")
        time.sleep(2)
        print("Ses conseillers et lui ont décidé que je serais plus heureux de rester dans la forêt plutôt que de venir avec lui.")
        time.sleep(2)
        print("Et ils avaient raison. Je m'ennuyais, c'est certain, mais je voulais terminer son projet.")
        time.sleep(2)
        print("Ça a pris si longtemps, mais maintenant, je connais chaque arbre de cette forêt et toutes leurs histoires.")
        time.sleep(2)
        print("J'espère un jour pouvoir lui remettre sa carte complétée.")
        time.sleep(2)
        print("Il est temps pour toi de retourner chez toi.")
        time.sleep(5)
        print("Tu te réveilles doucement dans ton lit.")
        time.sleep(2)
        print("Les souvenirs vivides de ton rêve ne quittent pas ton esprit.")
        time.sleep(2)
        print("Tu sens un poids sur tes genoux, mais, quand tu regardes, il n'y a rien.")
        time.sleep(2)
        print("La masse qui repose sur toi se soulève, et tu sens ses pattes descendre de ton lit.")
        time.sleep(2)
        print("Un miaulement doux se fait entendre. Tu te rendors.")
        time.sleep(2)
        print("FIN")
from time import sleep
from unittest import case
import random

def choix(question,choix1,choix2,choix3):
    print(question)
    sleep(0.5)
    print("1. " + choix1)
    sleep(0.5)
    print("2. " + choix2)
    sleep(0.5)
    print("3. " + choix3)
    reponse = input("Votre choix: ")
    while reponse not in ["1", "2", "3", "inventaire", "quitter"]:
        print("Choix invalide. Veuillez choisir 1, 2, 3, inventaire ou quitter.")
        reponse = input("Votre choix: ")
    return reponse

def dice_roll(crit_fail,fail,success,crit_success):
    d20 = random.randint(1, 20)
    print(f"Vous avez lancé un d20 et obtenu: {d20}")
    if d20 == 1:
        print(crit_fail)
        return 1
    elif d20 < 10:
        print(fail)
        return 2
    elif d20 < 20:
        print(success)
        return 3
    elif d20 == 20:
        print(crit_success)
        return 4

def gamble(argent):
    bet = int(input("Combien voulez-vous parier? Vous avez " + str(argent) + " $ "))
    while bet > argent or bet <= 0:
        print("Montant invalide. Veuillez entrer un montant entre 1 et " + str(argent) + " $")
        bet = int(input("Combien voulez-vous parier? Vous avez " + str(argent) + " $ "))
    d20 = dice_roll("Echec critique: Tu n'accepte pas la défaite et continue de misé jusqu'à ne plus avoir d'argent. ","Echec: tu perds l'argent que tu as misé","Reussite: tu as gagné " + str(bet) + " $","Reussite critique: tu as gagné " + str(bet**2) + " $")
    if d20 == 1:
        argent = 0
    elif d20 == 2:
        argent -= bet
    elif d20 == 3:
        argent += bet
    elif d20 == 4:
        argent += bet**2
    print("Tu as maintenant " + str(argent) + " $")
    
#_________________________________________________________________________________
argent = 0
print("Bienvune dans votres aventure, faites vos chois parmis ceux proposés. Vous pouvez egalement taper quitter pour quitter le jeu.")


reponse = choix("Tu ouvre le frigo apres t'avoir levé pour te rendre compte que tu n'as plus de lait. Tu ne peux rien faire de productif avant d'en avoir acheté. Tu sors de chez toi et part vers : ","Le nord","L'est","L'ouest")

match reponse:

    #nord
    case "1":  
        def nord():
           
            reponse = choix("Tu te dirige vers le nord. Tu croise une grand mere qui deplace un meuble.","Aider la grand mere ","Voller la poste de la grand mere","Continer ton chemin")
            match reponse:
                case "1":  
                    print("Tu decides d'aider la grand mere. Elle te remercie et tu continue ton chemin.")
                    reponse = choix("Tu arrive au dépaneur et tu vois que le lait est a 20$ a cause des taifs et l'inflation tu as " + str(argent) + " $","Acheter le lait","Quitter le dépaneur et aller vers l'est","Quitter le dépaneur et aller vers l'ouest")
                    match reponse:
                        
                        case "1":  
                            if argent >= 20:
                                argent -= 20
                                print("Tu achete le lait et tu retourne chez toi pour continuer ta journée. Tu as maintenant " + str(argent) + " $")
                                exit()
                            else:
                                reponse = choix("Tu n'as pas assez d'argent pour acheter le lait. Tu dois trouver une autre solution.","Abandonner","Quitter le dépaneur et aller vers l'est","Quitter le dépaneur et aller vers l'ouest")
                                match reponse:
                                    case "1":  
                                        print("Tu abandonne et retourne chez toi les mains vides. Tu ne peux pas continuer ta journée sans lait.")
                                        exit()

                                    case "2":                                  
                                        reponse = choix("Tu te dirige vers l'est et arrive à un cul-de-sac avec des ordures.","Abandonne et retourne chez toi","investiguer","Faire demi-tour vers l'ouest")
                                        match reponse:
                                        
                                            case "1":  
                                                print("Tu abandonne et retourne chez toi les mains vides. Tu ne peux pas continuer ta journée sans lait.")
                                                exit()
                                                
                                            #investiguer les poubelles
                                            case "2":
                                                resultat_poubelle = dice_roll("Echec critique: tu sors des poubelles avec une odeur terrible et les mais vides","Echec: tu sors des poubelles avec les mais vides ","Reussite: tu sors des poubelles avec 1$ ","Reussite critique: tu trouve une bouteille de lait intacte dans les poubelles! ")
                                                if resultat_poubelle == 4:
                                                    print("Felicitation, tu as trouvé une bouteille de lait tu peux retourner chez toi et continuer ta journé!")
                                                    exit()
                                                elif resultat_poubelle == 3:
                                                    argent += 5
                                                    print("tu as trouvé 5$ tu as maintenant " + str(argent) + " $")
                                                reponse = choix("Que fais-tu?","Faire demi-tour vers le nord.","Faire demi-tour vers l'ouest","quiter")
                                                
                                            #ouest
                                            case "3":
                                                reponse = choix("Q2","A","B","C")
                                            
                                            case "quitter":
                                                print("au revoir")
                                                exit()

                                    case "3":
                                        reponse = choix("Q2","A","B","C")
                                    
                                    case "quitter":
                                        print("au revoir")
                                        exit()

                        case "2":
                            reponse = choix("Tu te dirige vers l'est et arrive à un cul-de-sac avec des ordures.","Abandonne et retourne chez toi","investiguer","Faire demi-tour vers l'ouest")
                            match reponse:
                                        
                                case "1":  
                                    print("Tu abandonne et retourne chez toi les mains vides. Tu ne peux pas continuer ta journée sans lait.")
                                    exit()
                                                
                                #investiguer les poubelles
                                case "2":
                                        resultat_poubelle = dice_roll("Echec critique: tu sors des poubelles avec une odeur terrible et les mais vides","Echec: tu sors des poubelles avec les mais vides ","Reussite: tu sors des poubelles avec 1$ ","Reussite critique: tu trouve une bouteille de lait intacte dans les poubelles! ")
                                        if resultat_poubelle == 4:
                                            print("Felicitation, tu as trouvé une bouteille de lait tu peux retourner chez toi et continuer ta journé!")
                                            exit()
                                        elif resultat_poubelle == 3:
                                                argent += 5
                                                print("tu as trouvé 5$ tu as maintenant " + str(argent) + " $")
                                                choix("Que fais-tu?","Faire demi-tour vers le nord.","Faire demi-tour vers l'ouest","quiter")
                                                
                                            #ouest
                                case "3":
                                    reponse = choix("Q2","A","B","C")
                                            
                                case "quitter":
                                    print("au revoir")
                                    exit()
            
                        case "3":
                            reponse = choix("Q2","A","B","C")
                        
                        case "quitter":
                            print("au revoir")
                            exit()


                case "2":

                    argent += 5
                    print("tu volle la poste de la grand mere sans deffence. Tu trouve 5$ et tu continue ton chemin avec un pas plus rapide. Tu as maintenant " + str(argent) + " $")
                    reponse = choix("Tu arrive au dépaneur et tu vois que le lait est a 20$ a cause des taifs et l'inflation tu as " + str(argent) + " $","Acheter le lait","Quitter le dépaneur et aller vers l'est","Quitter le dépaneur et aller vers l'ouest")

                case "3":
                    choix("Tu arrive au dépaneur et tu vois que le lait est a 20$ a cause des taifs et l'inflation tu as " + str(argent) + " $","Acheter le lait","Quitter le dépaneur et aller vers l'est","Quitter le dépaneur et aller vers l'ouest")

                case "quitter":
                    print("au revoir")
                    exit()

    #est
    case "2":
        reponse = choix("Tu te dirige vers l'est et arrive à un cul-de-sac avec des ordures.","Faire demi-tour vers le nord.","investiguer","Faire demi-tour vers l'ouest")
        match reponse:
            #nord
            case "1":  
                print("Tu fais demi-tour vers le nord et arrive au dépaneur. Tu vois que le lait est a 20$ a cause des taifs et l'inflation tu as " + str(argent) + " $")
            #investiguer les poubelles
            case "2":
                resultat_poubelle = dice_roll("Echec critique: tu sors des poubelles avec une odeur terrible et les mais vides","Echec: tu sors des poubelles avec les mais vides ","Reussite: tu sors des poubelles avec 1$ ","Reussite critique: tu trouve une bouteille de lait intacte dans les poubelles! ")
                if resultat_poubelle == 4:
                    print("Felicitation, tu as trouvé une bouteille de lait tu peux retourner chez toi et continuer ta journé!")
                    exit()
                elif resultat_poubelle == 3:
                    argent += 1
                    print("tu as " + str(argent) + " $")
                    reponse = choix("Que fais-tu?","Faire demi-tour vers le nord.","Faire demi-tour vers l'ouest","quiter")
                
            #ouest
            case "3":
                reponse = choix("Q2","A","B","C")
            
            case "quitter":
                print("au revoir")
                exit()
    #ouest
    case "3":
       reponse = choix("Tu te dirige vers l'ouest et trouve plusieurs source de revenus: une pizzeria qui recherche des livreurs, une table de black jack et une banque","Prendre le travail de livreurs","Jouer au black jack","Aller à la banque")
       while reponse == "3":
           reponse = choix("la banque est fermé pour le moment, revien plus tard.","Prendre le travail de livreurs","Jouer au black jack","Aller à la banque")
       match reponse:
        case "1":  
            argent += 19
            reponse = choix("Apres une journé de dure labeur tu as gagné 19$ tu as maintenant " + str(argent) + " $","Retourner chez toi ","Aller jouer au black jack","Aller a la banque")
            while reponse == "3":
                print("la banque est fermé pour le moment, revien plus tard.")
                reponse = choix("la banque est fermé pour le moment, revien plus tard.","Retourner chez toi","Jouer au black jack","Aller à la banque")
            match reponse:
                case "1":
                    reponse = choix("Tu retourne chez toi avec " + str(argent) + " $","Aller au nord","Aller à l'est","Quitter")
                    match reponse:
                        case "1":
                            reponse = choix("Q2","A","B","C")
                        case "2":
                            reponse = choix("Q2","A","B","C")
                        case "quitter":
                            print("au revoir")
                            exit()
                case "2":
                    if argent != 0:
                        argent = gamble(argent)
                        reponse = choix("Que fais-tu?","Aller au nord","Aller à l'est","Rejouer")
                        while reponse == "3":
                            argent = gamble(argent)
                            reponse = choix("Que fais-tu?","Aller au nord","Aller à l'est","Rejouer")
                        match reponse:
                            case "1":
                                print("")
                                            
                            case "2":
                                print("la banque est fermé pour le moment, revien plus tard.")
                                reponse = choix("Que fais-tu?","Prendre le travail de livreurs","Aller a l'est","Aller au nord")

                            case "quitter":
                                print("au revoir")
                                exit()
                            
                
                    else:
                        print("Tu n'as pas d'argent pour parier. Tu dois trouver une autre solution.")
                        reponse = choix("Que fais-tu?","Prendre le travail de livreurs","Aller à la banque","Retourner chez toi")
                    
    

        case "2":
            if argent != 0:
                argent = gamble(argent)
                reponse = choix("Que fais-tu?","Prendre le travail de livreurs","Aller à la banque","Rejouer")
                while reponse == "3":
                    argent = gamble(argent)
                    reponse = choix("Que fais-tu?","Prendre le travail de livreurs","Aller à la banque","Rejouer")
                match reponse:
                    case "1":
                        argent += 19
                        reponse = choix("Apres une journé de dure labeur tu as gagné 19$ tu as maintenant " + str(argent) + " $","Retourner chez toi","Aller a la banque","jouer au black jack")
                        while reponse == "3":
                            argent = gamble(argent)
                            reponse = choix("Que fais-tu?","retourner chez toi","Aller à la banque","Rejouer")
                            match reponse:
                                case "1":
                                    reponse = choix("Tu retourne chez toi avec " + str(argent) + " $","Aller au nord","Aller à l'est","Quitter")
                                case "2":
                                    print("la banque est fermé pour le moment, revien plus tard.")
                                    reponse = choix("Que fais-tu?","Aller vers le nord","Aller à l'est","Quitter")

                                    
                    case "2":
                        print("la banque est fermé pour le moment, revien plus tard.")
                        reponse = choix("Que fais-tu?","Prendre le travail de livreurs","Aller a l'est","Aller au nord")

                    case "quitter":
                        print("au revoir")
                        exit()
                    
                
            else:
                print("Tu n'as pas d'argent pour parier. Tu dois trouver une autre solution.")
                reponse = choix("Que fais-tu?","Prendre le travail de livreurs","Aller à la banque","Retourner chez toi")
            
    
        case "quitter":
            print("au revoir")
            exit()
    case "quitter":
        print("au revoir")
        exit()


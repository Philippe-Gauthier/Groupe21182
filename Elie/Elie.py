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

#_________________________________________________________________________________
argent = 0
print("Bienvune dans votres aventure, faites vos chois parmis ceux proposés. Vous pouvez egalement taper quitter pour quitter le jeu.")


reponse = choix("Tu ouvre le frigo apres t'avoir levé pour te rendre compte que tu n'as plus de lait. Tu ne peux rien faire de productif avant d'en avoir acheté. Tu sors de chez toi et part vers : ","Le nord","L'est","L'ouest")

match reponse:

    #nord
    case "1":  
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
                                    choix("Tu te dirige vers l'est et arrive à un cul-de-sac avec des ordures.","Abandonne et retourne chez toi","investiguer","Faire demi-tour vers l'ouest")
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
                                            choix("Q2","A","B","C")
                                        
                                        case "quitter":
                                            print("au revoir")
                                            exit()

                                case "3":
                                    choix("Q2","A","B","C")
                                
                                case "quitter":
                                    print("au revoir")
                                    exit()

                    case "2":
                        choix("Tu te dirige vers l'est et arrive à un cul-de-sac avec des ordures.","Abandonne et retourne chez toi","investiguer","Faire demi-tour vers l'ouest")
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
                                choix("Q2","A","B","C")
                                        
                            case "quitter":
                                print("au revoir")
                                exit()
        
                    case "3":
                        choix("Q2","A","B","C")
                    
                    case "quitter":
                        print("au revoir")
                        exit()


            case "2":

                argent += 5
                print("tu volle la poste de la grand mere sans deffence. Tu trouve 5$ et tu continue ton chemin avec un pas plus rapide. Tu as maintenant " + str(argent) + " $")
                choix("Tu arrive au dépaneur et tu vois que le lait est a 20$ a cause des taifs et l'inflation tu as " + str(argent) + " $","Acheter le lait","Quitter le dépaneur et aller vers l'est","Quitter le dépaneur et aller vers l'ouest")

            case "3":
                choix("Tu arrive au dépaneur et tu vois que le lait est a 20$ a cause des taifs et l'inflation tu as " + str(argent) + " $","Acheter le lait","Quitter le dépaneur et aller vers l'est","Quitter le dépaneur et aller vers l'ouest")

            case "quitter":
                print("au revoir")
                exit()

    #est
    case "2":
        choix("Tu te dirige vers l'est et arrive à un cul-de-sac avec des ordures.","Faire demi-tour vers le nord.","investiguer","Faire demi-tour vers l'ouest")
        match reponse:
            #nord
            case "1":  
                choix("Q2","1","2","3")
            #investiguer les poubelles
            case "2":
                resultat_poubelle = dice_roll("Echec critique: tu sors des poubelles avec une odeur terrible et les mais vides","Echec: tu sors des poubelles avec les mais vides ","Reussite: tu sors des poubelles avec 1$ ","Reussite critique: tu trouve une bouteille de lait intacte dans les poubelles! ")
                if resultat_poubelle == 4:
                    print("Felicitation, tu as trouvé une bouteille de lait tu peux retourner chez toi et continuer ta journé!")
                    exit()
                elif resultat_poubelle == 3:
                    argent += 1
                    print("tu as " + str(argent) + " $")
                choix("Que fais-tu?","Faire demi-tour vers le nord.","Faire demi-tour vers l'ouest","quiter")
                
            #ouest
            case "3":
                choix("Q2","A","B","C")
            
            case "quitter":
                print("au revoir")
                exit()
    #ouest
    case "3":
       choix("Vous vous dirigez vers l'ouest et trouve plusieurs source de revenus: une pizzeria qui recherche des livreurs, une table de black jack et un","","","C")

    case "quitter":
        print("au revoir")
        exit()

#case ---------------
match reponse:
    case "1":  
        choix("Q2","1","2","3")
    case "2":
        choix("Q2","A","B","C")
    case "3":
       choix("Q2","A","B","C")
    
    case "quitter":
        print("au revoir")
        exit()

dice_roll("Echec critique","Echec","Reussite","Reussite critique")
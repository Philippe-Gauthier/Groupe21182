"""
Vincent Goulet
 
Fichier principale projet livre interactif

"""

print("Ton ami viens d'avoir sa liscence de pilote d'avion et vous décidé de partir avec son avion qu'il vient de construire. Tout à coup, une tempête vous prend par surprise et vous vous écraser dans le milieu d'une forêt. Tu t'en est bien sorti mais ton ami est inconcient.")

def le_choix(choix_1, choix_2, choix_3, choix_4) :
    """
    Entrée : les trois choix (texte)
    Sortie : choix décider (entier)
    But : Demander à l'utilisateur quel action faire
    """
    print(f"1: {choix_1}")
    print(f"2: {choix_2}")
    if(choix_3 != ""):
        print(f"3: {choix_3}")
    if(choix_4 != ""):
        print(f"4: {choix_4}")        
    descision = int(input("Choisisez une option: "))
    if(le_choix != choix_1 and choix_2 and choix_3 and choix_4):
        print("euh, non! tu ne peux pas faire cela. Bye Bye!")
    
    return descision

soin = "Si tu veux chercher l'avion en esperant trouver du soin à ton ami, écrit : 1"
mauvais_chum = "Si tu décide de partir et laisser ton ami dans l'avion parce que tu est le pire des amis, écrit : 2"
espoire  = "Si tu décide de vérifier son poux avant toute maneuvre de réanimation, écrit : 3"

print("Qu'allez-vous faires?")

choix_un =le_choix(soin, mauvais_chum, espoire,"")


if (choix_un == 1 ) :
    print("Tu trouve une trousse de premier soin dans un des compariment et réussi à soigner la blessure de ton ami. 10 min passe et ton ami n'est toujour pas réveillé.")

    good = "Si tu veux commencer a t aventurer dans la foret, ecrit : 1"
    bad = "Si tu veux rester avec ton ami et le rejoindre dans les cieux, ecrit : 2"

    print("Qu'allez-vous faires ?")

    choix_deux = le_choix(good, bad,"","")

    if(choix_deux == 1):
        print("Avant de commencer la marche, tu as réussi à trouver une boussole et une bouteille d'eau dans l'avion. Tu dois décider maintenant dans quel direction te dirigé.")

        nord = "Si tu veux te diriger vers le nord, puisque c'est plus simple d'utiliser la boussole ainsi, écrit : 1"
        est = "Si tu décides de te dirgier vers l'est puisque c'était vers cette direction que vous vous dirigiez avant le crash, écrit : 2"
        sud = "Si tu te dit vouloir aller vers le sud puisque tu est à bout des température du canada et espères avoir plus chaud, écrit : 3"
        ouest = "Si tu prend la décision de te diriger vers l'ouest puisque tu avait apercu un village sur le chemin, écrit : 4"

        choix_debut = le_choix( nord, est, sud, ouest)
        
        if (choix_debut == 1 ) : 
            print(" ")

        elif (choix_debut == 2) : 
            print("")

        elif (choix_debut == 3):
            print("")

        




    elif(choix_deux == 2):
        print("La partie est terminer, mais tu as retrouver ton ami! Bon repos")

elif (choix_un == 2):
     print("Avant de commencer la marche, tu as réussi à trouver une boussole et une bouteille d'eau dans l'avion. Tu dois décider maintenant dans quel direction te dirigé.")
nord = "Si tu veux te diriger vers le nord, puisque c'est plus simple d'utiliser la boussole ainsi, écrit : 1"
est = "Si tu décides de te dirgier vers l'est puisque c'était vers cette direction que vous vous dirigiez avant le crash, écrit : 2"
sud = "Si tu te dit vouloir aller vers le sud puisque tu est à bout des température du canada et espères avoir plus chaud, écrit : 3"
ouest = "Si tu prend la décision de te diriger vers l'ouest puisque tu avait apercu un village sur le chemin, écrit : 4"
choix_debut = le_choix( nord, est, sud, ouest)
        
if (choix_debut == 1 ) : 
            print(" ")

elif (choix_debut == 2) : 
            print("")

elif (choix_debut == 3):
            print("")

elif (choix_un == 3):
    print("En vérifiant son poux, tu confirme le décès de ton meilleur ami. Tu dois tout de même faire un choix pour la suite.")
    good
    triste= "Tu n'encaisse pas le décès de ton ami et tu trouve injuste que tu soit toujours vivant. Si tu veux pleuré et rejoindre ton ami, écrit : 2"
    choix_trois = le_choix(good,triste,"","")
    if(choix_trois == 1): 
        print("Avant de commencer la marche, tu as réussi à trouver une boussole et une bouteille d'eau dans l'avion. Tu dois décider maintenant dans quel direction te dirigé.")

        nord = "Si tu veux te diriger vers le nord, puisque c'est plus simple d'utiliser la boussole ainsi, écrit : 1"
        est = "Si tu décides de te dirgier vers l'est puisque c'était vers cette direction que vous vous dirigiez avant le crash, écrit : 2"
        sud = "Si tu te dit vouloir aller vers le sud puisque tu est à bout des température du canada et espères avoir plus chaud, écrit : 3"
        ouest = "Si tu prend la décision de te diriger vers l'ouest puisque tu avait apercu un village sur le chemin, écrit : 4"
        choix_debut = le_choix( nord, est, sud, ouest)
            
    
    elif(choix_trois == 2):
        print("La partie est terminer, mais tu as retrouver ton ami! Bon repos")
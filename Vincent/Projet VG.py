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

choix_un = le_choix(soin, mauvais_chum, espoire,"")


if (choix_un == 1 ) :
    print("Tu trouve une trousse de premier soin dans un des compariment et réussi à soigner la blessure de ton ami. 10 min passe et ton ami n'est toujour pas réveillé.")

    good = "Si tu veux commencer a t aventurer dans la foret, ecrit : 1"
    bad = "Si tu veux rester avec ton ami et le rejoindre dans les cieux, ecrit : 2"

    print("Qu'allez-vous faires ?")

    choix_postsoin = le_choix(good, bad, "", "")

    if(choix_postsoin == 1):
        print("Avant de commencer la marche, tu as réussi à trouver une boussole et une bouteille d'eau dans l'avion. Tu dois décider maintenant dans quel direction te dirigé.")

        nord = "Si tu veux te diriger vers le nord, puisque c'est plus simple d'utiliser la boussole ainsi, écrit : 1"
        est = "Si tu décides de te dirgier vers l'est puisque c'était vers cette direction que vous vous dirigiez avant le crash, écrit : 2"
        sud = "Si tu te dit vouloir aller vers le sud puisque tu est à bout des température du canada et espères avoir plus chaud, écrit : 3"
        ouest = "Si tu prend la décision de te diriger vers l'ouest puisque tu avait apercu un village sur le chemin, écrit : 4"
        choix_debut = le_choix(nord, est, sud, ouest)
        
        if (choix_debut == 1 ) : 
            print("Cool! Tu trouve une rivière au moment que t'a gourde est vide. Que fais tu ?")

            gourde_un = "Si tu veux remplir ta gourde et faire une pause pour en boire, ecrit : 1"
            gourde_deux= "Si tu veux remplir ta gourde mais continuer ton chemin sans la boire tout de suite, ecrit : 2"
            baignade = "Si tu veux prendre le temps de te baigner puisque tu commence à avoir chaud, ecrit: 3"
            choix_postdebut = le_choix(gourde_un, gourde_deux, baignade,"")
            
            if (choix_postdebut == 1):
                 print("Tu est fier de ta décision puisque c'était la meilleur eau que tu n'a jamais bu. Tu trouve qu'il fait chaud donc tu te trempe les pied dans l'eau. L'eau est très bonne, tellement que tu ne te rend pas compte de se qui ce passait sur tes jambes...")
                 print("Oups... Des sangsues on eu le temps de prendre tout ton sang.")
                 print("La partie est terminer, mais tu as retrouver ton ami! Bon repos")
                 

            elif(choix_postdebut == 2 ) :
                 print("Maintenant, deux choix sofre à toi.")  

                 courant = "Soit suivre lee sens du courant, ecrit : 1"
                 invers_courant = "Soit suivre le sens inverse du courant, ecrit : 2"
                 choix_courant = le_choix (courant, invers_courant, "", "")

                 if (choix_courant == 1): 
                      print("Cette décision t'amène à apercevoir assez rapidement des randonneur, réussi à les rejoindres, mais il ne parle pas le français ni l'anglais. Heureusement pour toi, ils ont compris que tu avait besoin d'aides et t'on aider à ton secours.")
                      print("Félicitation ! tu as réussi a t'en sortir! Bien jouer !")
                 elif (choix_courant == 2):
                      print("Une longue marche inattendu est arriver, heureusement l'eau de la rivière est excellente. Par contre, tu commence à avoir faim. un peu plus tard, tu apperçois ce que tu pense qui est des baies sauvages. En prens tu?")

                      baie = "Si oui , ecrit 1"
                      pas_baie = "Si non, ecrit 2"
                      choix_baies = le_choix(baie, pas_baie, "", "")
                      
                      if (choix_baies == 1):
                           print("Mais quel mauvais choix! La première règle en survie est de ne rien manger, surtout des fruits sauvages, sans être sur qu'ils ne sont pas toxic! Tu n'a jamais regarder le film Hunger Games ?!")
                           print("Après cette erreur, tu fais un intoxication alimentaire et meurt en quelque minute. La partie est terminé pout toi.")
                      
                      elif(choix_baies == 2):
                           print("Bon choix ! On n'ait jamais sur si les fruits sauvages sont commestible. Il commence à ce faire tard et tu trouve un endroit parfait pour faire un feu.")
                           print("Tu dois décider avec quoi et comment faire ton abri.")

                           bon_abri = "Si tu prend des branches et des feuilles de sapin et décide de le construire en dessous d'un arbre tombé au sol, ecrit : 1"
                           mauvais_abri = "Si tu décide de le faire avec du bois et de l'écorse de bouleau et de le construire en haut tipi acoter sur un arbre, ecrit : 2"

                           choix_abri = le_choix(bon_abri, mauvais_abri, "", "")
                           if(choix_abri == 1): 
                                print("Félicitation! Tu as survécu la nuit. En plus, ton feu de hier soir à été repéré par des randonneur qui ont contacté les secours.")
                                print("Tu t'en est sorti! Bien jouer!")
                           elif(choix_abri == 2):
                                print("Tu trouvait ton abri vraiment beau et bein réussi, mais à cause de sa hauteur, tu ne gardait pas la chaleur à l'intérieur.")
                                print("C'est ainsi que tu meurt d'hypothermie. La partie est terminé pour toi.")
                      

            
            elif(choix_postdebut == 3):    
                 print("Après t'être enlevé tous tes vêtement, tu saute dans la rivière et tu réalise assez rapidement que celle-ci est très froide. Aussi, le courant est trop fort par que tu soit capable de rejoindre la terre.")
                 print("Ton petit tour de rafting ce transforme rapidement en voyage avec Jack Dawson, la partie est terminé pour toi.") 

        elif (choix_debut == 2) : 
            print("Après une courte marche, tu apperçoit un village. Soulagé et certain d'être secourus, tu rentre dans le village, mais remarque qu'il s,agit d'une tribu.")
            
            fuir_tribu = "Si tu ne veux pas te mêler à cette tribu inconnue, sachant que ça peux être dangereux, ecrit :1"
            entre_tribu = "si ta curiosité de l'inconnue est plus grande que ta peur du danger possible, ecrit : 2"
            choix_tribu = le_choix(fuir_tribu,entre_tribu,"","")
            if(choix_tribu == 1):
                 print("En esseyant de retourner sur tes pas, tu tombe dans un de leur pièges mortelle.")
                 print("La partie est terminer, mais tu as retrouver ton ami! Bon repos")
            elif(choix_tribu == 2): 
                 print("En entrant dans la tribu, plusieurs des habitants te prennes et t'ammène à leur chef. Celui-ci parlant une langue étrangère, tu ne compris rien de ce qu'il disait.")
                 print("Malgré tout, celui-ci décida de t'épargner et tu décida de rester parmi eux. Tu t'impregna leur culture et les habitants commencent à te venéré, pensant que tu est un cadeau du ciel.")
                 print("Félicitation! Tu est maintenant un dieux aux yeux de certains. Tu as réussi! Bien jouer. ")

        elif (choix_debut == 3):
            print("")
        
        elif (choix_debut == 4): 
             print("")

    elif(choix_postsoin == 2):
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
    
    elif (choix_debut == 4):
         print("")

elif (choix_un == 3):
    print("En vérifiant son poux, tu confirme le décès de ton meilleur ami. Tu dois tout de même faire un choix pour la suite.")
    
    good= "Si tu veux commencé à avancer puisque tu pense que t'a survie est plus importante pour l'instant, écrit : 1"
    triste= "Tu n'encaisse pas le décès de ton ami et tu trouve injuste que tu soit toujours vivant. Si tu veux pleuré et rejoindre ton ami, écrit : 2"
    choix_postdeces = le_choix(good,triste,"","")
    
    if(choix_postdeces == 1): 
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
    
        elif (choix_debut == 4):
            print("")
            
    elif(choix_postdeces == 2):
        print("La partie est terminer, mais tu as retrouver ton ami! Bon repos")
"""
Vincent Goulet
 
Fichier principale projet livre interactif

"""

print("Ton ami vien d'avoir sa licence de pilote d'avion et vous décidez de partir avec son avion qu'il vient de construire. Tout à coup, une tempête vous prend par surprise et vous vous écrasez dans le milieu d'une forêt. Tu t'en es bien sorti mais ton ami est inconscient.")

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
    descision = int(input("Choisisez une option:"))
    if(le_choix != choix_1 and le_choix !=choix_2 and le_choix !=choix_3 and le_choix !=choix_4):
        print("euh, non! tu ne peux pas faire cela. Bye Bye!")
    
    return descision

soin = "Si tu veux chercher l'avion en espérant trouver du soin à ton ami, écrit : 1"
mauvais_chum = "Si tu décides de partir et laisser ton ami dans l'avion parce que tu es le pire des amis, écrit : 2"
espoire  = "Si tu décides de vérifier son pouls avant toute manoeuvre de réanimation, écrit : 3"
print("Qu'allez-vous faires?")
choix_un = le_choix(soin, mauvais_chum, espoire,"")

if (choix_un == 1 ) :
    print("Tu trouves une trousse de premiers soins dans un des compartriments et réussis à soigner la blessure de ton ami. 10 minutes passent et ton ami n'est toujours pas réveillé.")

    good = "Si tu veux commencer à t'aventurer dans la forêt, écrit : 1"
    bad = "Si tu veux rester avec ton ami et le rejoindre dans les cieux, écrit : 2"
    print("Qu'allez-vous faires ?")
    choix_postsoin = le_choix(good, bad, "", "")

    if(choix_postsoin == 1):
        print("Avant de commencer la marche, tu as réussi à trouver une boussole et une bouteille d'eau dans l'avion. Tu dois décider maintenant dans quelle direction te diriger.")

        nord = "Si tu veux te diriger vers le nord, puisque c'est plus simple d'utiliser la boussole ainsi, écrit : 1"
        est = "Si tu prens la décision de te diriger vers l'ouest puisque tu avais apercu un village sur le chemin, écrit : 2"
        sud = "Si tu te dis vouloir aller vers le sud puisque tu es à bout des températures du Canada et espères avoir plus chaud, écrit : 3"
        ouest = "Si tu décides de te dirgier vers l'est puisque c'était vers cette direction que vous vous dirigiez avant le crash, écrit : 4"
        choix_debut = le_choix(nord, est, sud, ouest)
        
        if (choix_debut == 1 ) : 
            print("Cool! Tu trouves une rivière au moment que ta gourde est vide. Que fais-tu ?")

            gourde_un = "Si tu veux remplir ta gourde et faire une pause pour en boire, écrit : 1"
            gourde_deux= "Si tu veux remplir ta gourde mais continuer ton chemin sans la boire tout de suite, écrit : 2"
            baignade = "Si tu veux prendre le temps de te baigner puisque tu commences à avoir chaud, écrit: 3"
            choix_postdebut = le_choix(gourde_un, gourde_deux, baignade,"")
            
            if (choix_postdebut == 1):
                 print("Tu es fier de ta décision puisque c'était la meilleure eau que tu n'as jamais bu. Tu trouves qu'il fait chaud donc tu te trempes les pieds dans l'eau. L'eau est très bonne, tellement que tu ne te rens pas compte de ce qui se passait sur tes jambes...")
                 print("Oups... Des sangsues ont eu le temps de prendre tout ton sang.")
                 print("La partie est terminée, mais tu as retrouvé ton ami! Bon repos")
                 

            elif(choix_postdebut == 2 ) :
                 print("Maintenant, deux choix s'offrent à toi.")  

                 courant = "Soit suivre le sens du courant, écrit : 1"
                 invers_courant = "Soit suivre le sens inverse du courant, écrit : 2"
                 choix_courant = le_choix (courant, invers_courant, "", "")

                 if (choix_courant == 1): 
                      print("Cette décision t'ammène à apercevoir assez rapidement des randonneurs, réussi à les rejoindre, mais ils ne parlent pas français ni anglais. Heureusement pour toi, ils ont compris que tu avais besoin d'aide et sont venus à ton secours.")
                      print("Félicitations ! tu as réussi a t'en sortir! Bien joué !")
                 
                 elif (choix_courant == 2):
                      print("Une longue marche innattendue est arrivée, heureusement l'eau de la rivière est excellente. Par contre, tu commences à avoir faim. Un peu plus tard, tu penses aperçevoir des baies sauvages. En prends-tu?")

                      baie = "Si oui , écrit 1"
                      pas_baie = "Si non, écrit 2"
                      choix_baies = le_choix(baie, pas_baie, "", "")
                      
                      if (choix_baies == 1):
                           print("Mais quel mauvais choix! La première règle en survie est de ne rien manger, surtout des fruits sauvages, sans être sûr qu'ils ne sont pas toxiques! Tu n'as jamais regardé le film Hunger Games ?!")
                           print("Après cet erreur, tu fais une intoxication alimentaire et meures en quelques minutes. La partie est terminée pour toi.")
                      
                      elif(choix_baies == 2):
                           print("Bon choix ! On n'est jamais sûr si les fruits sauvages sont commestibles. Il commence à se faire tard et tu trouves un endroit parfait pour faire un feu.")
                           print("Tu dois décider avec quoi et comment faire ton abri.")

                           bon_abri = "Si tu prends des branches et des feuilles de sapin et décides de le construire en dessous d'un arbre tombé au sol, écrit : 1"
                           mauvais_abri = "Si tu décides de le faire avec du bois et de l'écorse de bouleau et de le construire en un grand tipi appuyé sur un arbre, écrit : 2"
                           choix_abri = le_choix(bon_abri, mauvais_abri, "", "")
                           
                           if(choix_abri == 1): 
                                print("Félicitations! Tu as survécu la nuit. En plus, ton feu d'hier soir à été repéré par des randonneurs qui ont contacté les secours.")
                                print("Tu t'en es sorti! Bien joué!")
                           
                           elif(choix_abri == 2):
                                print("Tu trouvais ton abri vraiment beau et bien réussi, mais à cause de sa hauteur, tu ne gardais pas la chaleur à l'intérieur.")
                                print("C'est ainsi que tu meures d'hypothermie. La partie est terminée pour toi.")
                      

            
            elif(choix_postdebut == 3):    
                 print("Après avoir enlevé tous tes vêtements, tu sautes dans la rivière et tu réalises assez rapidement que celle-ci est très froide. Aussi, le courant est trop fort pour que tu sois capable de rejoindre la terre.")
                 print("Ton petit tour de rafting se transforme rapidement en voyage avec Jack Dawson, la partie est terminée pour toi.") 

        elif (choix_debut == 2) : 
            print("Après une courte marche, tu apperçois un village. Soulagé et certain d'être secouru, tu entres dans le village, mais remarque qu'il s'agit d'une tribu.")
            
            fuir_tribu = "Si tu ne veux pas te mêler à cette tribu inconnue, sachant que ça peut être dangereux, écrit :1"
            entre_tribu = "si ta curiosité de l'inconnu est plus grande que ta peur du danger possible, écrit : 2"
            choix_tribu = le_choix(fuir_tribu,entre_tribu,"","")
            
            if(choix_tribu == 1):
                 print("En essayant de retourner sur tes pas, tu tombes dans un de leurs pièges mortels.")
                 print("La partie est terminée, mais tu as retrouvé ton ami! Bon repos")
            
            elif(choix_tribu == 2): 
                 print("En entrant dans la tribu, plusieurs des habitants te prennent et t'emmènent à leur chef. Celui-ci parlant une langue étrangère, tu comprends rien de ce qu'il dit.")
                 print("Malgré tout, celui-ci décida de t'épargner et tu décidas de rester parmi eux. Tu t'impregnes de leur culture et les habitants commencent à te venérer, pensant que tu es un cadeau du ciel.")
                 print("Félicitations! Tu es maintenant un Dieu aux yeux de certains. Tu as réussi! Bien joué. ")

        elif (choix_debut == 3):
            print("Après quelques heures de marche, le soleil est sur le point de se coucher et tu trouves l'entrée d'une grotte au pied d'une montagne. Que fais-tu ?")

            entrer = "Si tu veux entrer dans la grotte afin de te réchauffer et de povoir dormir, écrit : 1"
            monter = "Si tu préfères grimper la montagne en espérant voir un chemin plus clair, écrit : 2"
            choix_montagne = le_choix(entrer, monter, "", "")

            if(choix_montagne == 1):
                 print("Le début de la grotte n'avait rien d'inquiétant, donc tu continues à avancer, mais tu tombes rapidement sur un grizzly qui te vois comme une bonne pointe de pizza.")
                 print("La partie est terminée pour toi, mais au moins tu as suffit au plaisir du grizzly!")
            
            elif(choix_montagne == 2):
                 print("Ta randonnée s'est bien passée, tu as atteint le haut de la montagne. tu as une superbe vue sur le coucher de soleil et en admirant le beau paysage, tu apperçois un hélicoptère.")
                 print("Par chance, celui-ci te remarque et comprend que tu as besoin d'aide. Il appelle donc les secours et tu as été sauvé.")
                 print("Félicitaions! Tu as été secouru. Bien joué !")    

        
        elif (choix_debut == 4): 
             print("Après de longues heures de marche, tu apperçois une petite maison de campagne. Tu frappes à la porte en espérant te faire répondre, mais tu t'évanouis de fatigue.")
             print("À ton réveil, le couple possédant la maison était à tes côtés et au téléphone avec les secours.")
             print("Félicitations! Tu as réussi à survivre! Bien joué !")

    elif(choix_postsoin == 2):
        print("La partie est terminée, mais tu as retrouvé ton ami! Bon repos")

elif (choix_un == 2):
    print("Avant de commencer la marche, tu as réussi à trouver une boussole et une bouteille d'eau dans l'avion. Tu dois décider maintenant dans quelle direction te diriger.")
    
    nord = "Si tu veux te diriger vers le nord, puisque c'est plus simple d'utiliser la boussole ainsi, écrit : 1"
    est = "Si tu décides de te dirgier vers l'est puisque c'était vers cette direction que vous vous dirigiez avant le crash, écrit : 2"
    sud = "Si tu te dis vouloir aller vers le sud puisque tu es à bout des températures du canada et espères avoir plus chaud, écrit : 3"
    ouest = "Si tu prends la décision de te diriger vers l'ouest puisque tu avais apercu un village sur le chemin, écrit : 4"
    choix_debut = le_choix( nord, est, sud, ouest)
    
    

elif (choix_un == 3):
    print("En vérifiant son pouls, tu confirme le décès de ton meilleur ami. Tu dois tout de même faire un choix pour la suite.")
    
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
            print("Cool! Tu trouves une rivière au moment que ta gourde est vide. Que fais-tu ?")

            gourde_un = "Si tu veux remplir ta gourde et faire une pause pour en boire, écrit : 1"
            gourde_deux= "Si tu veux remplir ta gourde mais continuer ton chemin sans la boire tout de suite, écrit : 2"
            baignade = "Si tu veux prendre le temps de te baigner puisque tu commences à avoir chaud, écrit: 3"
            choix_postdebut = le_choix(gourde_un, gourde_deux, baignade,"")
            
            if (choix_postdebut == 1):
                 print("Tu es fier de ta décision puisque c'était la meilleure eau que tu n'as jamais bu. Tu trouves qu'il fait chaud donc tu te trempes les pieds dans l'eau. L'eau est très bonne, tellement que tu ne te rens pas compte de ce qui se passait sur tes jambes...")
                 print("Oups... Des sangsues ont eu le temps de prendre tout ton sang.")
                 print("La partie est terminée, mais tu as retrouvé ton ami! Bon repos")
                 

            elif(choix_postdebut == 2 ) :
                 print("Maintenant, deux choix s'offrent à toi.")  

                 courant = "Soit suivre le sens du courant, écrit : 1"
                 invers_courant = "Soit suivre le sens inverse du courant, écrit : 2"
                 choix_courant = le_choix (courant, invers_courant, "", "")

                 if (choix_courant == 1): 
                      print("Cette décision t'ammène à apercevoir assez rapidement des randonneurs, réussi à les rejoindre, mais ils ne parlent pas français ni anglais. Heureusement pour toi, ils ont compris que tu avais besoin d'aide et sont venus à ton secours.")
                      print("Félicitations ! tu as réussi a t'en sortir! Bien joué !")
                 
                 elif (choix_courant == 2):
                      print("Une longue marche innattendue est arrivée, heureusement l'eau de la rivière est excellente. Par contre, tu commences à avoir faim. Un peu plus tard, tu penses aperçevoir des baies sauvages. En prends-tu?")

                      baie = "Si oui , écrit 1"
                      pas_baie = "Si non, écrit 2"
                      choix_baies = le_choix(baie, pas_baie, "", "")
                      
                      if (choix_baies == 1):
                           print("Mais quel mauvais choix! La première règle en survie est de ne rien manger, surtout des fruits sauvages, sans être sûr qu'ils ne sont pas toxiques! Tu n'as jamais regardé le film Hunger Games ?!")
                           print("Après cet erreur, tu fais une intoxication alimentaire et meures en quelques minutes. La partie est terminée pour toi.")
                      
                      elif(choix_baies == 2):
                           print("Bon choix ! On n'est jamais sûr si les fruits sauvages sont commestibles. Il commence à se faire tard et tu trouves un endroit parfait pour faire un feu.")
                           print("Tu dois décider avec quoi et comment faire ton abri.")

                           bon_abri = "Si tu prends des branches et des feuilles de sapin et décides de le construire en dessous d'un arbre tombé au sol, écrit : 1"
                           mauvais_abri = "Si tu décides de le faire avec du bois et de l'écorse de bouleau et de le construire en un grand tipi appuyé sur un arbre, écrit : 2"
                           choix_abri = le_choix(bon_abri, mauvais_abri, "", "")
                           
                           if(choix_abri == 1): 
                                print("Félicitations! Tu as survécu la nuit. En plus, ton feu d'hier soir à été repéré par des randonneurs qui ont contacté les secours.")
                                print("Tu t'en es sorti! Bien joué!")
                           
                           elif(choix_abri == 2):
                                print("Tu trouvais ton abri vraiment beau et bien réussi, mais à cause de sa hauteur, tu ne gardais pas la chaleur à l'intérieur.")
                                print("C'est ainsi que tu meures d'hypothermie. La partie est terminée pour toi.")
                      

            
            elif(choix_postdebut == 3):    
                 print("Après avoir enlevé tous tes vêtements, tu sautes dans la rivière et tu réalises assez rapidement que celle-ci est très froide. Aussi, le courant est trop fort pour que tu sois capable de rejoindre la terre.")
                 print("Ton petit tour de rafting se transforme rapidement en voyage avec Jack Dawson, la partie est terminée pour toi.") 

        elif (choix_debut == 2) : 
            print("Après une courte marche, tu apperçois un village. Soulagé et certain d'être secouru, tu entres dans le village, mais remarque qu'il s'agit d'une tribu.")
            
            fuir_tribu = "Si tu ne veux pas te mêler à cette tribu inconnue, sachant que ça peut être dangereux, écrit :1"
            entre_tribu = "si ta curiosité de l'inconnu est plus grande que ta peur du danger possible, écrit : 2"
            choix_tribu = le_choix(fuir_tribu,entre_tribu,"","")
            
            if(choix_tribu == 1):
                 print("En essayant de retourner sur tes pas, tu tombes dans un de leurs pièges mortels.")
                 print("La partie est terminée, mais tu as retrouvé ton ami! Bon repos")
            
            elif(choix_tribu == 2): 
                 print("En entrant dans la tribu, plusieurs des habitants te prennent et t'emmènent à leur chef. Celui-ci parlant une langue étrangère, tu comprends rien de ce qu'il dit.")
                 print("Malgré tout, celui-ci décida de t'épargner et tu décidas de rester parmi eux. Tu t'impregnes de leur culture et les habitants commencent à te venérer, pensant que tu es un cadeau du ciel.")
                 print("Félicitations! Tu es maintenant un Dieu aux yeux de certains. Tu as réussi! Bien joué. ")

        elif (choix_debut == 3):
            print("Après quelques heures de marche, le soleil est sur le point de se coucher et tu trouves l'entrée d'une grotte au pied d'une montagne. Que fais-tu ?")

            entrer = "Si tu veux entrer dans la grotte afin de te réchauffer et de povoir dormir, écrit : 1"
            monter = "Si tu préfères grimper la montagne en espérant voir un chemin plus clair, écrit : 2"
            choix_montagne = le_choix(entrer, monter, "", "")

            if(choix_montagne == 1):
                 print("Le début de la grotte n'avait rien d'inquiétant, donc tu continues à avancer, mais tu tombes rapidement sur un grizzly qui te vois comme une bonne pointe de pizza.")
                 print("La partie est terminée pour toi, mais au moins tu as suffit au plaisir du grizzly!")
            
            elif(choix_montagne == 2):
                 print("Ta randonnée s'est bien passée, tu as atteint le haut de la montagne. tu as une superbe vue sur le coucher de soleil et en admirant le beau paysage, tu apperçois un hélicoptère.")
                 print("Par chance, celui-ci te remarque et comprend que tu as besoin d'aide. Il appelle donc les secours et tu as été sauvé.")
                 print("Félicitaions! Tu as été secouru. Bien joué !")    

        
        elif (choix_debut == 4): 
             print("Après de longues heures de marche, tu apperçois une petite maison de campagne. Tu frappes à la porte en espérant te faire répondre, mais tu t'évanouis de fatigue.")
             print("À ton réveil, le couple possédant la maison était à tes côtés et au téléphone avec les secours.")
             print("Félicitations! Tu as réussi à survivre! Bien joué !")
            
    elif(choix_postdeces == 2):
        print("La partie est terminer, mais tu as retrouver ton ami! Bon repos")
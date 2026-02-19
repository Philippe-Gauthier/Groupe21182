""""
Nom = Karaboue
Prénom = Médjoua
Groupe = 21182
Projet1
Cours : 243-224-SH
"""



def trouver_reponse(Question, choix1, choix2, choix3,) : 
 """
 la fonction definie permet d'afficher, la question, le choix 1, choix 2, choix 3, 
 la decision, la condition if decision permet de proteger le choix des reponse qui est compris entre (1, 2, 3) 
 sinon "else" pour afficher "fin du jeu" lorsqu'il ne choisit pas entre les trois choix de reponse.
 return permet d'afficher en retour la decision
  """
 print("\n" + Question)
 print("---------------------------------")
 print(f"1: {choix1}")
 print(f"2: {choix2}")
 print(f"3: {choix3}") 
 decision = input("Veuillez choisir votre reponse :")
 if decision in ("1","2","3"):
    return int(decision)
 else:
  print ("Fin du jeu")

 return decision

reponse = trouver_reponse("Quelle est l unité de la courant électrique ?", "Ampère", "Volt", "Ohm ")
if reponse == 1:
   print("bonne reponse")
   reponse = trouver_reponse("Quel outil permet de mesurer le courant électrique?", "Multimètre", "Voltmètre", "Wattmètre")
   if reponse == 1:
      print("bonne reponse")
      reponse = trouver_reponse("Quelle est l unité du courant électrique ?", "watt", "Ohm", "Ampère")
      if reponse == 3:
           print("bonne reponse")
           reponse = trouver_reponse("Quelle est la formule pour calculer  le courant électrique  ?", "I=U/R", "P=R*2I", "V=XC*I")
           if reponse == 1:
              print("bonne reponse")
              reponse = ("Quel Metaux  produit du courant électrique correctement ?", "le fer", "L'étain", "le cuivre")
              if reponse == 3:
                print("bonne reponse")
                reponse = trouver_reponse("le courant est il meme dans un circuit serie ?", "oui", "non", "passe")
                if reponse == 1:
                   print("bonne reponse")
                   reponse =  trouver_reponse("Dans quel sens le courant circule ?", "négative au positive", "dans le deux sens", "positive au négative")
                   if reponse == 3:
                      print ("bonne reponse")
                      reponse =  trouver_reponse("que se passe t'il si la resistance augmente ?", "le courant augmente", "le courant est nul", "le courant diminue")
                      if reponse == 3:
                         print("bonne reponse")
                         reponse = trouver_reponse("Quel type de courant une pile prend ?", "AC", "DC", "aucun")
                         if reponse == 2:
                            print("bonne reponse")
                            reponse = trouver_reponse("un courant très élévés proveque quoi?", "Échauffement", "incendie", "feux")
                            if reponse == 2:
                               print("bonne reponse")
                               print("fin")
elif reponse == 2:
     print("Mauvaise reponse")
     reponse = trouver_reponse("Qu'est ce que la tension électrique?", "difference de potentiel", "difference de valeur", "difference de niveau")
     if reponse == 1:
        print("bonne reponse")
        reponse = trouver_reponse("quel est le symbole de la tension ?", "Q", "L", "U")
        if reponse == 3:
           print("bonne reponse")
           reponse = trouver_reponse("quel est l'unité de la tension électrique ?", "Ohm", "Volt", "Henry")
           if reponse == 2:
              print("bonne reponse")
              reponse = trouver_reponse("quel appareil mesure la tension ?", "Ampèremètre", "Ohmètre", "Voltmètre")
              if reponse == 3:
                 print("bonne reponse")
                 reponse = trouver_reponse("comment branche t-on le voltmètre ?", "en serie", "en parrallèle", "mixte")
                 if reponse == 2:
                    print("bonne reponse")
                    reponse = trouver_reponse("quel élément fournie la tension dans un circuit ?", "oscilloscope", "recepteur", "generateur")
                    if reponse == 3:
                       print("bonne reponse")
                       reponse = trouver_reponse("sans tension, peut on avoir du courant ?", "non", "peut être", "oui")
                       if reponse == 1:
                          print("bonne reponse")
                          reponse = trouver_reponse("dans un circuit serie la tension total est egal à quoi ?", "la somme des tensions", "la soustraction des tensions", "la division des courants")
                          if reponse == 1:
                             print("bonne reponse")
                             reponse = trouver_reponse("dans un circuit parallèle la tension est ?", "même", "different", "soustraire")
                             if reponse == 1:
                                print("bonne reponse")
                                reponse = trouver_reponse("la tension aux bornes d'une pile est appélée", "tension du recepteur", "tension du generateur", "tension de la pile")
                                if reponse == 2:
                                   print("bonne reponse")
                                   print ("fin")
elif reponse == 3:
 print("Mauvaise reponse")  
 reponse = trouver_reponse("quel est l'unité de la resistance électrique ?","Hertz", "Ampère", "Ohm")
 if reponse == 3:
    print("bonne reponse")
    reponse = trouver_reponse("Quel est le symbole qui represente la resistance ?","U", "R", "L")
    if reponse == 2:
       print("bonne reponse")
       reponse = trouver_reponse("quel est la formule qui correspond à la loi d'ohm ?", "U=R*I", "I=U/R", "R=U*I")
       if reponse == 1:
         print("bonne reponse")
         reponse = trouver_reponse("si la resistance augmente ?", "le courant diminue", "le courant augmente", "le courant est constante")
         if reponse == 1:
           print("bonne reponse")
           reponse = trouver_reponse("quel composant sert à limiter le courant dans un circuit ?", "le condensateur", "la diode", "la resistance")
           if reponse == 3:
              print("bonne reponse")
              reponse = trouver_reponse("quel formule permet de calculer la resistance", "R=U/I ", "R=I/U", "R=U*I2")
              if reponse == 1:
               print("bonne reponse")  
               print("fin")                           



       

                             



                    
  

 
 

     
          
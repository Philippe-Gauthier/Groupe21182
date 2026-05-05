questions = ["2+2=? ", "12/6=? ", "14-4=? "]

for element in questions:
    choix = input("enrez votre reponse:")
    fichier = open("test.txt" , "a")
    fichier.write(choix)
    fichier.close()








 
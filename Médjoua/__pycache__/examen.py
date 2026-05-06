"""
questions = ["2+2=? ", "12/6=? ", "14-4=? "]

for element in questions:
    choix = input("enrez votre reponse:")
    fichier = open("test.txt" , "a")
    fichier.write(choix)
    fichier.close()
"""

from Questions import questions, reponses

for i in questions:
    choix = input(f"Question{1}: {i} ")
    fichier = open("reponse_etudiant.txt" , "a")
    fichier.write(choix + "\n")
    fichier.close()

   







 
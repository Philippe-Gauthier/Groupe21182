"""
Code par: Tommy Brunelle
Ce fichier contient le code pour la partie correction de l'examen. 
"""
import Tommy.pratique_exam_01.questions as questions

# Compteur de bonnes reponses
points = 0
# Compte le nombre delements dans la liste
total = len(questions.reponses)

verification = open("resultats.txt", "r")
validation = verification.readline() # Validation est maintenant une string 4 2 10
verification.close()

# split() divise la string en liste selon les espaces
resultats = validation.split()
# resultats = ['4', '2', '10']

for i in range(total): # range(3) → i prend les valeurs 0, 1, 2
    if resultats[i] == questions.reponses[i]:
        points += 1

print(f"{points}/{total}")

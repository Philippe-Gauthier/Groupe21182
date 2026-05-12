"""
Code par: Tommy Brunelle
Ce fichier contient le code pour la demande de questions de l'examen
"""
import Tommy.pratique_exam_01.questions as questions

# Future liste de réponses de l'étudiant.e
hypothese = []

for element in questions.questions:
    essai = input(element)
    hypothese.append(essai)

def stocker_reponses(hypothese):
    """
    But: Noter les reponses dans un fichier externe
    Entree: La liste de la variable hypothese
    Sortie: Aucune
    """
    resultats = open("resultats.txt", "w")
    resultats.write(hypothese[0] + " " + hypothese[1] + " " + hypothese[2])

stocker_reponses(hypothese)


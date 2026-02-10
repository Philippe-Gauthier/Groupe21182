""""
Cassey Martin

Fichier principale projet livre interactif
"""

"""
Structure en arbre
Rappel: Aucune boucle permise.

Trier par des lists en rangée pour le texte afficher
(Incluant la question)
Montrer les choix possibles, organiser en rangé aussi(associer aux lignes)

Docstring doivent etre écrits pour chaque fonction, et pour le projet en général:
Entrées: 
Sorties:
But:

"""
#tuples are ordered and unchangeable, lists are ordered and changeable, sets are unordered and unindexed, dictionaries are unordered, changeable and indexed
introduction = "Un papillon vole dans la forêt, il est heureux et libre. Ensuite, que fais-t-il?"
nombere_ranger = int(5)
choix_ranger_un = tuple("Il va dormir","Il va manger des fleurs","Il va rencontrer d'autres papillons") #3
texte_ranger_un = () #3
choix_ranger_deux = () 
texte_ranger_deux = () #6
choix_ranger_trois = () 
texte_ranger_trois = () #12
choix_ranger_quatre = ()
texte_ranger_quatre = () #24

#Reste une list
choix_afficher = []
texte_afficher = str("")
question_afficher = str("")

commande = int(0)

#TODO: Trier les lists pour obtenir seulement les éléments nécessaires à afficher, et les afficher
def trier_texte_afficher():
    return 0

#TODO: Trier les lists pour obtenir seulement les éléments nécessaires à afficher, et les afficher
def trier_choix_afficher():
    return 0

#TODO: Idéalement, trier les lists pour obtenir la question separement du texte, et les afficher
def separer_texte_question():
    return 0

"""
Entrées: Rien
Sorties: String dans le terminal
But: Obtenir facilement une cohérence dans les sauts de ligne pour séparer les différentes sections du texte, question et choix
"""
def print_saut_ligne():
    print("-------------------------------------------------------------------------------------------------------------------")

"""
Entrées: choix_afficher, texte_afficher, question_afficher
Sorties: String dans le terminal
But: Afficher le texte, la question, les choix possibles et l'instruction de manière claire et bien formatté pour le lecteur
But futur: Manipuler les listes pour afficher seulement les éléments nécessaires, et les afficher de manière claire pour le lecteur
"""
def print_final():
    global choix_afficher, texte_afficher, question_afficher
    print_saut_ligne()
    print(f"Texte: {texte_afficher}")
    print_saut_ligne()
    print(f"Question: {question_afficher}")
    print_saut_ligne()
    i = 0
    len_choix = len(choix_afficher)
    if i < len_choix:
        choix_x_visible = choix_afficher[i]
        print(f"Choix {i+1}: {choix_x_visible}")
        i += 1
    print_saut_ligne()
    print("Entrez le numéro de votre choix pour continuer l'histoire.")
    print_saut_ligne()

commande = int(input(print_final())) #input attend avant de se reéexecuter

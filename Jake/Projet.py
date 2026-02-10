"""



Jacob Chagnon

Fichier principal projet livre interactif



"""
""" 
Entree : les choix (texte)
Sortie : option choisie (texte)
But : Demander au lecteur de faire un choix
"""



def choisir_option(choix_1, choix_2):
    print("************************************")
    print(f"1: {choix_1}")
    print(f"2: {choix_2}")

    decision = (input)
    return  decision


# Début du jeu
choix_1 = print()
choix_2 = print("L'aventure se termine avant d'avoir commencé.")
choisir_option(choix_1, choix_2)



print("Un mur d'arbres se dresse devant toi. Les épines de conifères s'étendent jusqu'à l'horizon, et ce, de chaque côté.")
print("Une affiche à l'orée de la forêt te prévient que tu es sur le point de passer sur un terrain privé, mais une voix tente de t'attirer vers l'intérieur.")
print("Que fais-tu?")

choisir_option(choix_1, choix_2)
choice = input("Tu t'avances vers la forêt (1) ou tu t`éloignes (2)")
if choice == 2: 
    print("L'aventure se termine avant d'avoir commencé.")
if choice == 1:
    print("Les feuilles craquent sous tes pieds. La voix se fait rassurante; comme un petit frère qui essaie d'avoir ton attention. ")


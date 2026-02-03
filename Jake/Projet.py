"""



Jacob Chagnon

Fichier principal projet livre interactif



"""
# Début du jeu
print("Un mur d'arbre se dresse devant toi. Les épines de conifères s'étendent jusqu'à l'horizon, et ce, de chaque côté.")
print("Une affiche à l'orée de la forêt te prévient que tu es sur le point de passer sur un terrain privé, mais une voix tente de t'attirer vers l'intérieur. Que fais-tu?")
# premier choix
# mauvais choix
choice = input("Tu t'avances vers la forêt (F) ou tu t`éloignes (E)")
if choice == "E":
    print("Ton aventure se termine avant même d'avoir débuté. L'histoire oublie ton nom.")
    print("GAME OVER")
# bon choix
if choice == "F":
    print("")
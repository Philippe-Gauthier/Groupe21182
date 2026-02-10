"""
Vincent Goulet
 
Fichier principale projet livre interactif

"""

print("Ton ami viens d'avoir sa liscence de pilote d'avion et vous décidé de partir avec son avion qu'il vient de construire. Tout à coup, une tempête vous prend par surprise et vous vous écraser dans le milieu d'une forêt. Tu t'en est bien sorti mais ton ami est inconcient.")

def premier_choix(choix_1, choix_2, choix_3,) :
    """
    Entrée : les trois choix (texte)
    Sortie : choix décider (entier)
    But : Demander à l'utilisateur quel action faire
    """
    print(f"1: {choix_1}")
    print(f"2: {choix_2}")
    print(f"3: {choix_3}")
    descision = int(input("Choisisez une option: "))

    return descision

soin = "Si tu veux chercher l'avion en esperant trouver du soin à ton ami, écrit : 1"
choix_200 = "Si tu décide de partir et laisser ton ami dans l'avion parce que tu est le pire des amis, écrit : 2"
choix_300 = "Si tu décide de vérifier son poux avant toute maneuvre de réanimation, écrit : 3"

print("Qu'allez-vous faires?")

choix_utilisateur =premier_choix(soin, choix_200, choix_300)

if (choix_utilisateur == 1 ) :
    print("Tu trouve une trousse de premier soin dans un des compariment et réussi à soigner la blessure de ton ami. 10 min passe et ton ami n'est toujour pas réveillé.")
    



import math

hypothenuse = input("Entrez la distance d'un trajet en ligne droite: ")
oppose = input("Entrez la distance de la derive du au courant: ")

adjacent = math.sqrt(((int(hypothenuse)**2) - ((int(oppose))**2)))
adjacent = math.ceil(adjacent)

print(adjacent)


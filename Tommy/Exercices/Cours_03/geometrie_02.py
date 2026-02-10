def calculer_aire_cercle(rayon):
    aire = 3.1416 * rayon ** 2
    return aire

def calculer_aire_triangle(base, hauteur):
    aire = base * hauteur / 2
    return aire

def calculer_aire_carre(cote):
    aire = cote ** 2
    return aire

def calculer_volume_pyramide(aire_base, hauteur):
    volume = aire_base * hauteur / 3
    return volume

def calculer_volume_cone(rayon, hauteur):
    return calculer_volume_pyramide(calculer_aire_cercle(rayon),hauteur)


# Je veux calculer le volume dun cone, r=4, h=5
print(calculer_volume_pyramide(calculer_aire_cercle(4),5))

#exemple pour projet livre
page = int(input("Quelle page"))
print(calculer_aire_cercle(page))

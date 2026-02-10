def calculer_aire_cercle(rayon):
    aire = 3.1416 * rayon ** 2
    return aire

def calculer_aire_triangle(base, hauteur):
    aire = base * hauteur / 2
    return aire

aire_cercle = calculer_aire_cercle(5)
aire_totale = calculer_aire_cercle(3) + calculer_aire_triangle(5,2)

print(aire_cercle, aire_totale)
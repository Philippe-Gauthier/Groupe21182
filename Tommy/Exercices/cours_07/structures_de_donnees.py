joueurs = []

joueur_a = {
    "nom" : "ALice",
    "points" : 3,
}

joueur_b = {
    "nom" : "bob",
    "points" : 2,
}

joueurs.append(joueur_a)
joueurs.append(joueur_b)
points = 0

for joueur in joueurs:
    points += joueur["points"]

print(points)

for cle, valeur in joueur_a.items():
    print(cle, valeur)


garde = {
    "nom" : "Roger",
    "hp" : 50,
    "force" : 20,
    "arme" : "Hache",
}

print("Le", garde["nom"], "attaque avec sa", garde["arme"])

garde["hp"] -= 5
garde["Vivant"] = True

for cle, valeur in garde.items():
    
    print(cle, valeur)
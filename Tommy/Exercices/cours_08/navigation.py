coordonnee_x = input("Entrez des coordonnees (x): ")
coordonnee_y = input("Entrez des coordonnees (y): ")

fichier = open("route.txt", "a") #a pour Append (ajout).
fichier.write(f"{coordonnee_x}, {coordonnee_y} \n")
fichier.close()

fichier = open("route.txt", "r") #r pour lecture
contenu = fichier.read()
fichier.close()
print(contenu)
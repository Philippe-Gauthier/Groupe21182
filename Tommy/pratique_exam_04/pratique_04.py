import catalogue

fichier = open("stock.txt", "r", encoding="utf-8")
stock = fichier.readlines() # Une liste de lignes [A101\n, B202\n, A103\, etc]
#read() --> une longue string A101\nB202\n etc
fichier.close()

noms_articles = ""

for element in stock:
    element = element.strip()  # enlève le \n
    if element in catalogue.dictionnaire_decodage:
        noms_articles += catalogue.dictionnaire_decodage[element] + "\n"
    else:
        noms_articles += "Article inexistant\n"

print(noms_articles)

ajout = input("nouvel article a ajouter: ")

# convertir le nom en code
if ajout in catalogue.dictionnaire_encodage:
    code = catalogue.dictionnaire_encodage[ajout]
else:
    code = "Article inexistant"

# stocker dans un nouveau fichier
fichier = open("nouveau_stock.txt", "w", encoding="utf-8")
fichier.write(code + "\n")
fichier.close()

print("Nouveau code enregistré :", code)



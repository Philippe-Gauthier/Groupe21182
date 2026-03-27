import json

routeur = {"modele": "RB750Gr3", "ip": "192.168.88.1", "ports_actifs": [1, 2, 4]}

fichier = open("mikrotik.json", "w")
json.dump(routeur, fichier)
fichier.close()

fichier = open("mikrotik.json", "r")

donnees_chargees = json.load(fichier)
print(donnees_chargees["ip"])

fichier.close()
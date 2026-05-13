import cle

# Lire le fichier.
fichier = open("message.txt", "r", encoding="utf-8")
message = fichier.read()
fichier.close()

# Décrypter
message_clair = ""

for element in message:
    if element.upper() in cle.decrypte:
        lettre = cle.decrypte[element.upper()] # cle.decrypte["Q"] → "A"
        if element.islower():
            message_clair += lettre.lower()
        else:
            message_clair += lettre
    else: # Si cest pas une lettre.
        message_clair += element

# Si je voulais les 2 elements dans le dictionnaire.
# for key, value in cle.decrypte.items():
    #print(key, value)

# Pour afficher ce que je prend dans le dictionnaire:
# for element in cle.decrypte:
    #print(element)

# Afficher
print("Message reçu : ")
print(message_clair)

# Réponse utilisateur
reponse = input("\nVotre réponse : ")

# Encrypter
reponse_codee = ""

for element in reponse:
    if element.upper() in cle.encrypte:
        lettre = cle.encrypte[element.upper()]
        if element.islower():
            reponse_codee += lettre.lower()
        else:
            reponse_codee += lettre
    else:
        reponse_codee += element

# Sauvegarder
fichier = open("reponse_03.txt", "w", encoding="utf-8")
fichier.write(reponse_codee)
fichier.close()

print("Réponse enregistrée xoxo.")
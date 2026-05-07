# Importer les clés depuis le fichier clé.py
from clé import cle_dechiffrage, cle_chiffrage


# FONCTION 1: Lire un fichier
def lire_fichier(nom_fichier):
    # Ouvrir le fichier en lecture
    f = open(nom_fichier, "r")
    # Lire tout le contenu
    contenu = f.read()
    # Fermer le fichier
    f.close()
    # Retourner ce qu'on a lu
    return contenu


# FONCTION 2: Décrypter un message
def decrypter(texte, cle):
    # Créer une variable vide pour le résultat
    resultat = ""
    
    # Pour chaque lettre du texte
    for lettre in texte:
        # Chercher la lettre dans la clé (en minuscule)
        if lettre.lower() in cle:
            # Si la lettre existe dans la clé, ajouter la lettre décryptée
            resultat = resultat + cle[lettre.lower()]
        else:
            # Si la lettre n'existe pas (espace, point, etc), garder la même
            resultat = resultat + lettre
    
    # Retourner le texte décrypté
    return resultat


# FONCTION 3: Crypter un message
def crypter(texte, cle):
    # Créer une variable vide pour le résultat
    resultat = ""
    
    # Pour chaque lettre du texte
    for lettre in texte:
        # Chercher la lettre dans la clé (en minuscule)
        if lettre.lower() in cle:
            # Si la lettre existe dans la clé, ajouter la lettre cryptée
            resultat = resultat + cle[lettre.lower()]
        else:
            # Si la lettre n'existe pas (espace, point, etc), garder la même
            resultat = resultat + lettre
    
    # Retourner le texte crypté
    return resultat


# FONCTION 4: Sauvegarder dans un fichier
def sauvegarder(texte, nom_fichier):
    # Ouvrir le fichier en écriture
    f = open(nom_fichier, "w")
    # Écrire le texte
    f.write(texte)
    # Fermer le fichier
    f.close()


# ===== PROGRAMME PRINCIPAL =====

# ÉTAPE 1: Lire le message encrypté dans le fichier
message_encrypte = lire_fichier("message.txt")
print("Message encrypté:")
print(message_encrypte)
print()

# ÉTAPE 2: Décrypter le message
message_lisible = decrypter(message_encrypte, cle_dechiffrage)
print("Message décrypté:")
print(message_lisible)
print()

# ÉTAPE 3: Demander une réponse à l'utilisateur
reponse = input("Tapez votre réponse: ")
print()

# ÉTAPE 4: Crypter la réponse
reponse_cryptee = crypter(reponse, cle_chiffrage)
print("Réponse cryptée:")
print(reponse_cryptee)
print()

# ÉTAPE 5: Sauvegarder la réponse cryptée
sauvegarder(reponse_cryptee, "reponse_encryptee.txt")
print("Réponse sauvegardée dans 'reponse_encryptee.txt'!")


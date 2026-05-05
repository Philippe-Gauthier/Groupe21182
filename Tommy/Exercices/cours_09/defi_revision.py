"""
-Prendre une string en entrée (input)
-verifier que la string contient uniquement 26 lettres de l'alphabet ou un espace
-Si cest pas le cas, on veut lever une erreur (raise error)
-Prendre chaque charactere et ajouter 13 dans l<alphabet (chiffrement de caesar) les espaces restent inchang/s
-ecrire le message encrypt/ dans un .txt

- En-tete de fichier
- en-tete de fonction
- au moins 3 fonctions differentes
- protection entree sortie (fichier, input, etc)

"""

def separer_message(message):

    # Pas obligé de fairte un set long à ecrire, on prend un string et on le met en set.
    possible = set("abcdefghijklmnopqrstuvwxyz ")

    # Pour chaque lettre dans le message, si la lettre est pas dans le set/variable "possible".
    for i in message:
        #.lower traite toutes mes lettres comme des minuscules.
        if i.lower() not in possible:
            raise ValueError(f"Le message contient des caracteres non pris en charge: {i}")
    
    return message


def encrypter_message(mots):
    # Je met pas set devant mon string pcq je veux que ce soit traité comme une liste
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Variable/string vide pour y inserer la phrase encrypté
    resultat = ""
    # Pour chaque lettre dans le mot/phrase
    for i in mots:
        # Si element = a un espace
        if i == " ":
            # AJoute un espace a la variable resultat
            resultat += " "
        # SInon (si cest une lettre)
        else:
            # .isupper verifie si la lettre est en majuscule. SI oui, TRUE et stocke l<Info, si non FALSE et stocke l<info
            majuscule = i.isupper()
            #variable minuscule force tout le mot a etre en minuscule (juste pour indexer tout)
            minuscule = i.lower()
            # Jindexe ma string alphabet et je les mets tous en minuscule
            index = alphabet.index(minuscule)
            # chaque lettre je l<Indexe de + 13
            nouvelle_lettre = alphabet[(index + 13) % 26] #modulo 26 pcq on fait exemple\
            #lettre p (15) + 13 = 28, 28 diviser 26 = 1 fois et reste 2, donc index devient 2.
            # Si majuscule, on ajoute la nouvelle lettre indexer et on force uppercase
            if majuscule:
                resultat += nouvelle_lettre.upper()
            # sinon, on ajoute nouvelle lettre indexer
            else:
                resultat += nouvelle_lettre

    return resultat

def exporter_message(phrase):
    fichier = open("messages_encryptes.txt", "w")
    fichier.write(phrase)

reponse = input("Message a transmettre: ")

try:
    message_valide = separer_message(reponse)
    message_encrypter = encrypter_message(message_valide)
    exporter_message(message_encrypter)

except ValueError as message_erreur:
    print(message_erreur)


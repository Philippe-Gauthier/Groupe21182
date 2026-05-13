"""
Philippe Gauthier
Gestionnaire d'inventaire
"""


import catalogue


def lire_fichier(nom_fichier):
    """
    - EntrÃ©e: nom du fichier Ã  lire
    - Sortie: liste de code
    - But: Lire le fichier d'inventaire
    """
    fichier = open(nom_fichier, "r")
    liste = fichier.readlines()
    fichier.close()

    return liste

def traduire_code(liste_code):
    """
    - EntrÃ©e: une liste de code
    - Sortie: une liste de noms d'article
    - But: Traduire les codes en nom d'article
    """
    liste_nom = []
    for code in liste_code:
       code = code.strip()
       liste_nom.append(catalogue.dictionnaire_decodage[code]) #decode

    return liste_nom


def imprimer_inventaire(liste_nom):
    """
    - EntrÃ©e: liste de nom
    - Sortie: Rien
    - But: Imprimer la liste de noms d'article
    """

    for nom in liste_nom:
        print(nom)

    return 


def ajout_article():
    """
    - EntrÃ©e: Rien
    - Sortie: Code de produit
    - But: Obtenir un code de produit Ã  partir de son nom
    """
    nom = input("Entrez un nom de produit: ")
    code = catalogue.dictionnaire_encodage[nom] #encode
    return code

def stocker_code(code, nom_fichier):
    """
    - EntrÃ©e: 
        - Code de produit
        - nom de fichier
    - Sortie: Rien
    - But: stocker le code dans le fichier
    """
    fichier = open(nom_fichier, "a")
    fichier.write("\n" + code )
    fichier.close()

    return

liste_encodage = lire_fichier("stock.txt")
liste_decode = traduire_code(liste_encodage)
imprimer_inventaire(liste_decode)
nouveau_article = ajout_article()
stocker_code(nouveau_article, "stock.txt")
"""
Programme pour remplacer les caractères non-autorisés par des astérisques.
"""

from caracteres import caracteres_autorises


def lire_fichier(nom_fichier):
    """
    Lit le contenu d'un fichier texte.
    
    Args:
        nom_fichier: Le nom du fichier à lire
        
    Returns:
        str: Le contenu du fichier
    """
    fichier = open(nom_fichier, "r")
    texte = fichier.read()
    fichier.close()
    return texte


def remplacer_caracteres_invalides(texte):
    """
    Remplace tous les caractères non-autorisés par des astérisques.
    
    Args:
        texte: Le texte à traiter
        
    Returns:
        tuple: (texte_modifié, nombre_remplacements)
    """
    texte_modifie = ""
    nombre_remplacements = 0
    
    for char in texte:
        if char in caracteres_autorises:
            texte_modifie += char
        else:
            texte_modifie += "*"
            nombre_remplacements += 1
    
    return texte_modifie, nombre_remplacements


def afficher_resultats(texte_modifie, nombre_remplacements):
    """
    Affiche le texte modifié et le nombre de remplacements.
    
    Args:
        texte_modifie: Le texte avec les caractères remplacés
        nombre_remplacements: Le nombre total de caractères remplacés
    """
    print("Texte modifié:")
    print(texte_modifie)
    print(f"\nNombre de caractères non-valides trouvés: {nombre_remplacements}")


if __name__ == "__main__":
    texte = lire_fichier("texte.txt")
    texte_modifie, nombre = remplacer_caracteres_invalides(texte)
    afficher_resultats(texte_modifie, nombre)
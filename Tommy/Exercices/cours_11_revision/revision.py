# Peut aller voir le document de 105 pages dans le powerpoint fournis par le prof.
# Peut aussi me preparer du code d<avance comme mettons preparer des fonctions pour lire et chercher des trucs dans des fichiers txt, csv, json.

# les inputs par defaut est tjrs un string, donc si on met input() on doit mettre int ou float
# Si on veut modifier une variable existante, doit mettre la variable de base plus haut ex debut = 0 juste pour la definir.
# dans les fonctions on peut return plus d<un truc avec la virgule ex: return 1, 2
# a, b = f() donc 1 irait dans a et 2 dans b

# eviter d<utiliser trop de variables globales
# Pour la documentation de fonctions: sortie d<Une fonction est TJRS un return, faut pas ecrire ce que ca fait.
# Pour la documentation de fonctions: S<il n<y a pas le mot return dans la fonction, ecrire aucune 'a sortie
# Pour la documentation de fonctions: entree est juste les parametres.

# // division entiere arrondi vers le bas
# & divise et affiche ce qui reste ex: 15 % 4 = 3
# ** exposant

# PEMDAS (parenthese, exposants, multi divi modulo, addi soustra)

# == egal 'a
# != pas egal

# True ou False TJRS avec la premiere majuscule.

# and or not (not inverse la condition)

# Quand on fait des if, ils sont lu dans l<ordre, donc si yen a un de vrai il lit pas les autres if, SAUF si on met des elif.

# while: repete tant qu<une condition est vraie.
# for: passer 'a travers d<une sequence delements.

# in range: for bla bla in range(start, stop, step) stop print pas le dernier donc (1, 6) print juste de 1 a 5.
# while (plus rare pour le cours), sauf projet 1.

# Dans le doute a lexam, cest probablement plus une boucle for que while.
# for blabla in sequence, blabla equivaut 'a i, cest juste pour dire for chaque elements dans sequence.

# mettre des noms de listes ou sequences au pluriel donc on peut appeler le i au singulier et cest moins melangeant.
# break dans while ca stop la boucle.
# continue ca skip lelement mais ca affiche le reste quand meme.

# else est pratique pour pas faire de break. si on a un break et un else, else sert a rien.

# Mettre une condition d<arret avec break si on est dans un WHile True quon veut pas voir looper a linfini.

# try/except, mettre un try avant un code que jai peur qui echoue et except on choisi lerreur quon veut pas qui saffiche pour continuer a run et mettre le message que je veux. On peut le mettre dans un while.

# module: cest un fichier .py quon va import dans le main pour utiliser les fonctions ou variables.
# quand on importe un module, on doit utiliser le . pour aller chercher et utiliser les variables et fonctions.

# Aller voir diapo pour noter les .append .insert etc. pour les listes.
IMPORTANT # Parcourir un dictionnaire: for cle, valeur in blabla.items(): print(f"{cle} : {valeur}")

#tuple est immuable.
# Pour faire un set, mieux decrire set exeple: a = set()

#Aller voir lecture de fichiers.

#w ecrase
#a append
#x cree (echoue si le fichier existe deja)
# Mettre des try/except quand on veut ouvrir ou lire des fichiers, voir diapo.
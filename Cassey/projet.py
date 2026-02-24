""""
Cassey Martin

Fichier principale projet livre interactif
"""

introduction = "Un papillon vole dans la forêt, il est heureux et libre. Ensuite, que fais-t-il?" 
nombre_colonne = int(5)
choix_colonne_un = ("Il se pose sur une feuille", 
                        "Il fonce dans un oiseau", 
                        "Il essaie de trouver son ami perdu") # 3 choix
texte_colonne_un = ("Pendant que le papillon dort sur une feuille, il a froid. À quel endroit va-t-il se réfugier pour se réchauffer?", 
                    "Ah non, son aile se brise! Il va voir qui pour la réparer?", 
                    "Il retrouve George, son ami d'enfance. À quel endroit va-t-il avec George?") #3 textes
choix_colonne_deux = ("Un trou dans un arbre", 
                    "Une fleur",
                    "La papillon en chef",
                    "Son ami George",
                    "Ils vont au Canada",
                    "Ils vont au mexique") 
texte_colonne_deux = ("Le papillon se réveille prêt à toute épreuve. Qui veux-t-il voir aujourd'huis?", 
                        "Il a froid en se levant. Quel animal va-t-il se poser dessus pour se réchauffer?",
                        "Avec son expertise, il sait par instint ce que sa perte signifie. Qu'est-ce que le chef l'avise?",
                        "George le supporte du mieux qu'il est possible. Que planifies George?",
                        "Lorsqu'ils arrivent, la neige leur donnent froid. Quel plan font-ils?",
                        "Arriver là-bas ils font face à un buffet. Que mangent-t-ils en premier?") #6
choix_colonne_trois = ("Son meilleur ami George",
                        "Sa mère",
                        "Un ours brun",
                        "Un crocrodile",
                        "Qu'il va mourrir", 
                        "Qu'il est en mesure de réparer son aile",
                        "Une aventure jusqu'au haut d'une montagne",
                        "D'aller le tuer demain",
                        "Ils essaient d'aller au mexique",
                        "Ils entrent chez quelqu'un",
                        "Les bananes",
                        "Les mangues",)
texte_colonne_trois = ("Ensemble, ils font des relais. Georgina demande de les rejoindre. Est-ce qu'ils acceptent la demande?",
                        "Il passe une merveilleuse journée avec sa mère. À la fin de la journée, que font-ils ensemble?",
                        "Le papillon se sent réchauffer. Que fais l'ours brun?",
                        "Le crocrodile se met a nager pendant que le papillon dors sur lui. Que fais son ami George en le voyant?",
                        "Le papillon est triste de cette nouvelle. Que fais le papillon avec sa dernière journée?", 
                        "Le papillon se prépare à l'opération. Quel couleur demande-t-il pour sa nouvelle aile?",
                        "Georges amène sur son dos sont ami jusqu'au haut de la montagne. Face au froid, que fais George rendu au sommet?",
                        "Son plan ne va pas comme prévu. Pourquoi?",
                        "En route, George se fait frapper par un cycliste. Que fait son ami?",
                        "De retour au chaud, ils mangent les mangues du comptoir et font face aux propriétaires. Comment le propriétaire réagi-t-il?",
                        "Le vendeur est faché de ça. Que prends-t-il pour les frapper avec?",
                        "Un vendeur, ayant planifier ça avait déjà une mangue ouverte pour les papillons. Face à la compétition, que font-ils?") #12
choix_colonne_quatre = ("Oui, mais ils le font mécontent",
                        "Oui, ils l'acceptent heureux",
                        "Ils vont déguster une feuille de menthe ensemble",
                        "Ils vont observer un feu d'artifice",
                        "Il essaie d'enlever le papillon",
                        "Il ignore le papillon",
                        "Il rit de lui",
                        "Il essaie de le réveiller",
                        "Il va se poser près de sa roche préférer",
                        "Il va voir sa mère",
                        "Rouge",
                        "Brun",
                        "Il reste avec son ami",
                        "Il redescend sans son ami",
                        "George se fait manger par un ours.",
                        "L'ami de George se fait manger par un ours.", 
                        "Il arrête la route, ayant accepté son sort",
                        "Il continue la route, déterminé à retrouver le chaud du mexique.",
                        "Il les laisse vivre",
                        "Il essaie des tuer",
                        "Une banane",
                        "Une tapette à mouche",
                        "Ils battent leur aile pour faire fuir les autres papillons",
                        "Ils mangent le plus rapidement possible")
texte_colonne_quatre = ("Georgina casse les ailes de son frère George et son ami. Elle est triste et va se coucher tôt.",
                        "Le trio passe une après-midi pleine d'aventure!",
                        "Le papillon déguste et va voir le couché du soleil avec sa mère.",
                        "Le papillon fini sa journée satisfait de son aventure avec sa mère.",
                        "L'ours aggripe l'aile du papillon et le dévore.",
                        "Le papillon se rendort au chaud.",
                        "Le papillon s'endort a tout jamais.",
                        "George reussi et le papillon survie.",
                        "Il meurt à côté de sa roche préférer.",
                        "Sa mère lui donne une potion qui fait regrandir son aile, et il vit un été de plus.",
                        "Le papillon se fait tirer par un drone en développement qui tire tout ce qui est rouge un jour après l'opération",
                        "Le papillon vole mieux qu'avant, et vit pour une été de plus.",
                        "Ils meurent ensemble.",
                        "George vit une été de plus.",
                        "L'ami de George se trouve dans une situation difficile, mais il réussi a survivre un mois de plus.",
                        "Il est content que sa situation se soit régler par elle-même.",                       
                        "Grâce au réchauffement climatique, il survie.",
                        "Il meurt trop épuiser en altitude.",
                        "Ils mangent à leur faim pendant le restant de leur vie.",
                        "Ils meurent grâce à une tape à mouche.",
                        "La stratégie du vendeur habitué s'est montrer fructueuse pour une fois de plus.",
                        "Les papillons s'enfuient et partent pour explorer d'autres section du buffet.",
                        "Les autres papillons, n'étant pas leur première fois, les font partir et ils quittent le buffet affamer.",
                        "Ils sont heureux de quitter le buffet le ventre plein.") #24

textes_possible = (introduction, texte_colonne_un, texte_colonne_deux, texte_colonne_trois, texte_colonne_quatre)
choix_possible = (choix_colonne_un, choix_colonne_deux, choix_colonne_trois, choix_colonne_quatre)

erreur = 0

choix_faite = int(0)
indice_precedant = int(0) #indice precedant choix maximum
etat_actuel = int(0)

#TODO: Preferablement, separer en plusieurs commande
"""
Entrées: etat_actuel, textes_possible, choix_possible
Sorties: tuple comprenant texte, question et choix
But: Regrouper l'information à afficher selon l'état actuel
"""
def informations_actuel():
    global etat_actuel, choix_faite, indice_precedant, textes_possible, choix_possible
    match etat_actuel:
        case 0:
            texte = textes_possible[etat_actuel]
            choix = choix_possible[choix_faite - 1]
        case 1:
            list_texte = textes_possible[etat_actuel] # colonnne associer(retourne list)
            texte = list_texte[choix_faite - 1] # A partir du choix faite(retourne texte)
            
            list_choix = choix_possible[etat_actuel] # colonne associer(retourne list)
            indice_precedant = choix_faite*2
            choix = (list_choix[(indice_precedant) - 1 - 1], list_choix[indice_precedant - 1]) # (12 34 56)
        case 2:
            list_texte = textes_possible[etat_actuel]
            endroit_texte = indice_precedant + choix_faite - 2 # 2-2 donne 0 donc max possible, et 1-2 donne -1 ce qui correspont a lui d'avant
            texte = list_texte[endroit_texte - 1] 
            
            list_choix = choix_possible[etat_actuel]
            indice_precedant = endroit_texte * 2
            choix = (list_choix[indice_precedant - 1 - 1], list_choix[indice_precedant - 1])
        case 3:
            list_texte = textes_possible[etat_actuel]
            endroit_texte = indice_precedant + choix_faite - 2 
            texte = list_texte[endroit_texte - 1]

            list_choix = textes_possible[etat_actuel]
            indice_precedant = endroit_texte * 2
            choix = (list_choix[indice_precedant - 1 - 1], list_choix[indice_precedant - 1])
        case 4:
            list_texte = textes_possible[etat_actuel]
            endroit_texte = indice_precedant + choix_faite - 2
            texte = list_texte[endroit_texte - 1]
            choix = "" # Aucun choix puisque texte finale
        case _:
            return textes_possible[0], choix_possible[0]
    return texte, choix


#TODO: Idéalement, trier les lists pour obtenir la question separement du texte, et les afficher
def separer_texte_question():
    return 0

"""
Entrées: Rien
Sorties: String dans le terminal
But: Obtenir facilement une cohérence dans les sauts de ligne pour séparer les différentes sections du texte, question et choix
"""
def print_saut_ligne():
    print("-" * 33)

#TODO: Modifier commentaires partout et specifiquement entrer ici
"""
Entrées: choix_afficher, texte_afficher, question_afficher
Sorties: String dans le terminal
But: Afficher le texte, la question, les choix possibles et l'instruction de manière claire et bien formatté pour le lecteur
But futur: Manipuler les listes pour afficher seulement les éléments nécessaires, et les afficher de manière claire pour le lecteur
"""
def print_final():
    informations = informations_actuel()
    print_saut_ligne()
    print(f"Texte: {informations[0]}")
    print_saut_ligne()
    #print(f"Question: {information[1]}")
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print_saut_ligne()
    i = 0
    len_choix = len(informations[1])
    if i < len_choix:
        choix_x_visible = informations[1][i]
        print(f"Choix {i+1}: {choix_x_visible}")
        i += 1
    if i < len_choix:
        choix_x_visible = informations[1][i]
        print(f"Choix {i+1}: {choix_x_visible}")
        i += 1
    if i < len_choix:
        choix_x_visible = informations[1][i]
        print(f"Choix {i+1}: {choix_x_visible}")
        #i += 1
    print_saut_ligne()
    if len_choix > 0:
        print("Entrez le numéro de votre choix pour continuer l'histoire.")
        print_saut_ligne()

#TODO: Distinguer davantage le print lorsquune erreur
"""
Entrées: choix_faite, etat_actuel, erreur
Sortie: etat_actuel
But: Changer d'état si désirer
"""
def changement_etat():
    global choix_faite, etat_actuel, erreur, prev_choix_faite
    if choix_faite == 3 and etat_actuel == 0: #vérifie si peut passer au prochain état
        return 1
    elif choix_faite == 1 or choix_faite == 2:
        return int(etat_actuel + 1)
    else: # sinon 
        choix_faite = prev_choix_faite
        erreur += 1 
        print_final()
        print_saut_ligne()
        print("Votre choix était invalide, veuillez le retapez")
        print_saut_ligne()
        return etat_actuel

prev_choix_faite = choix_faite
choix_faite = int(input(print_final())) # 1er choix
etat_actuel = changement_etat() # change état si peu

#TODO: essayer try-except
#######################
if erreur > 0:
    choix_faite = int(input(print_final())) # Xer choix
    etat_actuel = changement_etat() # change état si peu
    erreur -= 1
else:
    prev_choix_faite = choix_faite
    choix_faite = int(input(print_final())) #2em choix
    etat_actuel = changement_etat() # change état si peu

#######################
if erreur > 0:
    choix_faite = int(input(print_final())) # Xer choix
    etat_actuel = changement_etat() # change état si peu
    erreur -= 1
else:
    prev_choix_faite = choix_faite
    choix_faite = int(input(print_final())) #3em choix
    etat_actuel = changement_etat() # change état si peu

#######################
if erreur > 0:
    choix_faite = int(input(print_final())) # Xer choix
    etat_actuel = changement_etat() # change état si peu
    erreur -= 1
else:
    prev_choix_faite = choix_faite
    choix_faite = int(input(print_final())) #4em choix
    etat_actuel = changement_etat() # change état si peu

#######################
if erreur > 0:
    choix_faite = int(input(print_final())) # Xer choix
    etat_actuel = changement_etat() # change état si peu
    erreur -= 1
else:
    print_final()
""""
Cassey Martin

Fichier principale projet livre interactif
"""

"""
Structure en arbre
Rappel: Aucune boucle permise.

Trier par des lists en rangée pour le texte afficher
(Incluant la question)
Montrer les choix possibles, organiser en rangé aussi(associer aux lignes)

Docstring doivent etre écrits pour chaque fonction, et pour le projet en général:
Entrées: 
Sorties:
But:

"""
#tuples are ordered and unchangeable, lists are ordered and changeable, sets are unordered and unindexed, dictionaries are unordered, changeable and indexed
introduction = "Un papillon vole dans la forêt, il est heureux et libre. Ensuite, que fais-t-il?" 
nombere_ranger = int(5)
choix_ranger_un = tuple("Il se pose sur une feuille", 
                        "Il fonce dans un oiseau", 
                        "Il essaie de trouver son ami perdu") # 3 choix
texte_ranger_un = ("Pendant que le papillon dort sur une feuille, il a froid. À quel endroit va-t-il se réfugier pour se réchauffer?", 
                    "Ah non, son aile se brise! Il va voir qui pour la réparer?", 
                    "Il retrouve George, son ami d'enfance. À quel endroit va-t-il avec George?") #3 textes
choix_ranger_deux = ("Un trou dans un arbre", 
                    "Une fleur",
                    "La papillon en chef",
                    "Son ami George",
                    "Ils vont au Canada",
                    "Ils vont au mexique") 
texte_ranger_deux = ("Le papillon se réveille prêt à toute épreuve. Qui veux-t-il voir aujourd'huis?", 
                        "Il a froid en se levant. Quel animal va-t-il se poser dessus pour se réchauffer?",
                        "Avec son expertise, il sait par instint ce que sa perte signifie. Qu'est-ce que le chef l'avise?",
                        "George le supporte du mieux qu'il est possible. Que planifies George?",
                        "Lorsqu'ils arrivent, la neige leur donnent froid. Quel plan font-ils?",
                        "Arriver là-bas ils font face à un buffet. Que mangent-t-ils en premier?") #6
choix_ranger_trois = ("Sa mère", #0a1a
                        "Son meilleur ami George",
                        "Un ours brun",
                        "Un crocrodile",
                        "Qu'il va mourrir", 
                        "Qu'il est en mesure de réparer son aile",
                        "Une aventure jusqu'au haut d'une montagne",
                        "D'aller le tuer demain",
                        "Ils entrent chez quelqu'un",
                        "Ils essaient d'aller au mexique",
                        "Les mangues",
                        "Les bananes",)
texte_ranger_trois = ("Il passe une merveilleuse journée avec sa mère. À la fin de la journée, que font-ils ensemble?",
                        "Ensemble, ils font des relais. Georgina demande de les rejoindre. Est-ce qu'ils acceptent la demande?",
                        "Le papillon se sent réchauffer. Que fais l'ours brun?",
                        "Le crocrodile se met a nager pendant que le papillon dors sur lui. Que fais son ami George en le voyant?",
                        "Le papillon est triste de cette nouvelle. Que fais le papillon avec sa dernière journée?", 
                        "Le papillon se prépare à l'opération. Quel couleur demande-t-il pour sa nouvelle aile?",
                        "Georges amène sur son dos sont ami jusqu'au haut de la montagne. Face au froid, que fais George rendu au sommet?",
                        "Son plan ne va pas comme prévu. Pourquoi?",
                        "De retour au chaud, ils mangent les mangues du comptoir et font face aux propriétaires. Comment le propriétaire réagi-t-il?",
                        "En route, George se fait frapper par un cycliste. Que fait son ami?",
                        "Un vendeur, ayant planifier ça avait déjà une mangue ouverte pour les papillons. Face à la compétition, que font-ils?",
                        "Le vendeur est faché de ça. Que prends-t-il pour les frapper avec?",) #12
choix_ranger_quatre = ("Ils vont observer un feu d'artifice",
                        "Ils vont déguster une feuille de menthe ensemble",
                        "Oui, ils l'acceptent heureux",
                        "Oui, mais ils le font mécontent",
                        "Il ignore le papillon", 
                        "Il essaie d'enlever le papillon",
                        "Il essaie de le réveiller",
                        "Il rit de lui",
                        "Il va voir sa mère",
                        "Il va se poser près de sa roche préférer",
                        "Brun",
                        "Rouge",
                        "Il redescend sans son ami",
                        "Il reste avec son ami",
                        "George se fait manger par un ours.",
                        "L'ami de George se fait manger par un ours.", 
                        "Il les laisse vivre",
                        "Il essaie des tuer",
                        "Il arrête la route, ayant accepté son sort",
                        "Il continue la route, déterminé à retrouver le chaud du mexique.",
                        "Ils mangent le plus rapidement possible",
                        "Ils battent leur aile pour faire fuir les autres papillons",
                        "Une banane",
                        "Une tapette à mouche")
texte_ranger_quatre = ("Le papillon fini sa journée satisfait de son aventure avec sa mère.",
                        "Le papillon déguste et va voir le couché du soleil avec sa mère.",
                        "Le trio passe une après-midi pleine d'aventure!",
                        "Georgina casse les ailes de son frère George et son ami. Elle est triste et va se coucher tôt.",
                        "Le papillon se rendort au chaud.", 
                        "L'ours aggripe l'aile du papillon et le dévore.",
                        "George reussi et le papillon survie.",
                        "Le papillon s'endort a tout jamais.",
                        "Sa mère lui donne une potion qui fait regrandir son aile, et il vit un été de plus.",
                        "Il meurt à côté de sa roche préférer.",
                        "Le papillon vole mieux qu'avant, et vit pour une été de plus.",
                        "Le papillon se fait tirer par un drone en développement qui tire tout ce qui est rouge un jour après l'opération",
                        "George vit une été de plus.",
                        "Ils meurent ensemble.",
                        "L'ami de George se trouve dans une situation difficile, mais il réussi a survivre un mois de plus.",
                        "Il est content que sa situation se soit régler par elle-même.", 
                        "Ils mangent à leur faim pendant le restant de leur vie.",
                        "Ils meurent grâce à une tape à mouche.",
                        "Grâce au réchauffement climatique, il survie.",
                        "Il meurt trop épuiser en altitude.",
                        "Ils sont heureux de quitter le buffet le ventre plein.",
                        "Les autres papillons, n'étant pas leur première fois, les font partir et ils quittent le buffet affamer.",
                        "La stratégie du vendeur habitué s'est montrer fructueuse pour une fois de plus.",
                        "Les papillons s'enfuient et partent pour explorer d'autres section du buffet.") #24

#Reste une list
choix_afficher = []
texte_afficher = str("")
question_afficher = str("")

commande = int(0)

#TODO: Trier les lists pour obtenir seulement les éléments nécessaires à afficher, et les afficher
def trier_texte_afficher():
    return 0

#TODO: Trier les lists pour obtenir seulement les éléments nécessaires à afficher, et les afficher
def trier_choix_afficher():
    return 0

#TODO: Idéalement, trier les lists pour obtenir la question separement du texte, et les afficher
def separer_texte_question():
    return 0

"""
Entrées: Rien
Sorties: String dans le terminal
But: Obtenir facilement une cohérence dans les sauts de ligne pour séparer les différentes sections du texte, question et choix
"""
def print_saut_ligne():
    print("-------------------------------------------------------------------------------------------------------------------")

"""
Entrées: choix_afficher, texte_afficher, question_afficher
Sorties: String dans le terminal
But: Afficher le texte, la question, les choix possibles et l'instruction de manière claire et bien formatté pour le lecteur
But futur: Manipuler les listes pour afficher seulement les éléments nécessaires, et les afficher de manière claire pour le lecteur
"""
def print_final():
    global choix_afficher, texte_afficher, question_afficher
    print_saut_ligne()
    print(f"Texte: {texte_afficher}")
    print_saut_ligne()
    print(f"Question: {question_afficher}")
    print_saut_ligne()
    i = 0
    len_choix = len(choix_afficher)
    if i < len_choix:
        choix_x_visible = choix_afficher[i]
        print(f"Choix {i+1}: {choix_x_visible}")
        i += 1
    print_saut_ligne()
    print("Entrez le numéro de votre choix pour continuer l'histoire.")
    print_saut_ligne()

commande = int(input(print_final())) #input attend avant de se reéexecuter

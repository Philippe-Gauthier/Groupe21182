"""
Docstring for Ahmed.projet
by Ahmed Ait Hammou
Fichier principal pour Hardware and technoligies\ Choiceforge
"""
"""
quiz est le nom de la fonction de definition
les entrée ce sont le choix1, choix2, choix3, choix4 et correct_answer
return decision est la sortie de la fonction
"""
def quiz(question, choix1, choix2, choix3, choix4, correct_answer):
    # Affiche la question et les choix de réponse
    print(f"{question}")
    print(f"1: {choix1}")
    print(f"2: {choix2}")
    print(f"3: {choix3}")
    #n'afiche pas le quatriéme choix si il est vide
    if choix4 != "":
        print(f"4: {choix4}")
    # Vérifie que la réponse de l'utilisateur est valide
    valid_choices = ["1", "2", "3", "4"]
    # Demande à l'utilisateur de faire un choix
    decision = input("Entrez votre choix: ")
    # Vérifie que la réponse de l'utilisateur est la bonne ou pas
    if decision == correct_answer:
        print("Bonne réponse!")
    elif decision in valid_choices:
        correct_answer != valid_choices
        print("Mauvaise réponse!")
    # Si la réponse de l'utilisateur n'est pas valide, affiche un message d'erreur
    else:
        print("c'est du n'importe quoi mon gars, fait entrer les bonnes chiffres la prochaine fois")
        return decision
quiz("Quelle compagnie a un meilleur rapport qualité pour prix dans les GPU?", "Nvidia","AMD","Intel","","2")
quiz("Quelle est la marque de GPU la plus vendue au monde?", "Nvidia", "AMD", "Intel", "", "1")
quiz("la methode la plus éfficace pour diminué la temperature d'un CPU dans un budget de 45$?", "Air cooling single tower", "Water cooling", "Air cooling duel tower", "", "1")
quiz("qui est le plus performent?", "Exynos 2600", "Apple A19 Pro", "Dimensity 9500s", "Snapdragon 8 Elite Gen 5", "3")
quiz("c'est quoi la marque de téléphone la plus vendu au monde?", "Samsung", "Apple", "Xiaomi", "Oppo", "1")
quiz("quelle est la marque de CPU la plus vendu au monde?", "Intel", "AMD", "Apple", "Qualcomm", "1")
quiz("quelle est la marque de RAM la plus vendu au monde?", "Corsair", "G.Skill", "Kingston", "Crucial", "3")
quiz("quelle est la marque de SSD la plus vendu au monde?", "Samsung", "Western Digital", "Crucial", "Seagate", "1")
quiz("quelle est la marque de carte mère la plus vendu au monde?", "ASUS", "MSI", "Gigabyte", "ASRock", "1")
quiz("quelle carte graphique est fabriqué par Nvidia?", "RTX 6080", "RX 7900 XT", "RX 6800", "RTX 5090", "4")
quiz("quelle composante est la plus importante pour le gaming?", "CPU", "GPU", "RAM", "SSD", "2")
quiz("quelle composante est considéré comme le cerveau de l'ordinateur?", "CPU", "GPU", "RAM", "SSD", "1")

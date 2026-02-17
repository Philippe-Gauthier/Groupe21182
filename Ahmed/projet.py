"""
Docstring for Ahmed.projet
by Ahmed Ait Hammou
Fichier principal pour Hardware and technoligies\ Choiceforge
"""
def quiz(question, choix1, choix2, choix3, choix4, correct_answer):
    print(f"{question}")
    print(f"1: {choix1}")
    print(f"2: {choix2}")
    print(f"3: {choix3}")
    print(f"4: {choix4}")
    decision = input("Entrez votre choix: ")
    if decision == correct_answer :
        print("Bonne réponse!")
    else:
        print("Mauvaise réponse!")
        return decision
quiz("Quelle compagnie a un meilleur rapport qualité pour prix dans les GPU?", "Nvidia","AMD","Intel","","2")
quiz("Quelle est la marque de GPU la plus vendue au monde?", "Nvidia", "AMD", "Intel", "", "1")
quiz("la methode la plus éfficace pour diminué la temperature d'un CPU dans un budget de 45$?", "Air cooling single tower", "Water cooling", "Air cooling duel tower", "", "1")
quiz("qui est le plus performent?", "Exynos 2600", "Apple A19 Pro", "Dimensity 9500s", "Snapdragon 8 Elite Gen 5", "3")
quiz("c'est quoi la marque de téléphone la plus vendu au monde?", "Samsung", "Apple", "Xiaomi", "Oppo", "1")

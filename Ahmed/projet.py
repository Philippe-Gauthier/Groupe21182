"""
Docstring for Ahmed.projet
by Ahmed Ait Hammou
Fichier principal pour Hardware and technoligies\ Choiceforge
"""
def quiz():
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
question = "Quelle compagnie a un meilleur rapport qualité pour prix dans les GPU?"
choix1 = "Nvidia"
choix2 = "AMD"
choix3 = "Intel"
choix4 = ""
correct_answer = "2"
print(f" entrez votre choix: { choix1}, {choix2}, {choix3}")
quiz()
question = "C'est quoi la composante la plus utilié dans le 3D modeling?"
choix1 = "CPU"  
choix2 = "GPU"
choix3 = "RAM"
choix4 = ""
correct_answer = "2"
print(f" entrez votre choix: {choix1}, {choix2}, {choix3}")
quiz()
question = "la methode la plus éfficace pour diminué la temperature d'un CPU dans un budget de 45$?"
choix2= "Water cooling"
choix1= "Air cooling single tower"
choix3= "Air cooling duel tower"
choix4= ""
correct_answer = "1"
quiz()
question = "qui est le plus performent?"
choix1= "Exynos 2600"
choix2= "Apple A19 Pro"
choix3= "Dimensity 9500s"
choix4= "Snapdragon 8 Elite Gen 5"
correct_answer = "3"
quiz()
question = "c'est quoi la marque de téléphone la plus vendu au monde?"
choix1= "Samsung"
choix2= "Apple"
choix3= "Xiaomi"
choix4= "Oppo"
correct_answer = "1"
quiz()
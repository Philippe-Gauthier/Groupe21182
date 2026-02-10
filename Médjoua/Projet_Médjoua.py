test1 = "Quelle est l unité de la tension électrique ?"
choix11 = "Ampère"
choix12 = "Volt "
choix13 = "Ohm"

test2 = "Le voltmètre permet de mesurer quoi ?"
choix21 = "le courant"
choix22 = "la tension"
choix23 = "la puissance"

test3 = "Quelle est l unité du courant électrique ?"
choix31 = "Watt"
choix32 = "Ohm"
choix33 = "Ampere"

test4 = "Quelle est l outil qui permet de mesurer le courant électrique ?"
choix41 = "Amperemetre"
choix42 = "Wattmetre"
choix43 = "Ohmetre"

test5 = "Quelle est la formule de l'intensité du courant électrique ?"
choix51 = "U=V*I"
choix52 = "P=U*I"
choix53 = "I=R*U"

test6 = "Quelle est le symbole de la puissance électri"

def reponse_(choix1, choix2, choix3,) : 
 print("------------------------------")
 print(f"1: {choix1}")
 print(f"2: {choix2}")
 print(f"3: {choix3}")
 decision = int(input("Veuillez choisir votre reponse :"))

 return decision

print(test1)

reponse_(choix11, choix12, choix13)

print(test2)

reponse_(choix21, choix22, choix23)

print(test3)

reponse_(choix31, choix32, choix33)















































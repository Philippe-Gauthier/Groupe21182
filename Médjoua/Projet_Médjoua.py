"""
Auteur : Médjoua, Karaboue.
date :   fevrier 2026.
Projet : Jeu de question à choix multiple.
"""


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

test6 = "Quelle est le symbole de la puissance électrique"
choix61 = "R"
choix62 = "P"
choix63 = "V"

test7 = "Quelle est l'unité de la puissance électrique ?"
choix71 = "Farad"
choix72 = "Henri"
choix73 = "Watt"

test8 = "Qu'est ce que une inductance ?"
choix81 = "c'est une bobine"
choix82 = "c'est un condensateur"
choix83 = "c'est une resistance"

test9 = "Quelle est l unité de l inductance ?"
choix91 = "Hertz"
choix92 = "Henri"
choix93 = "Farad"

test10 = "Quelle est la formule de l inductance ?"
choix101 = "H = 1/T"
choix102 = "C = Q*t"
choix103 = "H = L*di/dt"

test11 = "Quel composant filtre la tension ?"
choix111 = "la Diode"
choix112 = "le condensatuer"
choix113 = "la resistance"

test12 = "Quel est l'unité de mesure du condensateur ?"
choix121 = "Henri"
choix122 = "Ohm"
choix123 = "Farad"

test13 = "Quel instrument permet de mésurer la capacitance ?"
choix131 = "Oscilloscope"
choix132 = "Générateur"
choix133 = "multimètre"

test14 = "Quel est spéciliter ?"
choix141 = "mémoire de courant"
choix142 = "memoire de  tension"
choix143 = "memoire de puissance"

test15 = "Quel composant laisse passé le courant dans un seul sens ?"
test151 = "la diode"
test152 = "la resistance"
test153 = "la bobine"

test16 = ""





def trouver_reponse(choix1, choix2, choix3,) : 
 """ Trouver la bonne reponse parmis les troischoix de reponse(...) """
 print("------------------------------")
 print(f"1: {choix1}")
 print(f"2: {choix2}")
 print(f"3: {choix3}")
 decision = int(input("Veuillez choisir votre reponse :"))

 return decision

print(test1)

trouver_reponse(choix11, choix12, choix13)

print(test2)

trouver_reponse(choix21, choix22, choix23)

print(test3)

trouver_reponse(choix31, choix32, choix33)

print(test4)

trouver_reponse(choix41, choix42, choix43)

print(test5)

trouver_reponse(choix51, choix52, choix53)

print(test6)

trouver_reponse(choix61, choix62, choix63)

print(test7)

trouver_reponse(choix71, choix72, choix73)

print(test8)

trouver_reponse(choix81, choix82, choix83)

print(test9)         

trouver_reponse(choix91, choix92, choix93)

print(test10)

trouver_reponse(choix101, choix102, choix103)
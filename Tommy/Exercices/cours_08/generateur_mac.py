import random

caracteres_valide = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def creer_bloc():
    element_01 = random.choice(caracteres_valide)
    element_02 = random.choice(caracteres_valide)

    return (element_01 + element_02)

adresse_mac = ""

for i in range(6):
    adresse_mac += creer_bloc() + ":"

adresse_mac = adresse_mac[:-1]

print(adresse_mac)
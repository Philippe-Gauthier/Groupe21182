import random

def des_6(nombre):
    total = 0
    for i in range(nombre): #Ligne qui permet de determiner le nb de des qu'on lance
        total += random.randint(1,6) #dire que cest un dé 6
    return total

print(des_6(1))


def des_20(nombre):
    total = 0
    for i in range(nombre):
        total += random.randint(1,20)
    return total

print(des_20(10))
    

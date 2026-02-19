print("1:Addition\n2:Soustraction")
choix = int(input("Choisis 1 ou 2: "))

if choix == 1:
    nombre1 = int(input("Ecrivez 1 nombre: "))
    nombre2 = int(input("Ecrivez 1 nombre a additionner: "))
    print(nombre1 + nombre2)
else:
    nombre1 = int(input("Ecrivez 1 nombre: "))
    nombre2 = int(input("Ecrivez 1 nombre a soustraire: "))
    print(nombre1 - nombre2)
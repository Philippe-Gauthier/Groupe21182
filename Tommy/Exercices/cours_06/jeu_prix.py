prix_secret = 36

while True:
    devine = int(input ("Quel est le prix: "))

    if devine > prix_secret:
        print("cest moins!")

    elif devine < prix_secret:
        print("cest plus!")

    else:
        print("cest gagne")
        break

name = input("Entrez votre nom: ")

porte = input("Bonjour, " + name + " faites votre chois entre 3 portes: gauche, droite ou centre?")
#la console indique que la parentaise ne ferme pas

match porte:

    case "gauche":
        print("Vous avez choisis la porte 1, celle de gauche.")

    case "droite":
        print("Vous avez choisis la porte 2, celle de droite.")

    case "centre":
        print("Vous avez choisis la porte 3, celle au centre.")

equipement = input("Devans vous se trouvent trois objets, vous ne pouvez n'en prendre qu'un. La corde, la poêle ou le tournevis?")

match equipement:

    case "corde":
        print("la corde, pratique.")

    case "poêle":
        print("Vous Etes sure?")

    case "tournevis":
        print("tres bon chois")
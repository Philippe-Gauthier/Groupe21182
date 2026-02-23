
question1 = "a"
choix1_1 = "b"
choix1_2 = "c"
question1_1 = "d"
choix1_1_1 = "e"
choix1_1_2 = "f"
question1_2 = "g"
question1_2_1 = "h"
question1_2_2 = "i"


def formatter(question, choix1, choix2):
    message = f"{question}\n"
    message += ("_" * 30) + "\n"
    message += f"1: {choix1} \n"
    message += f"2: {choix2} \n"
    message += "Decision: "
    return message

def questionner(question, choix1, choix2):
    decision = input(formatter(question, choix1, choix2))
    if proteger(decision):
        return decision
    else:
        print("erreur: Entree non-valide")
        return questionner(question, choix1, choix2)

def proteger(decision):
    if decision == "1" or decision == "2":
        protection = True
    else:
        protection = False

    return protection

decision = questionner(question1, choix1_1, choix1_2)
if decision == "1":
    decision = questionner(question1_1, choix1_1_1, choix1_1_2)
    if decision == "1":
        print("fin")


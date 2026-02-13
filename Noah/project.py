"""
by Noah PAYET
Fichier principal pour le début de l'hisoitre / simulateur d'ile de La Réunion
"""

# Importer les librairies necessaire au bon fonctionnement
import json
from tkinter import *
from PIL import Image, ImageTk

# Recupere les infos du fichier JSON
with open("story.json", "r", encoding="utf-8") as f:
    story = json.load(f)

# Permet d'afficher un chapitre
def afficher_chapitre(chapitre):
    global chapitre_actuel
    chapitre_actuel = chapitre

    # Recupere les donnees du json et les assignes a une variable
    data = story[chapitre]

    question = data["texte"]
    choix1 = data["choix1"]["texte"]
    choix2 = data["choix2"]["texte"]
    choix3 = data["choix3"]["texte"]
    choix4 = data["choix4"]["texte"]

    image_path = data["image"]
    image = Image.open(image_path)
    global photo
    photo = ImageTk.PhotoImage(image)

    # Associe chaque bouton a la destination correspondante. lambda sert de fonction temporaire qui appelle choisir associe au bouton
    bouton1.config(text=choix1, command=lambda: choisir(data["choix1"]["destination"]))
    bouton2.config(text=choix2, command=lambda: choisir(data["choix2"]["destination"]))
    bouton3.config(text=choix3, command=lambda: choisir(data["choix3"]["destination"]))
    bouton4.config(text=choix4, command=lambda: choisir(data["choix4"]["destination"]))

    boite_image.config(image=photo)
    question_label.config(text=question)

# appeler lorsqu'on clique sur un choix 
def choisir(nouveau_chapitre):
    if nouveau_chapitre:    
        afficher_chapitre(nouveau_chapitre)



# Creation de la fenetre principale
fenetre = Tk()
fenetre.minsize(1366, 768)
fenetre.maxsize(1920, 1080)
fenetre['bg'] = 'gray'

# Titre de la fenetre
fenetre.title("Reunion Island Simulator")
titre_label = Label(fenetre, text="Reunion Island Simulator")
titre_label.pack(padx=20, pady=20)

# Frame principale qui contient l'image et la question
Frame2 = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
Frame2.pack(expand=True, fill=BOTH, padx=40, pady=40)

# Frame pour l'image
boite_image = Label(Frame2, relief=RIDGE, borderwidth=2, anchor=CENTER)
boite_image.pack(padx=40, pady=10)

# Frame pour la question
boite_question = Frame(Frame2, bg="gray", relief=RIDGE)
boite_question.pack(padx=0.5, pady=2)

# Label pour la question
question_label = Label(boite_question, font=("Arial", 16))
question_label.pack(padx=20, pady=20)

# Frame pour les boutons de choix
Frame1 = Frame(fenetre, relief=RIDGE, bg="gray")
Frame1.pack(pady=20)

bouton1 = Button(Frame1, text="choix1", relief=RIDGE, font=("Arial", 12), bg="lightgray")
bouton1.pack(side=LEFT, padx=10)

bouton2 = Button(Frame1, text="choix2", relief=RIDGE, font=("Arial", 12), bg="lightgray")
bouton2.pack(side=LEFT, padx=10)

Label(Frame1, text="Faites un choix").pack(side=LEFT, padx=20)

bouton3 = Button(Frame1, text="choix3", relief=RIDGE, font=("Arial", 12), bg="lightgray")
bouton3.pack(side=LEFT, padx=10)

bouton4 = Button(Frame1, text="choix4", relief=RIDGE, font=("Arial", 12), bg="lightgray")
bouton4.pack(side=LEFT, padx=10)


# Affiche le chapitre d'introduction
afficher_chapitre("intro")

# Lancer la boucle principale de la fenetre
fenetre.mainloop()



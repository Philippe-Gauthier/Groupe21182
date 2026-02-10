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
    resized_image = image.resize((300, 300 ))
    photo = ImageTk.PhotoImage(resized_image)

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
fenetre.geometry("1366x768")
fenetre['bg'] = 'white'

# Titre de la fenetre
fenetre.title("Reunion Island Simulator")
titre_label = Label(fenetre, text="Reunion Island Simulator")
titre_label.pack(padx=20, pady=20)

# Frame principale qui contient l'image et la question
Frame2 = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
Frame2.pack(expand=True, fill=BOTH, padx=40, pady=10)

# Frame pour l'image
boite_image = Label(Frame2)
boite_image.pack(padx=40, pady=10)

# Frame pour la question
boite_question = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
boite_question.place(relx=0.5, rely=0.5, anchor=CENTER)

# Label pour la question
question_label = Label(boite_question, text="test", bg="white", font=("Arial", 16))
question_label.pack(padx=20, pady=20)

# Frame pour les boutons de choix
Frame1 = Frame(fenetre, bg="white")
Frame1.pack(pady=20)

bouton1 = Button(Frame1, text="choix1")
bouton1.pack(side=LEFT, padx=10)

bouton2 = Button(Frame1, text="choix2")
bouton2.pack(side=LEFT, padx=10)

Label(Frame1, text="Faites un choix", bg="white").pack(side=LEFT, padx=20)

bouton3 = Button(Frame1, text="choix3")
bouton3.pack(side=LEFT, padx=10)

bouton4 = Button(Frame1, text="choix4")
bouton4.pack(side=LEFT, padx=10)


# Affiche le chapitre d'introduction
afficher_chapitre("intro")

# Lancer la boucle principale de la fenetre
fenetre.mainloop()



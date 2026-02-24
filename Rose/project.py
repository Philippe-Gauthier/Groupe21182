"""
Rosemarie Dalton
gr 21182

projet 1 : Livre dont vous êtes le héros

"""

import textwrap as tw
import tkinter as tk
import StrandedText as st


class App:
    """
    Voici la plus grande partie du code. La classe App gère
    l'état de l'application et l'interface utilisateur.

    Ici, vous allez trouver les fonctions suivantes :
    - __init__: initialise l'application, crée l'interface
        utilisateur et définit les pages et les transitions.
    - update_view: met à jour le texte affiché et les étiquettes
        des boutons en fonction de la page actuelle.
    - on_button: gère les pressions de boutons et met à jour la
        page actuelle en fonction des transitions définies dans
        __init__.
    """

    def __init__(self, window):
        """
        Entree self: le parametre self permet d'acceder aux variables
        qui sont normalement uniques a la fonction dans d'autres
        fonctions de la classe App.

        Entree window: le parametre window est la fenetre principale
        de l'application tkinter. Lorsque l'on cree une instance de la
        classe App, on lui passe cette fenetre pour qu'elle puisse y
        ajouter la fenetre dans laquelle l'application va s'executer.

        Cette fonction initialise l'application, crée l'interface
        utilisateur et définit les pages et les transitions. Ses sorties
        sont :
        - self.pages : un dictionnaire qui associe chaque numero de
            page a son objet page
        - self.transitions : un dictionnaire qui associe chaque numero
            de page a une liste de pages suivantes en fonction du bouton
            appuye
        - self.curr_page : le numero de la page actuelle
        - la configuration des elements de l'interface utilisateur
            (fenetre, texte et boutons)

        Le but de cette fonction est de preparer l'application pour
        qu'elle puisse afficher la page initiale et repondre aux
        interactions de l'utilisateur.
        """
        self.window = window
        self.BUTTON_SIZE = 52
        self.test_mode = False
        self.test_page = 7
        self.path = []

        #TODO: debut du code pertinent pour l'evaluation
        # ici on cree un "lexique" qui associe chaque numero de page a
        # son objet page, provenant du fichier StrandedText.py
        self.PAGES = {
            1: st.p1,
            2: st.p2,
            3: st.p3,
            4: st.p4,
            5: st.p5,
            6: st.p6,
            7: st.p7,
            8: st.p8,
            9: st.p9,
            10: st.p10,
            11: st.p11,
            12: st.p12,
            13: st.p13,
            14: st.p14,
            15: st.p15,
            16: st.p16,
            17: st.p17,
            18: st.p18,
            19: st.p19,
            20: st.p20,
            21: st.p21,
            22: st.p22,
            23: st.p23,
            24: st.p24,
            25: st.p25,
            26: st.p26,
            27: st.p27,
            28: st.p28,
            29: st.p29,
            30: st.p30,
            31: st.p31,
            32: st.p32,
            33: st.p33,
            34: st.p34,
            35: st.p35,
            36: st.p36,
            37: st.p37,
            38: st.p38,
            39: st.p39,
            40: st.p40,
            41: st.p41
        }

        # ceci est un dictionnaire qui associe chaque numero de page a une
        # liste de pages suivantes en fonction du bouton appuye (1 pour
        # A, 2 pour B, 3 pour C, 4 pour D etc.)
        self.TRANSITIONS = {
            1: (2, 3, 4, 5),
            2: (6, 10, 6, 11),
            4: (7, 7, 7, 7),
            5: (12, 14, 12, 14),
            6: (15, 16, 17, 18),
            7: (8, 13, 19, 20),
            8: (41, 41, 41, 41),
            9: (8, 13, 19, 20),
            10: (15, 16, 17, 18),
            11: (15, 16, 17, 18),
            12: (8, 13, 19, 20),
            13: (41, 41, 41, 41),
            14: (8, 13, 19, 20),
            16: (7, 9, 7, 9),
            17: (26, 27, 28, 18),
            18: (41, 41, 41, 41),
            19: (41, 41, 41, 41),
            20: (41, 41, 41, 41),
            21: (41, 41, 41, 41),
            22: (41, 41, 41, 41),
            23: (41, 41, 41, 41),
            24: (41, 41, 41, 41),
            25: (41, 41, 41, 41),
            26: (41, 41, 41, 41),
            27: (41, 41, 41, 41),
            28: (41, 41, 41, 41),
            29: (41, 41, 41, 41),
            30: (41, 41, 41, 41),
            31: (41, 41, 41, 41),
            32: (41, 41, 41, 41),
            33: (41, 41, 41, 41),
            34: (41, 41, 41, 41),
            35: (41, 41, 41, 41),
            36: (41, 41, 41, 41),
            37: (41, 41, 41, 41),
            38: (41, 41, 41, 41),
            39: (41, 41, 41, 41),
            40: (41, 41, 41, 41),
            # les pages sans transitions definies restent sur la meme page
        }
        if self.test_mode:
            self.curr_page = self.test_page
        else : self.curr_page = 1

        #TODO: fin du code pertinent pour l'evaluation

        # configuration de l'interface utilisateur : on cree un widget Text
        # pour afficher le texte de la page, et des boutons pour les
        # options. On configure aussi la fenetre (taille, titre, couleur
        # de fond etc.)
        self.text = tk.Text(
            window,
            height = 17,
            width = 10,
            font = ("Helvetica", 16),
        )
        window.resizable(False, False)
        window.title("Livre")
        window.geometry("980x600")
        window.configure(bg = "darkOliveGreen")

        self.text.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "NSEW",
            padx = 5,
            pady = 5,
        )
        self.text.configure(
            bg = "darkOliveGreen4",
            fg = "black",
            state = tk.DISABLED,
        )
        window.grid_rowconfigure(index = 0, weight = 0)
        window.grid_columnconfigure(index = 0, weight = 1)

        # creer les boutons et les placer dans la fenetre. Les boutons
        # sont associes a la fonction on_button
        self.buttons = []
        for i in range(4):
            b = tk.Button(
                window,
                text = "",
                command=(lambda index = i + 1: self.on_button(index)),
            )
            b.config(
                height = 2,
                width = self.BUTTON_SIZE,
                bg = "darkOliveGreen4",
                fg = "black",
                font = ("Helvetica", 12))
            self.buttons.append(b)

        # placer les boutons dans la fenetre en utilisant grid. Les
        # boutons sont placés de manière à ce qu'ils soient alignés à
        # gauche et à droite de la fenetre, avec un espacement entre eux.
        self.buttons[0].grid(row = 2,
                            column = 0,
                            sticky = "E",
                            padx = 5,
                            pady = 5)
        self.buttons[1].grid(row = 2,
                             column = 0,
                             sticky = "W",
                             padx = 5,
                             pady = 5)
        self.buttons[2].grid(row = 3,
                             column = 0,
                             sticky = "E",
                             padx = 5,
                             pady = 5)
        self.buttons[3].grid(row = 3,
                             column = 0,
                             sticky = "W",
                             padx = 5,
                             pady = 5)

        self.update_view()

    #TODO: debut du code pertinent pour l'evaluation
    def update_view(self):
        """
        But : cette fonction met à jour le texte affiché et les
        étiquettes des boutons en fonction de la page actuelle.

        Entree self: le parametre self permet d'acceder aux variables qui
        sont normalement uniques a la fonction dans d'autres fonctions de
        la classe App.

        Les sorties de cette fonction sont :
        - le texte de la nouvelle page actuelle est affiché dans le
            widget Text de l'interface
        - les étiquettes des boutons sont mises à jour pour refléter les
            options de la nouvelle page actuelle

        """
        page = self.PAGES.get(self.curr_page)
        if page.endPage:
            display = tw.fill(page.text, 100)
            self.append_to_path(self.curr_page)
            self.end_of_story(display)

        else :

            if not page:
                # si la page n'existe pas dans le dictionnaire,
                # afficher un message d'erreur
                display = "[Page missing]"
                options = ["", "", "", ""]
            else:
                # si la page existe, afficher son texte et ses options
                # dans le widget de texte et les boutons.
                display = tw.fill(page.text, 100)
                options = [
                    page.option1,
                    page.option2,
                    page.option3,
                    page.option4,
                ]
                # ajouter la page actuelle au chemin parcouru pour tenir
                # compte de la dimension temporelle de l'histoire
                self.append_to_path(self.curr_page)

                # ajouter un bouton pour afficher la météo
                # et l'heure de l'histoire
                weather_button = tk.Button(
                    self.window,
                    text = (f"Weather : {page.weather}\n"
                          f"Time : {page.time}"),
                    bg = "darkOliveGreen4",
                    fg = "black",
                    font = ("Helvetica", 12)
                )

                # configurer le bouton
                weather_button.grid(
                    row = 1,
                    column = 0,
                    columnspan = 2,
                    pady = 5,
                    padx = 5,
                    sticky = "W"
                )

                # mettre à jour le texte et les boutons avec les informations
                # definies plus tot    
                self.text.config(state = tk.NORMAL)
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, display)
                self.text.config(state = tk.DISABLED)

                for btn, label in zip(self.buttons, options):
                    btn.config(text = label)

    def on_button(self, index):
        """
        But : cette fonction gère les pressions de boutons et met à jour la
        page actuelle en fonction des transitions définies dans __init__.

        Entree self: le parametre self permet d'acceder aux variables qui
        sont normalement uniques a la fonction dans d'autres fonctions de
        la classe App.

        Entree index: le parametre index indique quel bouton a été appuyé
        (1 pour A, 2 pour B, 3 pour C, 4 pour D etc.)

        Les sorties de cette fonction sont :
        - la page actuelle est mise à jour en fonction du bouton appuyé
            et des transitions définies dans __init__. Si aucune
            transition n'est définie pour la page actuelle, la page reste
            inchangée.
        - la fonction update_view est appelée pour mettre à jour
        l'affichage en fonction de la nouvelle page actuelle.

        """
        transition = self.TRANSITIONS.get(self.curr_page)
        # si une transition est définie et que l'index du bouton
        # est valide superieur ou egal a 1, et inferieur ou egal
        # au nombre de transitions possibles (len)
        if transition and 1 <= index <= len(transition):
            self.curr_page = transition[index - 1]
    # s'il n'y a pas de transition définie,
    # ne rien faire (rester sur la page)
        self.update_view()


    def append_to_path(self, page):
        """
        But : cette fonction permet d'ajouter la page actuelle
        au chemin parcouru et l'imprimer dans la console.

        Entree self: le parametre self permet d'acceder aux variables
            qui sont normalement uniques a la fonction dans d'autres
            fonctions de la classe App.
        Entree page: le parametre page est le numero de la page
            actuelle qui doit etre ajoutee au chemin parcouru.

        Sorties : cette fonction n'a pas de sortie formelle, mais
        elle modifie la variable d'instance self.path en y ajoutant
        la page actuelle, et imprime le chemin dans la console.

        """
        self.path.append(page)
        print(self.path)

    
    def end_of_story(self, page):
        """
        But : cette fonction gère la fin de l'histoire. 
        Lorsque la page actuelle est une page de fin (endPage=True), 
        cette fonction est appelée pour afficher le texte de fin 
        et supprimer les boutons d'options.
        
        Entree self: le parametre self permet d'acceder aux variables qui 
            sont normalement uniques a la fonction dans d'autres
            fonctions de la classe App.
        Entree page: le parametre page est le numero de la page 
            de fin qui doit etre affichee.

        Sorties : la fonction modifie l'affichage de l'application
        pour montrer le texte de fin, et supprime les boutons
        d'options. Elle affiche aussi un message dans la console
        pour indiquer que la fin de l'histoire a été atteinte.

        """

        print("End of story reached.")
        # ajouter le texte dans le widget de texte
        self.text.config(state = tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, page)
        self.text.config(state = tk.DISABLED)
        # supprimer les boutons d'options
        for btn in self.buttons:
            btn.destroy()
        # ajouter un bouton pour indiquer que l'utilisateur
        # accepte la fin de l'histoire et peut fermer la fenetre
        end_button = tk.Button(self.window, text = "ok")
        end_button.config(
            height = 2, 
            width = self.BUTTON_SIZE,
            bg = "firebrick4",)
        end_button.grid(row = 1,
                        column = 0,
                        columnspan = 2,
                        pady = 5)
    # TODO: fin du code pertinent pour l'evaluation


# la partie suivante crée la fenetre principale de l'application, crée une
# instance de la classe App en lui passant cette fenetre,
# et lance la boucle principale de l'application pour que
# l'interface soit responsive et puisse réagir aux
# interactions de l'utilisateur.
root = tk.Tk()
app = App(root)
root.mainloop()





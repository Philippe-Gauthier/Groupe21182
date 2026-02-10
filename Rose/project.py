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
    Voici la plus grande partie du code. 
    La classe App gère l'état de l'application et l'interface utilisateur.

    Ici, vous allez trouver les fonctions suivantes :
    - __init__: Initialise l'application, crée l'interface utilisateur et définit les pages et les transitions.
    - update_view: Met à jour le texte affiché et les étiquettes des boutons en fonction de la page actuelle.
    - on_button: Gère les pressions de boutons et met à jour la page actuelle en fonction des transitions définies dans __init__.
    
    """

   

    def __init__(self, window):
        """
        :param self: le parametre self permet d'acceder aux variables qui sont normalement uniques a la fonction dans d'autres fonctions de la classe App.
        :param window: le parametre window est la fenetre principale de l'application tkinter. 
        lorsque l'on cree une instance de la classe App, on lui passe cette fenetre pour 
        qu'elle puisse y ajouter la fenetre dans laquelle l'application va s'executer.

        cette fonction initialise l'application, crée l'interface utilisateur et définit les pages et les transitions, donc ses sorties sont :
        - self.pages : un dictionnaire qui associe chaque numero de page a son objet page
        - self.transitions : un dictionnaire qui associe chaque numero de page a une liste de pages suivantes en fonction du bouton appuye
        - self.curr_page : le numero de la page actuelle
        - la configuration des elements de l'interface utilisateur (fenetre, texte et boutons)

        le but de cette fonction est de preparer l'application pour qu'elle puisse afficher la page initiale et repondre aux interactions de l'utilisateur.
        """
        self.window = window
        self.button_size = 67
        self.testmode = False
        self.testPage = 6
        self.path = []

        # ici on cree un "lexique" qui associe chaque numero de page a son objet page, provenant du fichier StrandedText.py
        self.pages = {
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
            40: st.p40
        }

        # ceci est un dictionnaire qui associe chaque numero de page a une liste de pages suivantes en fonction du bouton appuye (1 pour A, 2 pour B, 3 pour C, 4 pour D etc.)
        self.transitions = {
            1: (2, 3, 4, 5),
            2: (6, 10, 6, 11),
            3: (7, 9, 7, 13),
            4: (8, 8, 8, 8),
            5: (12, 14, 12, 14),
            6: (15, 16, 17, 18),
            7: (15, 16, 17, 18),
            8: (19, 20, 21, 22),
            9: (15, 16, 17, 18),
            10: (15, 16, 17, 18),
            11: (15, 16, 17, 18),
            12: (19, 20, 21, 22),
            13: (15, 16, 17, 18),
            14: (19, 20, 21, 22),
            # v end v
            15: (25, 26, 27, 28),
            16: (29, 30, 31, 32),
            17: (33, 34, 35, 36),
            18: (37, 38, 39, 40),
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
        if self.testmode:
            self.curr_page = self.testPage
        else : self.curr_page = 1

        # configuration de l'interface utilisateur : on cree un widget Text pour afficher le texte de la page, et des boutons pour les options. On configure aussi la fenetre (taille, titre, couleur de fond etc.)
        self.text = tk.Text(window, height=20, width=10, font=("Helvetica", 16))
        window.resizable(False, False)
        window.title("Livre")
        window.geometry("980x600")
        window.configure(bg="grey")

        self.text.grid(row=0, column=0, columnspan=2, sticky="NSEW", padx=5, pady=5)
        window.grid_rowconfigure(index=0, weight=0)
        window.grid_columnconfigure(index=0, weight=1)

        # creer les boutons et les placer dans la fenetre. Les boutons sont associes a la fonction on_button
        self.buttons = []
        for i in range(4):
            b = tk.Button(window, text="", command=lambda index=i + 1: self.on_button(index))
            b.config(height=2, width=self.button_size)
            self.buttons.append(b)

        # placer les boutons dans la fenetre en utilisant grid. Les boutons sont placés de manière à ce qu'ils soient alignés à gauche et à droite de la fenetre, avec un espacement entre eux.
        self.buttons[0].grid(row=1, column=0, sticky="E", padx=5, pady=5)
        self.buttons[1].grid(row=1, column=0, sticky="W", padx=5, pady=5)
        self.buttons[2].grid(row=2, column=0, sticky="E", padx=5, pady=5)
        self.buttons[3].grid(row=2, column=0, sticky="W", padx=5, pady=5)

        self.update_view()

    def update_view(self):
        """
        cette fonction met à jour le texte affiché et les étiquettes des boutons en fonction de la page actuelle.
        :param self: le parametre self permet d'acceder aux variables qui sont normalement uniques a la fonction dans d'autres fonctions de la classe App.
        les sorties de cette fonction sont :
        - le texte de la nouvelle page actuelle est affiché dans le widget Text de l'interface
        - les étiquettes des boutons sont mises à jour pour refléter les options de la nouvelle page actuelle

        """

        page = self.pages.get(self.curr_page)
        
        if not page:
            # gracefully handle missing pages
            display = "[Page missing]"
            options = ["", "", "", ""]
        else:
            display = tw.fill(page.text, 100)
            options = [page.option1, page.option2, page.option3, page.option4]
            self.appendToPath(self.curr_page)

        self.text.config(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, display)
        self.text.config(state=tk.DISABLED)

        for btn, label in zip(self.buttons, options):
            btn.config(text=label)

    def on_button(self, index):
        """
        cette fonction gère les pressions de boutons et met à jour la page actuelle en fonction des transitions définies dans __init__.
        :param self: le parametre self permet d'acceder aux variables qui sont normalement uniques a la fonction dans d'autres fonctions de la classe App.
        :param index: le parametre index indique quel bouton a été appuyé (1 pour A, 2 pour B, 3 pour C, 4 pour D etc.)
        les sorties de cette fonction sont :
        - la page actuelle est mise à jour en fonction du bouton appuyé et des transitions définies dans __init__. Si aucune transition n'est définie pour la page actuelle, la page reste inchangée.
        - la fonction update_view est appelée pour mettre à jour l'affichage en fonction de la nouvelle page actuelle.
        
        """
        transition = self.transitions.get(self.curr_page)
        if transition and 1 <= index <= len(transition):
            self.curr_page = transition[index - 1]
        # if no transition defined, do nothing (stay on page)
        self.update_view()
    
    def appendToPath(self, page):
        self.path.append(page)
        print(self.path)


# la partie suivante crée la fenetre principale de l'application, crée une instance de la classe App en lui passant cette fenetre, et lance la boucle principale de l'application pour que l'interface soit responsive et puisse réagir aux interactions de l'utilisateur.
root = tk.Tk()
app = App(root)
root.mainloop()





"""Rosemarie Dalton

Refactored main file for the "choose your own adventure" GUI.

Improvements applied:
- Replaced repeated if/elif navigation with a data-driven transitions table
- Encapsulated state in an App class (removes globals)
- Avoid repeated textwrap calls; wrap only when updating the displayed text
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
        """
        self.window = window
        self.button_size = 67

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
        }

        # transitions[page] = (next_if_button1, next_if_button2, ...)
        self.transitions = {
            1: (2, 3, 4, 5),
            2: (6, 10, 13, 16),
            3: (7, 11, 14, 17),
            4: (8, 8, 8, 8),
            5: (9, 12, 15, 18),
            # pages without explicit transitions will keep the same page
        }

        self.curr_page = 1

        # build UI
        self.text = tk.Text(window, height=20, width=10, font=("Helvetica", 16))
        window.resizable(False, False)
        window.title("Livre")
        window.geometry("980x600")
        window.configure(bg="grey")

        self.text.grid(row=0, column=0, columnspan=2, sticky="NSEW", padx=5, pady=5)
        window.grid_rowconfigure(index=0, weight=0)
        window.grid_columnconfigure(index=0, weight=1)

        # create buttons and attach index-based handlers
        self.buttons = []
        for i in range(4):
            b = tk.Button(window, text="", command=lambda index=i + 1: self.on_button(index))
            b.config(height=2, width=self.button_size)
            self.buttons.append(b)

        # place buttons (A/B share row 1, C/D share row 2, left/right alternation)
        self.buttons[0].grid(row=1, column=0, sticky="E", padx=5, pady=5)
        self.buttons[1].grid(row=1, column=0, sticky="W", padx=5, pady=5)
        self.buttons[2].grid(row=2, column=0, sticky="E", padx=5, pady=5)
        self.buttons[3].grid(row=2, column=0, sticky="W", padx=5, pady=5)

        self.update_view()

    def update_view(self):
        """Refresh the text and button labels for the current page."""
        page = self.pages.get(self.curr_page)
        if not page:
            # gracefully handle missing pages
            display = "[Page missing]"
            options = ["", "", "", ""]
        else:
            display = tw.fill(page.text, 100)
            options = [page.option1, page.option2, page.option3, page.option4]

        self.text.config(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, display)
        self.text.config(state=tk.DISABLED)

        for btn, label in zip(self.buttons, options):
            btn.config(text=label)

    def on_button(self, index):
        """Handle a button press (index in 1..4)."""
        transition = self.transitions.get(self.curr_page)
        if transition and 1 <= index <= len(transition):
            self.curr_page = transition[index - 1]
        # if no transition defined, do nothing (stay on page)
        self.update_view()



root = tk.Tk()
app = App(root)
root.mainloop()




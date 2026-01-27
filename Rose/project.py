"""
Rosemarie Dalton

Fichier principal pour le projet "un livre dont vous etes le heros"

"""

import tkinter as tk

newText = "hello"

def changetext() :
    newText = "\nthis is the new text"
    text.insert(tk.END, newText)
    
window = tk.Tk()
button = tk.Button(window, text="hello", command=changetext)
text = tk.Text(window, height=15, width=50)

window.title("Livre")
window.geometry("500x300")
window.configure(bg="grey")

initial_text = "This is a multi-line text area positioned \nwith the grid manager.\nIt will expand with the window."
text.insert(tk.END, initial_text)
text.grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)
window.grid_rowconfigure(6, weight=0)
window.grid_columnconfigure(0, weight=1)

button.grid(row=3, column=0)


#button.pack(side="bottom", pady=50)
#button.place(relx=0.45, rely=0.45)
#button.place(relx=0.45, rely=0.9)


window.mainloop()
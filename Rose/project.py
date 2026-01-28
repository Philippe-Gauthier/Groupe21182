"""
Rosemarie Dalton

Fichier principal pour le projet "un livre dont vous etes le heros"

use currPage to define what happens next: first loop simply starts the tree, bu then we can assign pages to the options instead of relying on the indexer

for example : button a is pressed for the first time : page is 2
button c is pressed : page is 6

so in button a, b, and c there are different options if the page was 2, and it sets the currPage to another unique id to continue this sequence

(yes, the fractal tree is gonna be insane since there are 4 options. yes, i will ask if i can make a text file to ppick from to keep this code cleaner)

if we want to change the story (inn future) simply add a class prefix or smt to be able to change aptly between stories

"""

import tkinter as tk
import StrandedText

buttonSize = 67

i = 0

currPage = 0



initialText = StrandedText.initialText
option1 = StrandedText.p1o1
option2 = StrandedText.p1o2
option3 = StrandedText.p1o3
option4 = StrandedText.p1o4

    
def button1Pressed() :
    global i
    global currPage
    i += 1
  
    if (i == 1) :
        currPage = 2
        
        newText = StrandedText.page2Text
        option1 = "Hope for the best"
        option2 = "Grab Theo's hand"
        option3 = "Pray"
        option4 = "Start crying"
        
        
    text.config(state=tk.NORMAL)
    text.delete('1.0', tk.END)
    text.insert(tk.END, newText)
    text.config(state=tk.DISABLED)
    buttonA.config(text=option1)
    buttonB.config(text=option2)
    buttonC.config(text=option3)
    buttonD.config(text=option4)
    
def button2Pressed() :
    global i
    global currPage
    i += 1
    
    if (i == 1) :
        currPage = 3
        
        newText = "You grab your towel and shampoo and walk to the shower room. You start the water and let the warmth engulf your cold skin. Nothing beats a nice warm shower to start your day. You wash your hair and \nscrub yourself clean, then enjoy a few more minutes under the hot water. Just as you're about to finish \ngetting dressed, the ship starts violently shaking. It feels like it crashed into something. You rapidly \nfinish putting your socks on, but there is not much you can do to help the situation."
        option1 = "Hope for the best"
        option2 = "Try to find your friends"
        option3 = "Pray"
        option4 = "Start crying"
        
        
    text.config(state=tk.NORMAL)
    text.delete('1.0', tk.END)
    text.insert(tk.END, newText)
    text.config(state=tk.DISABLED)
    buttonA.config(text=option1)
    buttonB.config(text=option2)
    buttonC.config(text=option3)
    buttonD.config(text=option4)
    
def button3Pressed() :
    global i
    global currPage
    i += 1
    
    if (i == 1) :
        currPage = 4
        print("mlem")
        
        
    text.config(state=tk.NORMAL)
    text.delete('1.0', tk.END)
    text.insert(tk.END, newText)
    text.config(state=tk.DISABLED)
    buttonA.config(text=option1)
    buttonB.config(text=option2)
    buttonC.config(text=option3)
    buttonD.config(text=option4)
    
def button4Pressed() :
    global i
    global currPage
    i += 1
    
    if (i == 1) :
        currPage = 5
        print("meep")
        
        
    text.config(state=tk.NORMAL)
    text.delete('1.0', tk.END)
    text.insert(tk.END, newText)
    text.config(state=tk.DISABLED)
    buttonA.config(text=option1)
    buttonB.config(text=option2)
    buttonC.config(text=option3)
    buttonD.config(text=option4)
    
window = tk.Tk()


text = tk.Text(window, height=20, width=10, font=("Helvetica", 16))

window.resizable(False, False)

window.title("Livre")
window.geometry("980x600")
window.configure(bg="grey")


# initial_text = "This is a multi-line text area positioned \nwith the grid manager.\nIt will expand with the window."
# text.insert(tk.END, initial_text)
text.grid(row=0, column=0, columnspan=2, sticky="NSEW", padx=5, pady=5)
window.grid_rowconfigure(index=0, weight=0)
window.grid_columnconfigure(index=0, weight=1)


buttonA = tk.Button(window, text=option1, command=button1Pressed)
buttonB = tk.Button(window, text=option2, command=button2Pressed)
buttonC = tk.Button(window, text=option3, command=button3Pressed)
buttonD = tk.Button(window, text=option4, command=button4Pressed)

buttonA.grid(row=1, column=0, sticky="E", padx=5, pady=5)
buttonA.config(height=2, width=buttonSize)

buttonB.grid(row=1, column=0, sticky="W", padx=5, pady=5)
buttonB.config(height=2, width=buttonSize)

buttonC.grid(row=2, column=0, sticky="E", padx=5, pady=5)
buttonC.config(height=2, width=buttonSize)

buttonD.grid(row=2, column=0, sticky="W", padx=5, pady=5)
buttonD.config(height=2, width=buttonSize)

text.insert(tk.END, initialText)

text.config(state=tk.DISABLED)
window.mainloop()



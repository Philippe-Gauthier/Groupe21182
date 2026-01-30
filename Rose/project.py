"""
Rosemarie Dalton

Fichier principal pour le projet "un livre dont vous etes le heros"

use currPage to define what happens next: first loop simply starts the tree, bu then we can assign pages to the options instead of relying on the indexer

for example : button a is pressed for the first time : page is 2
button c is pressed : page is 6

so in button a, b, and c there are different options if the page was 2, and it sets the currPage to another unique id to continue this sequence

(yes, the fractal tree is gonna be insane since there are 4 options.)

if we want to change the story (inn future) simply add a class prefix or smt to be able to change aptly between stories

"""
import textwrap as tw
import tkinter as tk
import StrandedText as st

buttonSize = 67

i = 0

currPage = 0



newText = tw.fill(st.p1.text, 100)
option1 = st.p1.option1
option2 = st.p1.option2
option3 = st.p1.option3
option4 = st.p1.option4

def setOptions(page) :
    global option1
    global option2
    global option3
    global option4
    global newText
    newText = page.text
    option1 = page.option1
    option2 = page.option2
    option3 = page.option3
    option4 = page.option4

def updateText() :
    text.config(state=tk.NORMAL)
    text.delete('1.0', tk.END)
    text.insert(tk.END, tw.fill(newText, 100))
    text.config(state=tk.DISABLED)
    buttonA.config(text=option1)
    buttonB.config(text=option2)
    buttonC.config(text=option3)
    buttonD.config(text=option4)

    
def button1Pressed() :
    global i
    global currPage
 
    i += 1
  
    if (i == 1) :
        currPage = 2 
        setOptions(st.p2)
    elif (currPage == 2) :
        currPage = 6
        setOptions(st.p6)
    elif (currPage == 3) :
        currPage = 7
        setOptions(st.p7)
    elif (currPage == 4) :
        currPage = 8
        setOptions(st.p8)
    elif (currPage == 5) :
        currPage = 9
        setOptions(st.p9)

        
        
    updateText()
    
def button2Pressed() :
    global i
    global currPage

    i += 1
    
    if (i == 1) :
        currPage = 3
        setOptions(st.p3)
    elif (currPage == 2) :
        currPage = 10
        setOptions(st.p10)
    elif (currPage == 3) :
        currPage = 11
        setOptions(st.p11)
    elif (currPage == 4) :
        currPage = 12
        setOptions(st.p12)
    elif (currPage == 5) :
        currPage = 13
        setOptions(st.p13)

    updateText()
    
def button3Pressed() :
    global i
    global currPage

    i += 1
    
    if (i == 1) :
        currPage = 4
        setOptions(st.p4)   
        
    updateText()
    
def button4Pressed() :
    global i
    global currPage

    i += 1
    
    if (i == 1) :
        currPage = 5
        setOptions(st.p5)
        
    updateText()





    
window = tk.Tk()


text = tk.Text(window, height=20, width=10, font=("Helvetica", 16))

window.resizable(False, False)

window.title("Livre")
window.geometry("980x600")
window.configure(bg="grey")


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

text.insert(tk.END, newText)

text.config(state=tk.DISABLED)
window.mainloop()



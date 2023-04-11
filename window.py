# import the modules
import tkinter
import random
from tkinter import *
from tkinter.ttk import *


class Wordle:
    lives = 5   #lives to guess the word
    count = 0   # if count == 5, You win    
    mystery_word = {} #random word chosed from words.txt
    rand = 0 #random word gen
         
def startGame(event):
    global s1    
    
    global letters_guess
    
    lives = s1.lives
    letter = event.char
    
    if len(str(letter)) > 2:
        wrong = tkinter.Label(jorge, text = "One letter at a time",font = ('Helvetica', 12))
        wrong.pack()
    elif letter == "":
        label_word.config(text=letters_guess)
        letters_box.delete(0,3)
    else:
        print(f"{letter} was pressed")
        # for i in range(s1.rand,(s1.rand)+5):
        #     s1.mystery_word[(i%6)] = words[i];
        
        if letter in s1.mystery_word.values():
            for j in range(0,5):
                if letter == s1.mystery_word[j]:
                    letters_guess = letters_guess[:(j*2)] + letter + letters_guess[(j*2)+1:]
                    s1.count = s1.count + 1
        else:
            lives = lives - 1
            lives_counter.config(text = f"Lives left: {lives}")

                             
# Driver Code
# create a GUI window
jorge = Tk()

global s1
s1 = Wordle()

global letters_guess
letters_guess = "_ _ _ _ _"

with open("words.txt","r+") as k:
        words = k.read()

s1.rand = 6 * (random.randint(0,5757))

for i in range(s1.rand,(s1.rand)+5):
    s1.mystery_word[(i%6)] = words[i];
    
print(s1.mystery_word)

# set the title
jorge.title("Wordle")
 
# set the size
jorge.geometry("375x200")
 
# add an instructions label
instructions = tkinter.Label(jorge, text = "Guess a letter in the word!",font = ('Helvetica', 12))
instructions.pack()

 
# add a lives left label
lives_counter = Label(jorge, text = f"Lives left: {s1.lives}", font = ('Helvetica', 12))   
lives_counter.pack()
 
# add a label for displaying the word
label_word = tkinter.Label(jorge, text=letters_guess, font = ('Helvetica', 60))
label_word.pack()
 
#text box for inputing letters
letters_box = tkinter.Entry(jorge)
letters_box.pack()

jorge.bind('<Key>',startGame)

# start the GUI
jorge.mainloop()


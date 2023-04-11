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
    letter = ""
    
    if event == "<Return>" or event == "": 
        clear("")
    else:
        letter = str(event)
        print(f"{letter} was pressed")
        for i in range(s1.rand,(s1.rand)+5):
            s1.mystery_word[(i%6)] = words[i];
        
        if letter in s1.mystery_word.values():
            for j in range(0,5):
                if letter == s1.mystery_word[j]:
                    letters_guess = letters_guess[:(j*2)] + str(letter) + letters_guess[(j*2)+1:]
                    s1.count = s1.count + 1
        elif letter not in s1.mystery_word.values():
            lives = lives - 1
    
        print(letters_guess)
        print(f'lives: {lives}')

        

def clear(ans):
    return letters_box.delete(0,END) 
                             
# Driver Code
# create a GUI window
jorge = Tk()

global s1
s1 = Wordle()

global letters_guess
letters_guess = "_ _ _ _ _"

with open("words.txt","r+") as k:
        words = k.read()

#s1.rand = 6 * (random.randint(0,5757))
s1.rand = 6

# set the title
jorge.title("Wordle")
 
# set the size
jorge.geometry("375x200")
 
# add an instructions label
instructions = tkinter.Label(jorge, text = "Guess a letter in the word!",font = ('Helvetica', 12))
instructions.pack()
 
# start game label
start_game = tkinter.Label(jorge, text = "Press enter to start",font = ('Helvetica', 12))
start_game.pack()
 
# add a lives left label
lives_counter = Label(jorge, text = f"Lives left: {s1.lives}", font = ('Helvetica', 12))   
lives_counter.pack()
 
# add a label for displaying the word
label_word = tkinter.Label(jorge, font = ('Helvetica', 60))
label_word.pack()
 
#text box for inputing letters
letters_box = tkinter.Entry(jorge)
letters_box.pack()
 
startGame("")
jorge.bind("<Key>",startGame)
# startGame("e")
# startGame("t")
# startGame("h")
# startGame("r")

# start the GUI
jorge.mainloop()


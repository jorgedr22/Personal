# import the modules
import tkinter
import random
from tkinter import *
from tkinter.ttk import *


class Wordle:
    lives = 5   #lives to guess the word
    count = 0   # if count == 5, You win    
    guess = {}  # keeps track of users guessed letters
    mystery_word = {} #random word chosed from words.txt
    rand = 0 #random word gen
         
def startGame(event):
    global s1    
        
    letters_guess = "_ _ _ _ _"
    letter = ""
    
    if event == 'go': 
        print("Game start")
    else:
        letter = event.char
        print(f"{letter} was pressed")
    
    for i in range(s1.rand,(s1.rand)+5):
        s1.mystery_word[i] = words[i];
    
    print(str(s1.mystery_word))
    
    while s1.lives>0:
        if letter in s1.mystery_word.values():
            for j in range(s1.rand,(s1.rand)+5):
                if letter == s1.mystery_word[j]:
                    letters_guess = letters_guess[:((j%6)*2)] + letter + letters_guess[(((j%6)*2)+1):]
                    s1.count += 1
        else:
            s1.lives -= 1
        label_word.config(text=letters_guess)
        lives_counter.config(text=f'{s1.lives}')
        clear()

def clear():
    letters_box.delete(0,END)            
                       
# Driver Code
# create a GUI window
jorge = Tk()

global s1
s1 = Wordle()

with open("words.txt","r+") as k:
        words = k.read()

s1.rand = 6 * (random.randint(0,5757))

# set the title
jorge.title("Wordle")
 
# set the size
jorge.geometry("375x200")
 
# add an instructions label
instructions = tkinter.Label(jorge, text = "Guess a letter in the word!",font = ('Helvetica', 12))
instructions.pack()
 
# start game label
start_game = tkinter.Label(jorge, text = "Press enter to start",
                                      font = ('Helvetica', 12))
start_game.pack()
 
# add a lives left label
lives_counter = tkinter.Label(jorge, text = f"Lives left: {s1.lives}", font = ('Helvetica', 12))
               
lives_counter.pack()
 
# add a label for displaying the word
label_word = tkinter.Label(jorge, font = ('Helvetica', 60))
label_word.pack()
 
startGame('go')
jorge.bind('<Key>',startGame)

#text box for inputing letters
letters_box = Entry(jorge)
letters_box.pack()

# start the GUI
jorge.mainloop()

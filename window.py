# import the modules
import tkinter
import random
from tkinter import *
from tkinter.ttk import *


class Wordle:
    lives = 0   #lives to guess the word
    count = 0   # if count == 5, You win    
    mystery_word = {} #random word chosed from words.txt
    rand = 0 #random word gen
         
def startGame(event):
    global s1    
    s1.lives = 5
    
    letters_guess = "_ _ _ _ _"
    letter = ""
    
    if event == 'go': 
        print("Game start")
        update(letters_guess,str(s1.lives))
    else:
        letter = event.char
        print(f"{letter} was pressed")
    
    for i in range(s1.rand,(s1.rand)+5):
        s1.mystery_word[i] = words[i];
    
    print(str(s1.mystery_word))
    
    while s1.lives > 0 and s1.count<5:
        if letter in s1.mystery_word.values():
            for j in range(s1.rand,(s1.rand)+5):
                if letter == s1.mystery_word[j]:
                    letters_guess = letters_guess[:((j%6)*2)] + str(letter) + letters_guess[(((j%6)*2)+1):]
                    s1.count += 1
        else:
            s1.lives -= 1           
        update(letters_guess,s1.lives)

def clear(event):
    letters_box.delete(0,END) 
               
   
def update(ans,lives):
    label_word['text'] = ans
    lives_counter['text'] = lives
                        
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
lives_counter = Label(jorge, text = f"Lives left: {s1.lives}", font = ('Helvetica', 12))
               
lives_counter.pack()
 
# add a label for displaying the word
label_word = tkinter.Label(jorge, font = ('Helvetica', 60))
label_word.pack()
 
startGame('go')

#text box for inputing letters
letters_box = Entry(jorge)
letters_box.pack()
jorge.bind('<Key>',startGame)
jorge.bind('<Return>',clear)
# start the GUI
jorge.mainloop()


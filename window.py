# import the modules
import tkinter
import random
from tkinter import *
from tkinter.ttk import *
import sys
import os

class Wordle:
    lives = 5   #lives to guess the word
    count = 0   # if count == 5, You win    
    mystery_word = {} #random word chosed from words.txt
    word = ""
    rand = 0 #random word gen
    temp = ""
    
         
def startGame(event):
    global s1    
    global letters_guess
    
    letter = event.char
    
    
    if len(str(letter)) > 2: #input more than two letters
        wrong = tkinter.Label(jorge, text = "One letter at a time",font = ('Helvetica', 12))
        wrong.pack()
        
    elif event.keysym == "Return" and s1.temp in s1.mystery_word.values(): #submit a guess and the guess is in the word
        for j in range(0,5):
            if s1.temp == s1.mystery_word[j]:
                letters_guess = letters_guess[:(j*2)] + s1.temp + letters_guess[(j*2)+1:]
                s1.count = s1.count + 1
        label_word.config(text=letters_guess)
        letters_box.delete(0,END)
        if s1.count == 5:
            with open("/Users/jorgedelriocuriel/Desktop/Personal/fireworks.py") as k:
                exec(k.read())
        
    elif event.keysym == "Return" and s1.temp not in s1.mystery_word.values(): #submit a guess and the guess is not in the word 
        label_word.config(text=letters_guess)
        s1.lives -= 1
        lives_counter.config(text=f'Lives left: {s1.lives}')
        letters_box.delete(0,END)
        if s1.lives == 0:
            label_word.config(text="You lose!\nThe word was\n"+s1.word)
            
    elif event.keysym == "Return": # only press enter
        print("")
    
    elif letter:
        s1.temp = letter
        
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
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

for i in range(s1.rand,s1.rand+5):
    s1.mystery_word[(i%6)] = words[i];

for i in range(s1.rand,s1.rand+5):
    s1.word = s1.word[:(i%6)] + str(words[i]) + s1.word[(i%6)+1:]

# set the title
jorge.title("Wordle")

# set the size
jorge.geometry("500x500")

# add an instructions label
instructions = tkinter.Label(jorge, text = "Guess a letter in the word!",font = ('Helvetica', 18))
instructions.pack()

restart = Button(jorge, text="Restart", command=restart_program)
restart.pack(side=tkinter.BOTTOM)

# add a lives left label
lives_counter = Label(jorge, text = f"Lives left: {s1.lives}", font = ('Helvetica', 18))   
lives_counter.pack()

# add a label for displaying the word
label_word = tkinter.Label(jorge, text=letters_guess, font = ('Helvetica', 60))
label_word.pack()

#text box for inputing letters
letters_box = tkinter.Entry(jorge)
letters_box.focus_set()
letters_box.pack()

jorge.bind('<Key>',startGame)
print(s1.word)
# start the GUI
jorge.mainloop()


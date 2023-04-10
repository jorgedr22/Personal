# import the modules
import tkinter
import random
#import wordle as wd
# function that will start the game.

class Wordle:
    lives = 2   #lives to guess the word
    count = 0   # if count == 5, You win    
    guess = {}  # keeps track of users guessed letters
    mystery_word = {} #random word chosed from words.txt
         
def startGame():
    global s1
    with open("words.txt","r+") as k:
        words = k.read()
        
    letters_guess = "_ _ _ _ _"
    
    op = random.randint(0,5757)
    op = op * 6
    
    for i in range(op,op+5):
        s1.mystery_word[i] = words[i];
    
    print(str(s1.mystery_word))
    
    while s1.lives>0:
        if e.get().lower in s1.mystery_word.values():
            for j in range(op,op+5):
                if e.get().lower == s1.mystery_word[j]:
                    letters_guess = letters_guess[:((j%6)*2)] + e + letters_guess[(((j%6)*2)+1):]
                    s1.count += 1
                    e.delete(0,tkinter.END)
                    #label_word.config(text=letters_guess)
                    print(letters_guess)
        else:
            s1.lives -= 1
            e.delete(0,tkinter.END)
            #label_word.config(text=letters_guess)
            print(letters_guess)

            
                       
# Driver Code
# create a GUI window
root = tkinter.Tk()

global s1
s1 = Wordle()
# set the title
root.title("Wordle")
 
# set the size
root.geometry("375x200")
 
# add an instructions label
instructions = tkinter.Label(root, text = "Guess a letter in the word!",font = ('Helvetica', 12))
instructions.pack()
 
# start game label
start_game = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12))
start_game.pack()
 
# add a lives left label
lives_counter = tkinter.Label(root, text = f"Lives left: {s1.lives}", font = ('Helvetica', 12))
               
lives_counter.pack()
 
# add a label for displaying the word
label_word = tkinter.Label(root, font = ('Helvetica', 60))
label_word.pack()
 
# add a text entry box for
# typing in letters
e = tkinter.Entry(root)
 

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame())
e.pack()
 
# set focus on the entry box
e.focus_set()
 
# start the GUI
root.mainloop()

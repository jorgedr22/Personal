import random
import os
import sys
from tkinter import *
from tkinter.ttk import *
from collections import OrderedDict
import time
import fireworks  
import pygame
pygame.init()

master = Tk() 
# sets the geometry of main
# root window
master.geometry("200x200")
 
 
# function to open a new window
# on a button click
def openNewWindow():

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,text ="This is a new window").pack()


label = Label(master,text ="This is the main window")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(master,text ="Click to open a new window",command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

# def start_game(mystery_word,op):
#      print("The word is:\n")
#      print('_ _ _ _ _')

#      Op = 6*op;
#      for i in mystery_word:
#         print(mystery_word[i],end="")
#      print("")
    
#      string_letters = "_ _ _ _ _"
#      final_ans =""
#      trys=10;
#      count=0
    
#      while trys>0:
#          inp = input("Guess a letter:")
    
#          if inp in mystery_word.values():
#              os.system("clear")
#              for j in range(Op,Op+5):
#                  if inp == mystery_word[j]:
#                      #string_letters = string_letters[:(j%6)] + inp + string_letters[((j%6)+1):]
#                      string_letters = string_letters[:((j%6)*2)] + inp + string_letters[(((j%6)*2)+1):]
#                      count += 1                
#          else:
#              trys -= 1
#              print("Life lost! Lives left:"+str(trys)+"\n")
         
#          if(count<5):               
#             print("The word is:\n" + string_letters)
#          elif(count == 5):
#             final_ans = string_letters.replace(" ","")
#             print("You guessed the word!\n"+final_ans)
#             time.sleep(3)
#             break
#      fireworks.start()
            
                
# def game():
#     with open("words.txt","r+") as k:
#         words = k.read()
    
#     op = random.randint(0,5757)
#     guess = {}

#     for i in range((op*6),(op*6)+5):
#         guess[i] = words[i];
    
#     print("Welcome to Wordle!")
#     rule = input("Would you like to read the rules of the game?\n")
#     if rule.capitalize() == "Yes":
#         os.system('clear')
#         rules_of_game(guess,op)
#     else:
#         os.system('clear')        
#         start_game(guess,op)

# def rules_of_game(mystery_word,op):
#     print("Guess any letter in the English Alphabet to fill up the word. You have 10 trys before you lose the game. Good luck!")
#     start_game(mystery_word,op)
        
# while 1:
#     os.system('clear')  
#     start = input("Would you like to play wordle?\n")

#     if start.capitalize() == "Yes":
#         game()
#         os.system('clear')
#     else:
#         os.system('clear')
#         print("See you later")
#         break
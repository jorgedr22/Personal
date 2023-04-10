import random
import os
import sys
from collections import OrderedDict
import time
import fireworks
import pygame
pygame.init()
def start_game(mystery_word,op):
    print("The word is:\n")
    print('_ _ _ _ _')

    Op = 6*op;
    for i in mystery_word:
        print(mystery_word[i],end="")
    print("")
    
    string_letters = "_____"
    trys=10;
    count=0
    
    while trys>0:
        inp = input("Guess a letter:")
    
        if inp in mystery_word.values():
            os.system("clear")
            for j in range(Op,Op+5):
                if inp == mystery_word[j]:
                    string_letters = string_letters[:(j%6)] + inp + string_letters[((j%6)+1):]
                    count+=1                
        else:
            trys -= 1
            print("Life lost! Lives left:"+str(trys)+"\n")
                        
        print("The word is:\n" + string_letters)
        if(count == 5):
            fireworks.start()
            
    print("You lost!")
    time.sleep(10)
                
def game():
    with open("words.txt") as w:
        words = w.read()

    op = random.randint(0,5757)
    guess = {}
    
    for i in range((op*6),(op*6)+5):
        guess[i] = words[i];
        
    print("Welcome to Wordle!")
    rule = input("Would you like to read the rules of the game?")
    if rule.capitalize() == "Yes":
        os.system('clear')
        rules_of_game(guess,op)
    else:
        os.system('clear')        
        start_game(guess,op)

def rules_of_game(mystery_word,op):
    print("Guess any letter in the English Alphabet to fill up the word. You have 10 trys before you lose the game. Good luck!")
    start_game(mystery_word,op)

while 1:
    os.system('clear')
    start = input("Would you like to play wordle?\n")

    if start.capitalize() == "Yes":
        os.system('clear')
        game() 
    else:
        os.system('clear')
        print("See you later")
        break
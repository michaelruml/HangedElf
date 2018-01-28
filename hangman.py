import random
file = open("words.csv", "r") 
word_list = file.read()
word_split = word_list.split("_")

from random import randrange
random_index = randrange(0,len(word_split))
word  = word_split[random_index]

hidden_word = []
for x in range(len(word)):
    hidden_word.append("_")
letters = list(word) #seznam písmen

print(hidden_word) #prázdný seznam písmen
lives = 0

def hangman_1():
    """
    /-----
    |    | 
    | 
    |
    |    
    |________"""

def hangman_2():
    """
    /-----
    |    | 
    |    O
    |
    |    
    |________"""

def hangman_3():
    """
    /-----
    |    | 
    |    O
    |   /|\
    |    
    |________"""

def hangman_4():
    """
    /-----
    |    | 
    |    O
    |   /|\
    |    /\ 
    |________"""


while hidden_word != letters:
    input_letter = input("What letter are you guessing?:")
    if len(input_letter) == 0:
        print("You should probably wrtie something")
    elif len(input_letter) >= 1:
        print("Write just one letter, not an entire essay")
    else:
        while input_letter in letters:
            position = letters.index(input_letter)
            hidden_word[position] = input_letter
            letters[position] = "."

            print(hidden_word)

        if hidden_word == letters:
            print("Congratulations, you have won (well, this round)")
        else:
            print("Wrong letter")
            lives = lives + 1
           
            if lives == 1:
                print(hangman_1)
            elif lives == 2:
                print(hangman_2)
            elif lives == 3:
                print(hangman_3)
            elif lives == 4:
                print(hangman_4)
            
            print(hidden_word)

            

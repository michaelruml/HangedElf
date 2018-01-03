import random
file = open("words.csv", "r") 
word_list = file.read()
print(word_list)
word_split = word_list.split("_")
print(word_split)
from random import randrange
random_index = randrange(0,len(word_split))
word  = word_split[random_index]
print(word)
#hidden_word = ["_ "*len(word)]
hidden_word = []
for x in range(len(word)):
    hidden_word.append("_")

letters = list(word)  #seznam vytvořený z jendnotlivych písmen ve slove ##vyřeším to potom    

print(hidden_word) #_ _ _ _

playing = "yes"

lives = 0

while playing == "yes" :
    while hidden_word != letters:
        input_word = input("what letter are you guessing?:")
        if len(input_word) == 0:
            print("You  didnt write anything")
        elif len(input_word) != 1:
            print("write just one letter, not a whole essay")
        elif len(input_word) == 1:
            if input_word in letters:
                position = word.index(input_word)
                hidden_word[position] = input_word
                
                print(hidden_word)
            else:
                print(hidden_word)
                print("wrong letter")
                lives = lives + 1
                print("You have ", lives, " left.")
                if lives == 4:
                    print("you lost")
                    playing = input("Play again?(yes or no)")
                       #tohle z nějakého důvodu nefunguje ##if playing != "yes" :
                           # print("end of the game")
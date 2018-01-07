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

letters = list(word)  #seznam vytvořený z jendnotlivych písmen ve slove ##vyřeším to potom    


def lives1():
    print("/-----")
    print("|    |") 
    print("|    ") 
    print("|    ")
    print("|    ")
    print("|________")


def lives2():
    print("/-----")
    print("|    |")
    print("|    O") 
    print("|    ")
    print("|     ")
    print("|________")


def lives3():
    print("/-----")
    print("|    |")
    print("|    O") 
    print("|   /|\ ")
    print("|     ")
    print("|________")



def lives4():
    print("/-----")
    print("|    |")
    print("|    O") 
    print("|   /|\ ")
    print("|    /\ ")
    print("|________")


print(hidden_word) #_ _ _ _
lives = 0
playing = "yes"

while playing == "yes" :
    while hidden_word != letters:
        input_letter = input("what letter are you guessing?:")
        if len(input_letter) == 0:
            print("You  didnt write anything")
        elif len(input_letter) != 1:
            print("write just one letter, not a whole essay")
        elif len(input_letter) == 1:
            if input_letter in letters:
                position = word.index(input_letter)
                hidden_word[position] = input_letter 
                print(hidden_word)
                if hidden_word == letters:
                        print("Congratuations, you won!")
                        playing = input("type yes if you wish to continue:")
                        if playing != "yes":
                                print("end of the game it seems")                             
            else:
                print(hidden_word)
                print("wrong letter")
                lives = lives + 1
                print("You have ", lives, " left.")
                if lives == 4:
                    print("you lost")
                    print(lives4)
                    playing = input("Play again?(yes or no)")
                       #tohle z nějakého důvodu nefunguje ##if playing != "yes" :
                           # print("end of the game")

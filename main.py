word = "auto"
hidden_word = ["_ "*len(word)]
letters = list(word)  #seznam vytvořený z jendnotlivych písmen ve slove ##vyřeším to potom    

print(hidden_word) #_ _ _ _

playing = "yes"

lives = 0
hangman_0 = "you have 4 lives left"
hangman_1 = "you have 3 lives left"
hangman_2 = "you have 2 lives left"
hangman_3 = "you have 1 life left"
hangman_4 = "you have 0 lives left"

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
                if lives == 0:
                    print(hangman_0)
                elif lives == 1:
                    print(hangman_1)
                elif lives == 2:
                    print(hangman_2)
                elif lives == 3:
                    print(hangman_3)
                elif lives == 4:
                    print(hangman_4)
                    print("you lost")
                    playing = input("Play again?(yes or no)")
                       #tohle z nějakého důvodu nefunguje ##if playing != "yes" :
                           # print("end of the game")
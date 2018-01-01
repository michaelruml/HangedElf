word = "auto" #slovo hledané #seznamslov #importnu to později
hidden_word = ["_ "*len(word)]
print(hidden_word) #_ _ _ _
letters = list(word)  #seznam vytvořený z jendnotlivych písmen ve slove ##vyřeším to potom 
word_string = str(word)   
playing = "yes"
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
                #každý hangman bude mít svoji hodnotu od 0 po 5 (nebo něco) 
                print(hidden_word)
                print("wrong letter")
                lives = lives + 1
                    if lives == 0:
                        print(hangman_0)
                    elif lives == 1:
                        print(hangman_1)
                    elif lives == 2
                        print(hangan_2)
                    elif lives == 3:
                        print(hangman_3)
                    elif lives == 4:
                        print(hangman_4)
                        print("you lost")
                        playing = input("Play again?(yes or no)")     
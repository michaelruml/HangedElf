word = "auto" #slovo hledané #seznamslov #importnu to později
hidden_word = ["_ "*len(word)]
print(hidden_word) #_ _ _ _
letters = list(word)  #seznam vytvořený z jendnotlivych písmen ve slove ##vyřeším to potom 
hangman = print("a") 
word_string = str(word)
while playing == yes:
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
                print(hangman)
                print(hidden_word)
                    if hidden_word == letters:
                        playing = input("do you wish to play again?(if you dont type yes, this thing is going to crash I think)")
            else:
                print(hangman) #každý hangman bude mít svoji hodnotu od 0 po 5 (nebo něco) 
                print(hidden_word)
                print("wrong letter")
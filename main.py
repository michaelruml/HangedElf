word = "auto" #slovo hledané #seznamslov #importnu to později
hidden_word = ["_ "*len(word)]
print(hidden_word) #_ _ _ _
letters = list(word)  #seznam vytvořený z jendnotlivych písmen ve slove ##vyřeším to potom 
hangman = print("a") 
word_string = str(word)
while hidden_word != letters:
    input_word = input("what letter are you guessing?:")
    if len(input_word) == 0:
       print("Yout didnt write anything")
    elif len(input_word) >= 1:
        print("write just one letter, not a whole essay")

    position = word.index(input_word) 
    if input_word in letters:
        print(hangman)
        hidden_word[position] = input_word
        print(hidden_word)
    else:
        print("wrong letter")
        print(hangman) #každý hangman bude mít svoji hodnotu od 0 po 5 (nebo něco) 
        print(hidden_word)
    
# vyřeším později   
# on/off = input("do you wish to plaz again?": )  #input pro x





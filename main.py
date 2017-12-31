word = words.csv #seznamslov
hidden_word = "_ "*len(word)
print(hidden_word)
letters = list(word)  #seznam vytvořený z jendnotlivych písmen ve slove ##vyřeším to potom 

input_word = input("what letter are you guessing?:")
if len(input_word) == 0:
    print("Yout didnt write anything")
elif len(input_word) >= 1:
    print("write just one letter, not a whole essay")

if input_word in list:
    print(hangman)
    hidden_word[letters[input_word]] == input_word
    print(hidden_word)
    
    print("wrong letter")
    hangman = hangman + 1
    print(hangman) #každý hangman bude mít svoji hodnotu od 0 po 5 (nebo něco) 
    print(hidden_word)
    
# vyřeším později   
# on/off = input("do you wish to plaz again?": )  #input pro x
x = yes
x = input("do you wish to play agiain(type yes or no):")
if x != yes:
        print("youre a dumbass")




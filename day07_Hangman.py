import random
import hangman_words

# if you want just import a specific things from the file the we use 
# from hangman_words import word_list

# word_list = ["raihan", "kabir", "hridoy"]

chosen_word = random.choice(hangman_words.word_list) 
# chosen_word = random.choice(word_list)  #if we import via from then we use it 
print(chosen_word)
length = len(chosen_word)

placeholder = ""
for position in range(length):
    placeholder += "_"

print(placeholder)

correct_letters = []
lives = 6
while length > -6:
    guess = input("Guess a letter : ").lower()

    if guess in correct_letters:
        print(f"You already guess this --> {guess} letter")
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter  
        else:
            display += "_"
    
    print(display)

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            print("You lost")
            break
    
    print(f"you have {lives}/{6} life remaining .....")

    if "_" not in display:
        print("You win")
        break
    

    
    length -= 1






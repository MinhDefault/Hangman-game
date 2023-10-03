import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
from replit import clear

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for i in chosen_word:
    display.append("_")
lives = 6
check = True 
while check:
    guess = input("Type a letter: ")
    # index_list = 0
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    print(f"You guessd: {guess}")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            if "_" not in display:
                check = False
                print("You win.")
    


        # else:
        #     lives -= 1
        #     print("You type a letter not matches word")
        #     if lives == 0:
        #         check = False
        #         print("You lose.")
    if guess not in chosen_word:
        lives -= 1
        print("You type a letter not matches with word")
        if lives == 0:
            check = False
            print("You lose.")
    print(stages[lives])
    # print(f"You guessd: {guess}")
            
        
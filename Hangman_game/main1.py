from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
import random
from replit import clear


def play_game():
    print(logo)
    display = []
    lives = 6
    chosen_word = random.choice(word_list)
    print(chosen_word)
    for i in chosen_word:
        display += "_"
    # print(display)
    end_game = False
    while not end_game :
        guess = input("Guess a letter")
        
        clear()
        if guess in display:
            print(f"You've already guessed {guess}")
        position = 0
        print(f"You guessed letter:{guess}")
        for i in chosen_word:
            if guess == i:
                display[position] = guess 
                position += 1   
            
      
                
                if "_" not in display:
                    print("You win")
                    end_game = True

        if guess not in chosen_word:
            lives -= 1
            print("You type a letter not matches with word")
            if lives == 0:
                print("You lose")
                end_game = True  
        print(display)     
        print(stages[lives])    




play_again = True
while play_again:
    play_game()
    check = input("Do you want to play again?")
    if check == "no":
        play_again = False
        print("tam biet") 


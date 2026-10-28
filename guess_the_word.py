# Jesse Butcher
# CIS256 Fall 2026
# Programming Assignment 4

#importing a random to select my random word for game
import random

def play():
    
# my list of random words for game
 words = ['pig', 'dog', 'cat', 'cow']

 random_word = random.choice(words)

#setting input guides for game

 guessed_letters = []
 incorrect_letters = []
 incorrect_guesses = 0
 max_attempts = 5

 displayed_word = ["_"] * len(random_word)

#prints the game title

 print(' Guess the word ')

 #while loop for the guessing parameters

 while incorrect_guesses < max_attempts and "_" in displayed_word:
    print("\nword:", " ".join(displayed_word))
    print("correct guesses:", ", ".join(guessed_letters))
    print("incorrect guesses:", ", ".join(incorrect_letters))
    print(f"attempts left: {max_attempts - incorrect_guesses}")

    guess = input("Enter a letter: ").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("Enter a valid letter A-Z")
        continue

    if guess in guessed_letters or guess in incorrect_letters:
        print("Incorrect letter guess again!")
        continue

    if guess in random_word:
        print("Good Guess!")
        guessed_letters.append(guess)

        for i in range(len(random_word)):
            if random_word[i] == guess:
                displayed_word[i] = guess

        else:
            print("Wrong Guess!")
            incorrect_letters.append(guess)
            incorrect_guesses += 1

            if "_" not in displayed_word:
                print("\nYou Win! The word was:", words)
                return "win"
               
                 
            else:
                print("\Game Over! The word was:", words)
                return "loss"

if __name__ == "__main__":
    play()    
                
   
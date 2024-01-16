import random
# Hangman
# 1. choose a word
#     beginning of loop
# 2. ask for a guess, g 
# 3. generate for a clue
# 4. check to see if the clue = the word
#     a. if it does, you win
#     b. else you continue
# 4. add that guess to a list of guessed letters
# 5. go back to 2
#     end of loop


# choose a word
with open("words.txt", "r") as wordfile:
    words = [word.strip() for word in wordfile.readlines() if len(word.strip())]

def play_hangman():
    '''simulates a game of hangman'''
    play_again = True
    while play_again:
        play_response = input("Do you want to play hangman (y or n)?: ")
        if play_response != "y":
            break
        hangman_word = random.choice(words)
        guesses_left = 6
        guessed_letters = ""
        errors = 0
        while guesses_left > 0:
            clue = ""
            for letter in hangman_word:
                if letter in guessed_letters:
                    clue += letter
                else:
                    clue += "-"
            print("Clue:", clue)
            print("Letters guessed:", guessed_letters)
            guess = input("Your guess: ")
            if guess in guessed_letters:
                continue
            if guess not in hangman_word:
                errors += 1
                print(errors, "error(s)")
            guessed_letters += guess
            guesses_left -= 1
            if guesses_left == 0:
                print("You lose! The word was", hangman_word)
                break
            if "-" not in clue:
                print("You win!")
                break
        repeat_response = input(("Do you want to play again? (y or n): "))
        if repeat_response != "y":
            play_again = False
    print("Goodbye")

play_hangman()




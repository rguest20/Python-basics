i = 1
while i <= 4:
    print("This is loop number " + str(i))
    i += 1

print("Loop Complete - Preparing Guessing Game")

secret_word = "hamburger"
guess = ""
guess_number = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_number < guess_limit:
        guess = input("Guess the secret word: ")
        guess_number += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose! A loser is you!")
else:
    print("You is winner!! A winner is you!")

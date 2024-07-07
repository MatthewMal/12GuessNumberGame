import random

UPPER_LIMIT = 100
LOWER_LIMIT = 0
guess = LOWER_LIMIT - 1

print("Welcome to the Number Guessing game!")

difficulty = input("Choose difficulty level: type 'easy' or 'hard': ")

while difficulty not in ['easy', 'hard']:
    difficulty = input("There was an error! Please type either 'easy' or 'hard': ")

print("I'm thinking of a number between 1-100")
guess_target = random.randint(LOWER_LIMIT, UPPER_LIMIT)
guess_counter = 0


if difficulty == 'easy':
    guess_limit = 10
elif difficulty == 'hard':
    guess_limit = 5

while guess_counter < guess_limit and guess != guess_target:
    print(f"You have {guess_limit - guess_counter} guesses left")

    guess = int(input("Make a guess: "))

    if guess > UPPER_LIMIT or guess < LOWER_LIMIT:
        print("Guess out of range\n")
    elif guess > guess_target:
        print("Too high!\n")
    elif guess < guess_target:
        print("Too low!\n")

    guess_counter += 1

if guess == guess_target:
    print("Congratulations, you guessed it!")
else:
    print("Sorry, you ran out of guesses. The correct number was", guess_target)

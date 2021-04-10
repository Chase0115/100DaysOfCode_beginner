import random

easy_attempt = 10
hard_attempt = 5


def mode(difficulty):
    while difficulty != 0:
        print(f"You have {difficulty} attempts remaining to guess the number ")
        user_guess = int(input("Make a guess: "))
        if user_guess == answer:
            print(f"You got it! The answer was {answer}")
            difficulty = 1
        elif user_guess > answer:
            print("Too high")
            print("Guess again")
        elif user_guess < answer:
            print("Too low")
            print("Guess again")

        difficulty -= 1


answer = random.randrange(100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {answer}")
mode_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode_choice == 'easy':
    mode(easy_attempt)

elif mode_choice == 'hard':
    mode(hard_attempt)

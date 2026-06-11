import random

secret_number = random.randint(1, 100)

attempts = 5

print("===== Number Guessing Game =====")
print("Guess a number between 1 and 100")
print("You have 5 attempts.")

while attempts > 0:
    guess = int(input("\nEnter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Too low!")

    attempts -= 1

    if attempts > 0:
        print("Remaining attempts:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The correct number was:", secret_number)
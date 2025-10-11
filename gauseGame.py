import random

print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 20.")

# Step 1: Generate random secret number
secret_number = random.randint(1, 20)

# Step 2: Player gets 6 guesses
for guess_count in range(6):
    print(f"\nAttempt {guess_count + 1} of 6")
    guess = int(input("Take a guess: "))

    # Step 3: Compare guess to secret number
    if guess < secret_number:
        print("Your guess is too low!")
    elif guess > secret_number:
        print("Your guess is too high!")
    else:
        # Step 4: Correct guess
        print(f"Congratulations! You guessed it right. The number was {secret_number}.")
        break
else:
    # Step 6: Player used all guesses
    print(f"Sorry, you've used all 6 guesses. The number was {secret_number}. Better luck next time!")

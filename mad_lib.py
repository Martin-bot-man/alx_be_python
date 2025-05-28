import random
print("Welcome to the Number guessing game")
print("****" *10)

print("Im thinking of a number between 1 and 10")

secret_number = random.randint(1, 10);
guess_taken = 0


while guess_taken < 3:
    guess = int(input("Take a guess: "))
    guess_taken += 1

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        break  # This condition is the correct guess
if guess == secret_number:
    print(f"Good job! You guessed my number in {guess_taken} tries!")
else:
    print(f"Nope. The number I was thinking of was {secret_number}.")
print("Thanks for playing!")
# End of the game



          


    






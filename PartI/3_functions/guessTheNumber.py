import random
 
 
def guess_number(secretNumber):
    for guessesTaken in range(1, 7):
        print("Take a guess.")
        guess = int(input())

        if guess < secretNumber:
            print("Your guess is to low.")
        elif guess > secretNumber:
            print("Your guess is to high.")
        else: break

    if guess == secretNumber:
        print(f"Good Job! you guessed the number in {guessesTaken} guesses")
    else:
        print(f"Nope the number i was thinking of was {secretNumber}")


secretNumber = random.randint(1, 100)
print("I am thinking of a number between 1 and 100")

guess_number(secretNumber)
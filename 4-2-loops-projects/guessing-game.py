from random import randint, random

random_number = randint(1,10)

guess = None
while guess!=random_number:
    guess = input("Guess a number between 1 and 10: ")
    if guess:
        guess = int(guess)
        if guess>=1 and guess<=10:
            if guess == random_number:
                print("You guessed it! You won!")
                cont = input("Do you want to play again? (y/n) ")
                if cont == "y":
                    random_number = randint(1,10)
                    guess = None
                else:
                    print("Thank you for playing!")
                    break
            elif guess>random_number:
                print("Too high, try again!")
            else:
                print("Too low, try again!")
        else:
            print("You need to type in a number between 1 and 10")
    else:
        print("You need to enter a number")
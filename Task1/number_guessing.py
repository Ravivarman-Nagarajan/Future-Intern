import random

def number_guessing():
    number_to_guess = random.randint(1,100)
    guess  = None


    print ("Welcome to Number Guessing game!!" )
    print ("I am thinking of a number between 1 and 100")

    while guess != number_to_guess:

        try:
            guess = int(input("Enter your guess : "))


            if guess < number_to_guess :
                print("Your Guess is too low!")

            elif guess > number_to_guess :
                print("Your Guess is too high!")

            else :
                print("You guessed it right!!")
        except:
            print("Invalid Input!!")


number_guessing()
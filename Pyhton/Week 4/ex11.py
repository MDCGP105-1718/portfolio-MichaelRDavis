from random import randint
random_number = randint(1, 100)
guess = 0

while(random_number != guess):
    guess = int(input("Insert a number between 1 and 100:\n"))
    print("Sorry guess again human:\n")
    if(guess == random_number):
        print("Well done human you found my number:\n")

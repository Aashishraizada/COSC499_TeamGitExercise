import math
import random

x = random.randint(0 , 100)
n = 0
guess = True

print("Guess a number ")

while guess:
    y = int(input("Your guess: "))

    if x == y:
        print("Congratulation you did it in: ")
        guess = False
        break
    elif x > y:
        print("You guessed too small")
        n = n + 1

    elif x < y:
        print("You guessed too big")
        n = n + 1

print("You did it in" + str(n) + "tries")

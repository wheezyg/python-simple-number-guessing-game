print ("WELCOME TO FACEBOOK")

import random
import time

email = input("Email address or phone number:")
password = input("Password:")

#VARIABLES
computer = random.randint(1,20)
turns = 6
goes = 0

print ("Welcome back", email)

user = int(input("Guess what number the computer is thinking of between 1 and 20\n"))

while user:
    if user != computer and user > computer:
        print ("incorrect, number is lower")
        turns -= 1
        goes += 1
        print ("you have", turns, "goes left")
        user = int(input("guess again\n"))

    if user != computer and user < computer:
        print ("incorrect, number is higher")
        turns -= 1
        goes += 1
        print ("you have", turns, "goes left")
        user = int(input("guess again\n"))
    if user == computer:
        goes += 1
        print ("CORRECT\nyou got it in", turns, "goes")
        break
    if turns == 1:
        print ("incorrect")
        print("out of goes")
        print ("GAME OVER")
        break










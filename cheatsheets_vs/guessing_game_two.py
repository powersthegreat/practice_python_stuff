#computer guesses a number between 1 and 100
#you are holding in your head

import random

counter = 0
minimum = 0
maximum = 100
user_response = ""

while user_response != "exit":

    computer_guess = random.randint(minimum,maximum)
    print("My guess is " + str(computer_guess))
    user_response = input("Enter too 'low', too 'high', or 'correct'\n")

    if user_response == "high":
        maximum = int(computer_guess)
        computer_guess = random.randint(minimum,maximum - 1)

    elif user_response == "low":
        minimum = int(computer_guess)
        computer_guess = random.randint(minimum + 1,maximum)
    elif user_response == "correct":
        print("I got it in " + str(counter) + " trys!")
        break

    counter += 1
input()


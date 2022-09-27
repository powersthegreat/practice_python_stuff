#cows and bulls game
import random

def cows_bulls(user_guess, random_four):
    cows = 0
    bulls = 0

    for i in range(0, 4):
        if user_guess[i] == random_four[i]:
            cows += 1
        else:
            bulls += 1
    statement = f"Cows: {cows} \nBulls: {bulls}"
    if user_guess == random_four:
        return print("Congrats you won!")
    else:
        return print(statement)

user_input = input("Would you like to play cows and bulls? Enter 'yes' or 'no'.\n")
random_four_list = []
for i in range(0, 4):
    random_four_list.append(str(random.randint(0,9)))
random_four_num = "".join(random_four_list)


while user_input == 'yes':
    guess = input("Enter a four digit guess:\n")
    answer = cows_bulls(guess, random_four_num)
    if answer == "Congrats you won!":
        break
    print(random_four_num + '\n' + '\n')
    user_input = input("Would you like to guess again? Enter 'yes' or 'no'.\n")
    
    


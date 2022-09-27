#infinite monkey theorm
import random as random

alphabet_string = 'abcdefghijklmnopqrstuvwxyz '
alphabet_list = []
for i in range(0, 27):
    alphabet_list.append(alphabet_string[i])

def random_34_string(letter_list):
    random_string_list = []
    for i in range(0, 16):
        index = random.randint(0,26)
        random_string_list.append(letter_list[index])
    random_string = "".join(random_string_list)
    return random_string

goal_string = "computer science"
test = random_34_string(alphabet_list)
# print(test)
# print(len(test))
# print(goal_string)
# print(len(goal_string))
count = 0

while test != goal_string:
    count += 1
    test = random_34_string(alphabet_list)
    print(count)
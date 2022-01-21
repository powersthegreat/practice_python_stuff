import random

def max_of_three(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_3 and num_2 > num_1:
        return num_2
    elif num_3 > num_1 and num_3 > num_2:
        return num_3
    else:
        return num_1, num_2, num_3

random_num_1 = random.randint(0,200)
random_num_2 = random.randint(0,200)
random_num_3 = random.randint(0,200)
print(random_num_1, random_num_2, random_num_3)
print("\n")
print(max_of_three(random_num_1, random_num_2, random_num_3))
print("\n")
import random as random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def password_generator(strength):
    stripped = strength.strip()
    lowered = strength.lower()
    numbers = []
    lower_letters = []
    upper_letters = []
    for i in range(0, 8):
        numbers.append(random.randint(0,9))
    for i in range(0,2):
        rd_int_1 = random.randint(0,25)
        lower_letters.append(alphabet[int(rd_int_1)])
    for i in range(0,2):
        rd_int_2 = random.randint(0,25)
        upper_letters.append(alphabet[int(rd_int_2)])
    if lowered == "easy":
        password_1 = numbers
        return password_1
    elif lowered == "medium":
        password_2 = numbers + lower_letters
        return password_2
    elif lowered == "strong":
        cap_upper_letters = []
        for letter in upper_letters:
            new = letter.capitalize()
            cap_upper_letters.append(new)
        password_3 = numbers + lower_letters + cap_upper_letters
        return password_3

user_input = input("How strong do you want your password to be? Enter weak, medium, or strong:\n")

random_password = password_generator(user_input)
cleaned_password = ""
for i in random_password:
    cleaned_password = cleaned_password + str(i)

print(cleaned_password)

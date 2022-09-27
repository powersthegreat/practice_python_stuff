## 1. Functions are objects
def add_five(num):
    print(num+5)

add_five(2)
print(add_five)

# # 2. Functions within functions
def add_five(num):
    def add_two(num):
        return num+2
    num_plus_two = add_two(num)
    print(num_plus_two + 3)

add_five(10)
add_two(4)

# # 3. Returning functions from functions
def get_math_function(operation):
    def add(num1, num2):
        return num1 + num2
    def sub(num1, num2):
        return num1 - num2
    if operation == '+':
        return add
    elif operation == '-':
        return sub

add_function = get_math_function('+')
sub_function = get_math_function('-')

print(add_function(4,6))
print(sub_function(6,4))

# # 4. Decorating a function
def title_decorator(print_name_function):
    def wrapper():
        print("Professor")
        print_name_function()
    return wrapper

def print_my_name():
    print('Will')

def print_matts_name():
    print("Matt")

decorated1_function = title_decorator(print_my_name)
decorated2_function = title_decorator(print_matts_name)
decorated1_function()
decorated2_function()

# # 5. Decorators
def title_decorator(print_name_function):
    def wrapper():
        print("Professor")
        print_name_function()
    return wrapper

@title_decorator
def print_my_name():
    print('Will')

@title_decorator
def print_matts_name():
    print("Matt")

print_my_name()
print_matts_name()

# 6. Decorators w/ Parameters
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor")
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_my_name(name, age):
    print(f"{name} is {age}")


print_my_name("Will", 40)

# decorator @ thing goes right above function
# you want to use it one

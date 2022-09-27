a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

def compare(list_1, list_2):
    yn_list = []
    for nums in list_1:
        square = nums**2
        if square in list_2:
            yn_list.append(1)
        else:
            yn_list.append(0)
    # print(yn_list)
    # print(sum(yn_list))
    # print(len(yn_list))
    if sum(yn_list) == len(yn_list):
        return True
    else:
        return False

output = compare(a, b)
print(output)
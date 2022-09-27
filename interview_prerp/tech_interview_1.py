#given a list and a number, rotated that list forward as many times as the number implies
#assuming the list will wrap and it is all positive numbers

# print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e']))

#'a', 'b', 'c', 'd', 'e', 'f' => 3
#'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f'

def rotate_forward(given_list, rotations):
    expanded_list = []
    full_list = []

    for i in range(0, rotations):
        expanded_list.append(given_list)

    for i in range(0, len(expanded_list)):
        for t in range(len(expanded_list[0])):
            full_list.append(expanded_list[i][t])

    start = (rotations * -1) - len(given_list)
    end = (rotations * -1)
    rotated_list = full_list[start:end]

    return rotated_list

def rotate_backward(given_list, rotations):
    expanded_list = []
    full_list = []

    for i in range(0, rotations):
        expanded_list.append(given_list)

    for i in range(0, len(expanded_list)):
        for t in range(len(expanded_list[0])):
            full_list.append(expanded_list[i][t])
    
    start = rotations
    end = rotations + len(given_list)
    rotated_list = full_list[start:end]

    return rotated_list


my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#, 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = 2
print(my_list)
print(rotate_forward(my_list, num))
print(rotate_backward(my_list, num))


            

        
    
        
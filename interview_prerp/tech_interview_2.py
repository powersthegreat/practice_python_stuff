def rotation_point(given_list):
    alphabet_dict = alph_dict()
    new_list = []
    for i in given_list:
        new_list.append(alphabet_dict[i])
    minimum = 27
    for nums in new_list:
        if nums < minimum:
            minimum = nums
    index = new_list.index(minimum)
    return print(f"List: {given_list}\nInitial Index: {index}\n")


def alph_dict():
    alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    int_alphabet = []
    for i in range(0, len(alph_list)):
        int_alphabet.append(i)
    alphabet_dict = dict(zip(alph_list, int_alphabet))
    return alphabet_dict

my_list = ['o', 'p', 'q', 'r', 's', 't', 'u', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i', 'j', 'k', 'l']
rotation_point(my_list)
input_1 = [0,1,0,1,1,1,1,0,0,1]
input_2 = [9,3,2,7,2,5,3,8]

k_1 = 3
k_2 = 4
k_9 = 9

def kth_smallest_element(my_list, k):
    ordered_list = []
    for i in range(0, len(my_list)):
        min_num = min(my_list)
        ordered_list.append(min_num)
        my_list.remove(min_num)

    for nums in ordered_list:
        index = ordered_list.count(nums)
        if index > 1:
            for j in range(0, index-1):
                ordered_list.remove(nums)
    try:
        kth_smallest = ordered_list[k]
        return kth_smallest
    except IndexError:
        return "NULL"

        
print(kth_smallest_element(input_1, 9))
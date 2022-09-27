import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
one_nine_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7,
                 "eight":8, "nine":9}
for line in sys.stdin:
    line_list = []
    ans_list = []
    for i in line:
        line_list.append(i)
        
    for key in one_nine_dict.keys():
        tf_list = []
        for i in range(0, len(key)):
            if key[i] in line_list:
                tf_list.append(1)
                #line_list.remove(key[i])
            else:
                tf_list.append(0)
        if sum(tf_list) == len(tf_list):
            ans_list.append(key)
            
         
    ans_list_2 = []
    print(ans_list)
    for num in ans_list:
        value = one_nine_dict[num]
        value = str(value)
        ans_list_2.append(value)

    answer = int("".join(ans_list_2))
    print(answer)
#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for i in my_list:
        for j in range(len(my_list) - 1):
            if max < my_list[j + 1]:
                max = my_list[j + 1]
               
    return max



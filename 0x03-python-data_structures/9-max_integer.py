#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        maxx = my_list[0]
        for i in my_list:
            for j in range(len(my_list) - 1):
                if maxx < my_list[j + 1]:
                    maxx = my_list[j + 1]
        return maxx

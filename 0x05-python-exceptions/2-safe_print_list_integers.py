#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list[:x]:
        try:
            count += 1
            print("{:d}".format(i), end="")
        except (TypeError, ValueError):
            count -= 1
            pass
    print()
    return count

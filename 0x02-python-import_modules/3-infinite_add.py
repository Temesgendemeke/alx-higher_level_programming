#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    length = len(sys.argv)
    for i in sys.argv:
        if length == 1:
            pass
        elif i != sys.argv[0]:
            sum += int(i)
    print(sum)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    j = 1
    if n == 0:
        print("0 arguments.")
    else:
        print("{:d} argument:".format(n))
    for i in sys.argv:

        if i == sys.argv[0]:
            continue
        else:
            print("{:d}: {:s}".format(j, i))
            j += 1

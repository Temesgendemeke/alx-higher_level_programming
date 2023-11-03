#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n > 1:
        print("{:d} arguments:".format(n))
        j = 1
        for i in sys.argv:
            if i == sys.argv[0]:
                continue
            print("{:d}: {:s}".format(j, i))
            j += 1
    else:
        print("0 arguments.")

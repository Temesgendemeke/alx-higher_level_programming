#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    for i in range(len(args) - 1):
        try:
            return fct(args[i], args[i + 1])
        except (ValueError, ZeroDivisionError) as zero:
            print("Exception: {}".format(zero), file=sys.stderr)
            return None
            
        except IndexError as idx:
            print("Exception: {}".format(idx), file=sys.stderr)
            return None
   
           

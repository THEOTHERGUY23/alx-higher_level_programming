#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for q in range(x):
        try:
            print(my_list[q], end="")
            num += 1
        except IndexError:
            break
        print("")
        Return

#!/usr/bin/python3
if __name__ != "__main__":
    exit()
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = my_list
    if idx >= 0 and idx < len(newList):
        newList[idx] = element
    return newList

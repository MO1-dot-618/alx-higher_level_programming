#!/usr/bin/python3
def uniq_add(my_list=[]):
    aniq = set(my_list)
    result = 0
    for i in aniq:
        result += i
    return result

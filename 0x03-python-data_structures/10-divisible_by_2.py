#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    div = []
    for i in my_list:
        div.append(True if i % 2 == 0 else False)
    return div

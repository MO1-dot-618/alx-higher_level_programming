#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return None
    elif idx == 0:
        return my_list[1:]
    elif idx == len(my_list) - 1:
        return my_list[:idx]
    else:
        return my_list[:idx] + my_list[idx - 1:]

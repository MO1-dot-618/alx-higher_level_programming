#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = []
    for i in range(list_length):
        try:
            c.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ValueError):
            c.append(0)
            print("wrong type")
        except ZeroDivisionError:
            c.append(0)
            print("division by 0")
        except IndexError:
            c.append(0)
            print("out of range")
        finally:
            continue
    return c

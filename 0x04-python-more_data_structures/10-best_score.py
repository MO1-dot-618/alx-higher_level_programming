#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    store = None
    b_student = None
    for student, val in a_dictionary.items():
        if store is None or val > store:
            store = val
            b_student = student
    return b_student

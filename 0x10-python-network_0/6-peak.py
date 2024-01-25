#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    lt = list_of_integers
    lft, rt = 0, len(list_of_integers) - 1

    while lft <= rt:
        m = (lft + rt) // 2
        if m > 0 and lt[m] < lt[m - 1]:
            rt = m - 1
        elif m < len(lt) - 1 and lt[m + 1] > lt[m]:
            lft = m + 1

        else:
            return lt[m]

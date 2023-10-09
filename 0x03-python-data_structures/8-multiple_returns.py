#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = (sentence[:1] if length != 0 else None)
    return (length, first)

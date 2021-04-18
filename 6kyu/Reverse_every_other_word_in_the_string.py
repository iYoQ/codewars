#!/usr/bin/env python3

def reverse_alternate(string):
    string = string.split()
    for ind, i in enumerate(string):
        if ind % 2:
            string[ind] = i[::-1]
    return " ".join(string)
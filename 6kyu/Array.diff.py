#!/usr/bin/env python3

def array_diff(a, b):
    for i in range(len(a)-1,-1,-1):
        if a[i] in b:
            a.pop(i)
    return a
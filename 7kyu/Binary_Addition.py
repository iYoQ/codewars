#!/usr/bin/env python3

def add_binary(a,b):
    n = a + b
    t = ''
    while n > 0:
        t = str(n % 2) + t
        n //= 2
    return t
#!/usr/bin/env python3

def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 = int(p0 + p0*(percent/100) + aug)
        count += 1
    return count
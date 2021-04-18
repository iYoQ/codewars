#!/usr/bin/env python3

def find_uniq(arr):
    return next(i for i in set(arr) if arr.count(i) == 1)
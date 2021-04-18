#!/usr/bin/env python3


def move_zeros(array):
    new = []
    zero = []
    for i in range(len(array)):
        new.append(array[i]) if array[i] else zero.append(array[i])
    return new + zero
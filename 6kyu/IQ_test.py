#!/usr/bin/env python3

def iq_test(numbers):
    numbers = list(map(int, numbers.split()))
    count_odd = [i for i in numbers if i % 2]
    count_even = [i for i in numbers if not i % 2]
    if len(count_odd) < len(count_even):
        return numbers.index(*count_odd) + 1
    return numbers.index(*count_even) + 1
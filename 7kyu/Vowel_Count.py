#!/usr/bin/env python3

def get_count(input_str):
    list_ = ["a", "e", "i", "o", "u"]
    return sum([1 for i in input_str for j in list_ if i == j])
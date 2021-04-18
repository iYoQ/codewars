#!/usr/bin/env python3

def sort_array(source_array):
    for i in range(len(source_array)):
        for j in range(i, len(source_array)):
            if source_array[i] % 2 and source_array[j] % 2:
                if source_array[j] < source_array[i]:
                    source_array[j], source_array[i] = source_array[i], source_array[j]
    return source_array
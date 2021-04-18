#!/usr/bin/env python3

def number(bus_stops):
    s = 0
    for i in bus_stops:
        s += sum(i) - i[1]*2
    return s 
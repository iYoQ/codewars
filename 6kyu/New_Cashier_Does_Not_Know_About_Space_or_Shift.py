#!/usr/bin/env python3

def get_order(order):
    l = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke", ]
    return ("".join([(i + " ")*order.count(i.lower()) for i in l if i.lower() in order])).strip()
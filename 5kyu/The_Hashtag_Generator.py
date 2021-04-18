#!/usr/bin/env python3

def generate_hashtag(s):
    return False if (len(s) > 140 or not s) else "#" + "".join(i.capitalize() for i in s.split())
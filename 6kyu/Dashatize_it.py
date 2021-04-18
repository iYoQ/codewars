#!/usr/bin/env python3

def dashatize(n):
    if isinstance(n, int):
        n = abs(n)
        n = list(map(int, str(n)))
        if len(n) == 1:
            return str(n[0])
        for index, i in enumerate(n):
            if i % 2:
                if index and index != len(n)-1:
                    n[index] = "-" + str(i) + "-"
                elif not index:
                    n[index] = str(i) + "-"
                elif index == len(n)-1:
                    n[index] = "-" + str(i)
            else:
                n[index] = str(i)
        s = "".join(n)
        s = s.replace("--", "-")
        return s
    return "None"
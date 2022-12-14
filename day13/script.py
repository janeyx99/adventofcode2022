#!/bin/bash python3

import json
import itertools
import functools
from typing import Any, List, Optional, Tuple

lol: List[Tuple[List, List]] = []

def listsInOrder(l1: List[Any], l2: List[Any]) -> int:
    for x, y in itertools.zip_longest(l1, l2):
        if isinstance(x, int) and isinstance(y, int):
            if x > y:
                return -1
            elif x < y:
                return 1
            # continue!
        elif x is None:
            return 1
        elif y is None:
            return -1
        else:
            if not isinstance(x, List):
                x = [x]
            if not isinstance(y, List):
                y = [y]
            r = listsInOrder(x, y)
            if r != 0:
                return r
            # continue!
    return 0
    

with open('input.txt') as f:
    l1 = None
    l2 = None
    fill1 = True
    for line in f.readlines():
        if line.startswith('['):
            if fill1:
                l1 = json.loads(line)
            else:
                l2 = json.loads(line)
            fill1 = not fill1
        else:
            # line is empty, so append another pair
            lol.append((l1, l2))
    lol.append((l1, l2))
    # sum = 0
    # for i, (x, y) in enumerate(lol):
    #     r = listsInOrder(x, y)
    #     if r >= 0:
    #         print(i)
    #         sum += i + 1
    # print(sum)

    flatlol = [[[2]], [[6]]]
    for x in lol:
        flatlol.extend(x)

    flatlol.sort(key=functools.cmp_to_key(listsInOrder), reverse=True)
    for z in flatlol:
        print(z)
    i1 = flatlol.index([[2]]) + 1
    i2 = flatlol.index([[6]]) + 1
    print(i1, i2, i1*i2)


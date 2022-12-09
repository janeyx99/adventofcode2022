#!/bin/bash python3

from typing import Tuple, Set

hx, hy = (0, 0)
txs = [0 for _ in range(9)]
tys = [0 for _ in range(9)]
visited: Set[Tuple[int, int]] = set([(0,0)])

def moveHead(dir: str) -> None:
    global hx, hy
    if dir == 'U':
        hy += 1
    elif dir == 'D':
        hy -= 1
    elif dir == 'L':
        hx -= 1
    elif dir == 'R':
        hx += 1
    else:
        raise RuntimeError(f'{dir} should be one of UDLR but is not.')

def moveTail() -> None:
    global hx, hy, tx, ty
    dx = hx - tx
    adx = abs(dx)
    dy = hy - ty
    ady = abs(dy)
    if adx + ady >= 2 and adx != ady:
        tx += dx / adx if dx != 0 else 0
        ty += (dy) / ady if dy != 0 else 0
        visited.add((tx, ty))

def moveTails() -> None:
    global hx, hy, txs, tys
    for i in range(len(txs)):
        tx = txs[i]
        ty = tys[i]
        if i == 0:
            x = hx
            y = hy
        else:
            x = txs[i - 1]
            y = tys[i - 1]
        dx = x - tx
        adx = abs(dx)
        dy = y - ty
        ady = abs(dy)
        if adx + ady >= 2 and (adx != 1 or ady != 1):
            txs[i] += dx / adx if dx != 0 else 0
            tys[i] += dy / ady if dy != 0 else 0
    visited.add((txs[-1], tys[-1]))

with open('input.txt') as f:
    for line in f.readlines():
        dir, steps = line.strip().split()
        for _ in range(int(steps)):
            moveHead(dir)
            moveTails()

print(len(visited))
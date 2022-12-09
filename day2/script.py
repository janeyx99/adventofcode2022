#!/bin/bash python3

rock = 1       # A, X
paper = 2      # B, Y
scissors = 3   # C, Z

lose = 0
tie = 3
win = 6

move_points = {
    'X': 1,
    'A': 1,
    'Y': 2,
    'B': 2,
    'Z': 3,
    'C': 3,
}

win_cond_points = {
    'X': 0,
    'Y': 3,
    'Z': 6
}



def old_get_points_per_round(op_move: str, your_move: str) -> int:
    total = move_points[your_move]
    if (your_move == 'X' and op_move == 'A' or
        your_move == 'Y' and op_move == 'B' or
        your_move == 'Z' and op_move == 'C'):
        return total + 3
    if (your_move == 'X' and op_move == 'B' or
        your_move == 'Y' and op_move == 'C' or
        your_move == 'Z' and op_move == 'A'):
        return total
    return total + 6


def get_points_per_round(op_move: str, win_cond: str) -> int:
    total = win_cond_points[win_cond]
    if win_cond == 'Y':
        return total + move_points[op_move]
    if win_cond == 'X':
        if op_move == 'A':
            return total + 3
        if op_move == 'B':
            return total + 1
        return total + 2
    if op_move == 'A':
        return total + 2
    if op_move == 'B':
        return total + 3
    return total + 1

with open('input.txt') as f:
    total = 0
    for line in f.readlines():
        print(get_points_per_round(*line.split()))
        total += get_points_per_round(*line.split())
        print(total)

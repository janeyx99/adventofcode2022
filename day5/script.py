#!/bin/bash python3

# bottom is left
STRING_STACKS = [
  'DTRBJLWG',
  'SWC',
  'RZTM',
  'DTCHSPV',
  'GPTLDZ',
  'FBRZJQCD',
  'SBDJMFTR',
  'LHRBTVM',
  'QPDSV'
]

STACKS = [[*s] for s in STRING_STACKS]

def move(how_many: int, source: int, dest: int) -> None:
  d = STACKS[dest - 1]
  s = STACKS[source - 1]
  i = len(s) - how_many
  r = s[i:]
  # r.reverse()
  STACKS[source - 1] = s[:i]
  d.extend(r)

with open('input.txt') as f:
  for line in f.readlines():
    if line.startswith("move"):
      how_many, source, dest = [int(s) for s in line.strip().split() if s.isnumeric()]
      move(how_many, source, dest)


print("".join([s.pop() for s in STACKS]))
#!/bin/bash python3

# A-Z is 65-90, a-z is 97-122
def get_priority(c: str) -> int:
  code = ord(c)
  if code > 90:
    return code - 96
  return code - 38

def part1(line): 
  rs1 = set()
  rs2 = set()
  line = line.strip()
  assert len(line) % 2 == 0, f'num items should be even but line is {line}.'
  for i in range(int(len(line) / 2)):
    p1 = get_priority(line[i])
    p2 = get_priority(line[len(line) - 1 - i])
    rs1.add(p1)
    rs2.add(p2)
    if p1 in rs2:
      return p1
    if p2 in rs1:
      return p2

def get_common(e1: set, e2: set, e3: set) -> int:
  common = e1.intersection(e2).intersection(e3)
  assert len(common) == 1, f'{common}'
  return get_priority(common.pop())

with open('input.txt') as f:
  total = 0
  i = 0
  e1 = set()
  e2 = set()
  for line in f.readlines():
    line = line.strip()
    if i == 0:
      e1 = set(line)
    elif i == 1:
      e2 = set(line)
    else:
      total += get_common(e1, e2, set(line))
    i = (i + 1) % 3
    
  print(total)

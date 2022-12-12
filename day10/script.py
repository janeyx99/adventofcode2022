#!/bin/bash python3

from typing import List, Any

x = 1
cycle = 0
W = 40
H = 6
toDraw = ['.' for _ in range(W * H)]

hasDrawn = [False for _ in range(W * H)]

def countCycle(cycle: int) -> bool:
  global x
  return cycle == 20 or (cycle - 20) % W == 0

def handleCommand(command: Any, currSum: int) -> int:
  global x, cycle
  res = currSum
  if command == "noop":
    if cycle % W >= x - 1 and cycle % W <= x + 1:
      toDraw[cycle] = '#'
    cycle += 1
    # hasDrawn[cycle] = toDraw[cycle]
    if countCycle(cycle):
      res = currSum + cycle * x
  else:
    num = int(command.split()[1])
    if cycle % W >= x - 1 and cycle % W <= x + 1:
      toDraw[cycle] = '#'
    if (cycle + 1) % W >= x - 1 and (cycle + 1) % W <= x + 1:
      toDraw[cycle + 1] = '#'
    cycle += 2
    # hasDrawn[cycle - 1] = toDraw[cycle - 1]
    # hasDrawn[cycle] = toDraw[cycle]
    if countCycle(cycle - 1):
      res = currSum + (cycle - 1) * x
    elif countCycle(cycle):
      res = currSum + cycle * x
    x += num
  return res

with open('input.txt') as f:
  sum = 0
  for line in f.readlines():
    sum = handleCommand(line.strip(), sum)

  for i in range(H):
    print(''.join(toDraw[W * i:W * (i+1)]))
    
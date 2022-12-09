#!/bin/bash python3

from typing import List


grid: List[List[int]] = []
is_viewable : List[List[int]] = []

# 0 1 3 4 2 1 5 1 9 0 9 2
def updateRow(row: List[int], i: int) -> None:
  currMax = row[0]
  is_viewable[i][0] = 1
  for j, num in enumerate(row):
    if num > currMax:
      is_viewable[i][j] = 1
      currMax = num

  currMax = row[len(row) - 1]
  is_viewable[i][len(row) - 1] = 1
  for j in reversed(range(len(row))):
    num = row[j]
    if num > currMax:
      is_viewable[i][j] = 1
      currMax = num

def updateCol(grid: List[List[int]], j: int) -> None:
  currMax = grid[0][j]
  is_viewable[0][j] = 1
  for i in range(len(grid)):
    num = grid[i][j]
    if num > currMax:
      is_viewable[i][j] = 1
      currMax = num
  
  currMax = grid[len(grid) - 1][j]
  is_viewable[len(grid) - 1][j] = 1
  for i in reversed(range(len(grid))):
    num = grid[i][j]
    if num > currMax:
      is_viewable[i][j] = 1
      currMax = num

def updateGrid() -> None:
  for i, row in enumerate(grid):
    updateRow(row, i)

  for j in range(len(grid[0])):
    updateCol(grid, j)

with open('input.txt') as f:
  for line in f.readlines():
    grid.append([int(c) for c in line.strip()])
    is_viewable.append([0 for _ in line.strip()])

  max_prod = 0
  for i, row in enumerate(grid):
    for j, num in enumerate(row):
      # go up
      up_view = 0
      for k in reversed(range(0, i)):
        up_view += 1
        if grid[k][j] >= num:
          break
      down_view = 0
      for k in range(i + 1, len(grid)):
        down_view += 1
        if grid[k][j] >= num:
          break
      left_view = 0
      for k in reversed(range(0, j)):
        left_view += 1
        if grid[i][k] >= num:
          break
      right_view = 0
      for k in range(j + 1, len(row)):
        right_view += 1
        if grid[i][k] >= num:
          break
      max_prod = max(max_prod, up_view * down_view * left_view * right_view)
  print(max_prod)
  # updateGrid()
  # print(is_viewable)
  # print(sum(map(sum, is_viewable)))
#!/bin/bash python3

from typing import List
import sys

sys.setrecursionlimit(5000)

class Node:
  def __init__(self, name, dist=1000000000, seen=False):
    self.name: str = name
    self.neighbors: List[Node] = []
    self.dist: int = dist  # just a really large number
    self.seen = seen
  def __str__(self):
    return (f'{self.name} has neighbors {", ".join([n.name for n in self.neighbors])}, '
           f'distance from start = {self.dist}, and has been seen = {self.seen}')

q = []
def getShortestPaths(s: Node) -> None:
  global q
  s.seen = True
  for n in s.neighbors:
    n.dist = min(n.dist, s.dist + 1)
  for n in s.neighbors:
    if not n.seen:
      q.append(n)
      n.seen = True
  if len(q) > 0:
    getShortestPaths(q.pop(0))

grid: List[List[Node]] = []
startNode = None
endNode = None

def createNodeFor(c: str) -> Node:
  global startNode, endNode, q
  if c == 'S':
    startNode = Node('a', dist=0)
    return startNode
  if c == 'E':
    endNode = Node('z')
    return endNode
  if c == 'a':
    n = Node('a', dist=0, seen=True)
    q.append(n)
    return n
  return Node(c)


def isNeighbor(me: Node, neighbor: Node) -> bool:
  return ord(neighbor.name) - ord(me.name) <= 1

with open('input.txt') as f:
  for line in f.readlines():
    grid.append([createNodeFor(c) for c in [*line.strip()]])

  for i, row in enumerate(grid):
    for j, c in enumerate(row):
      # check top
      if i - 1 >= 0 and isNeighbor(c, grid[i - 1][j]):
          c.neighbors.append(grid[i - 1][j])

      # check down
      if i + 1 < len(grid) and isNeighbor(c, grid[i + 1][j]):
          c.neighbors.append(grid[i + 1][j])
        
      # check left
      if j - 1 >= 0 and isNeighbor(c, grid[i][j - 1]):
          c.neighbors.append(grid[i][j - 1])
      
      # check right
      if j + 1 < len(row) and isNeighbor(c, grid[i][j + 1]):
          c.neighbors.append(grid[i][j + 1])

  # run dijkstra's
  getShortestPaths(startNode)

print(startNode)
print(endNode)

#!/bin/bash python3

with open('input.txt') as f:
  total = 0
  for line in f.readlines():
    e1, e2 = line.strip().split(',')
    min1, max1 = e1.split('-')
    min2, max2 = e2.split('-')
    if (int(min2) <= int(max1) and int(max2) >= int(min1)) or (int(min1) <= int(max2) and int(max1) >= int(min2)):
      total += 1
      print(e1, e2, int(min2) <= int(max1), int(min1) <= int(max2))
print(total)

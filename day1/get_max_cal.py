#!/bin/bash python3

with open('input.txt') as f:
  one = 0
  two = 0
  three = 0
  curr = 0
  for line in f.readlines():
    try:
      curr += int(line)
    except ValueError:
      smallest = min(one, two, three)
      if curr > smallest:
        if one is smallest:
          one = curr
        elif two is smallest:
          two = curr
        else:
          three = curr
      curr = 0

print(one + two + three)
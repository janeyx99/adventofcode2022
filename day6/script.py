#!/bin/bash python3

n = 13
with open('input.txt') as f:
  last_n_chars = []
  i = 0
  for c in f.read():
    print(last_n_chars)
    i += 1
    if c in last_n_chars:
      j = last_n_chars.index(c)
      last_n_chars = last_n_chars[j + 1:]
      last_n_chars.append(c)
    elif len(last_n_chars) < n:
      last_n_chars.append(c)
    else:
      break

print(i)

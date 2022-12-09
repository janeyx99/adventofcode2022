#!/bin/bash python3

from typing import Dict, List, Optional, Tuple, Union


class Directory:
  def __init__(self, name, parent=None):
    self.name: str = name
    self.parent: Optional[Directory] = parent
    self.children: Dict[str, Union[File, Directory]] = {}
    self.size: int = 0
  def __str__(self):
    return self.name
  def addFile(self, name: str, size: int) -> None:
    assert name not in self.children, f'{name} should not already exist in {self.name}!'
    self.children[name] = File(name, size, self)
    ancestor = self
    while ancestor is not None:
      ancestor.size += size
      ancestor = ancestor.parent
  def addDir(self, name: str) -> None:
    assert name not in self.children, f'{name} should not already exist in {self.name}!'
    self.children[name] = Directory(name, self)
  def getChildDir(self, name: str):
    assert name in self.children, f'{name} should be a child of {self.name}'
    return self.children[name]


class File:
  def __init__(self, name, size, parent=None):
    self.name: str = name
    self.size: int = size
    self.parent: Optional[Directory] = parent
  def __str__(self):
    return self.name


# Handles command and returns the new current directory and whether we're ls'ing
def handleCommand(c: str, currdir: Directory) -> Tuple[Directory, bool]:
  if c.startswith('cd'):
    _, dirname = c.strip().split()
    if dirname == '..':
      return currdir.parent, False
    return currdir.getChildDir(dirname), False
  if c.startswith('ls'):
    return currdir, True


def getSum(dir: Directory) -> int:
  sum = 0
  if dir.size <= 100000:
    sum = dir.size
  for _, f in dir.children.items():
    if isinstance(f, Directory):
      sum += getSum(f)
  return sum


def getDirSizes(dir: Directory) -> List[int]:
  sizes = [dir.size]
  for _, f in dir.children.items():
    if isinstance(f, Directory):
      sizes.extend(getDirSizes(f))
  return sizes


with open('input.txt') as f:
  rootrootdir: Directory = Directory('root', None)
  rootdir: Directory = Directory('/', rootrootdir)
  rootrootdir.children['/'] = rootdir
  currdir = rootrootdir
  ls = False
  for line in f.readlines():
    if line.startswith('$'):
      currdir, ls = handleCommand(line[2:], currdir)
    else:
      assert ls, 'We should be in LS mode.'
      detail, filename = line.strip().split()
      if detail == 'dir':
        currdir.addDir(filename)
      else:
        currdir.addFile(filename, int(detail))

# print(getSum(rootdir))
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000
SPACE_USED = rootdir.size

s = getDirSizes(rootdir)
s.sort()
for x in s:
  if TOTAL_SPACE - SPACE_USED + x >= SPACE_NEEDED:
    print(x)
    break

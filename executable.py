#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
x = argv
def calc(x):
  result = pow(int(x[1]), 2)
  print(x[1] + "2 = " result)

if __name__ == '__main__':
    calc(x)

#!/usr/bin/env python

from sys import argv

def mytac(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines[::-1]

name = argv[1]
# for reversed_line in mytac(name):
    # print(reversed_line, end='')

print(''.join(mytac(name)))

mytac2 = lambda n : open(n).readlines()[::-1]
print(str.join('',mytac2(name)))

#print(*mytac(name), sep='')

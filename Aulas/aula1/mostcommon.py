#!/usr/bin/env python

from sys import argv

def most_common(text, n):
    ocurrences = dict()
    words = text.split()
    for word in words:
        word = word.strip('.,!?;:').lower()
        ocurrences.setdefault(word, 0)
        ocurrences[word] += 1
    n_most_common = sorted(ocurrences.items(), key=lambda x: x[1], reverse=True)[:n]
    return (n_most_common, sum(ocurrences.values()))

with open(argv[1]) as f:
    n_most_common, total = most_common(f.read(), int(argv[2]))
    for i, (pal, n) in enumerate(n_most_common):
        print(f"{i+1}) {pal} - {n} ocorrências ({n/total:.2f})")

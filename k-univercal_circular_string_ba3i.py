'''

Find a k-Universal Circular String

A k-universal circular string is a circular string that contains every possible k-mer constructed over a given alphabet.

k-Universal Circular String Problem
Find a k-universal circular binary string.

Given: An integer k.

Return: A k-universal circular string. (If multiple answers exist, you may return any one.)

'''

import itertools
import random
import sys

def path(pattern):

    path = pattern[0]
    pattern_len = len(pattern)
    for i in range(1, pattern_len):
        kmer = len(pattern[i])
        
        if pattern[i][0:kmer - 1] == path[i:]:
            path = path + pattern[i][kmer - 1]
    
    return path

def deBruijn(pattern):
    
    graph = {}
    for i in pattern:
        klen = len(i)
        suffix = i[1:]
        prefix = i[0: klen - 1]
        if prefix not in graph:
            graph[prefix] = []
            graph[prefix].append(suffix)
        else:
            graph[prefix].append(suffix)

    return graph

def EulerianCycle(graph):

    cycle = []
    path = []
    i = random.choice(list(graph))
    path.append(i)
    while path:
        if graph[i]:
            neighbor = graph[i].pop()
            i = neighbor
            path.append(i)
        else:
            cycle.append(path.pop())
            if path:
                i = path[-1]
            
    return cycle[::-1]


def FindkUniversalCircularString(k):
    
    binary = [''.join(p) for p in itertools.product(['0', '1'], repeat=k)]
    debr = deBruijn(binary)
    cycle = EulerianCycle(debr)
    circular_string = path(cycle)
    string = circular_string[: len(circular_string) - k + 1]

    return string

if __name__ == "__main__":
    #k = sys.argv[1]
    k = 9
    print(FindkUniversalCircularString(k))
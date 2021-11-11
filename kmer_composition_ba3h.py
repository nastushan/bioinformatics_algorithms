'''

Reconstruct a String from its k-mer Composition

String Reconstruction Problem
Reconstruct a string from its k-mer composition.

Given: An integer k followed by a list of k-mers Patterns.

Return: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

'''


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

def EulerianPath(graph):
    
    cycle = []
    path = []
    degrees = count(graph)
    for n in degrees:
        if (degrees[n][0] - degrees[n][1]) == 1:
            start = n
        elif (degrees[n][1] - degrees[n][0]) == 1:
            end = n
    if end not in graph.keys():
        graph[end] = [start]
    else:
        graph[end].append(start)
    #i = random.choice(list(graph))
    path.append(start)
    i = start
    while path:
        if n not in graph.keys():
            graph[n] = []
        if graph[i]:
            neighbor = graph[i].pop()
            i = neighbor
            path.append(i)
        else:
            cycle.append(path.pop())
            if path:
                i = path[-1]
    cycle = cycle[::-1]
    cycle.pop()
            
    return cycle


def count(graph):
    
    degrees = {}
    for i in graph:
        degrees[i] = []
        degrees[i].append(len(graph[i]))
        degrees[i].append(0)
    for i in graph:
        for j in graph[i]:
            if j not in degrees.keys():
                degrees[j] = [0, 1]
            else:
                degrees[j][1] += 1

    return degrees


def StringReconstruction(k, pattern):
    
    debr = deBruijn(pattern)
    eulerian = EulerianPath(debr)
    genome = path(eulerian)
    #g = genome[: len(genome) - k + 1]
    
    return genome

if __name__ == "__main__":
    #filename = sys.argv[1]
    filename = 'rosalind_ba3h_.txt'
    with open(filename) as file:
        Text = file.read().splitlines()
        k = 25

print(StringReconstruction(k, Text))
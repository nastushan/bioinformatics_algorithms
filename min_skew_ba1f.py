''' 

Find a Position in a Genome Minimizing the Skew 

Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC")) are:

0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

Minimum Skew Problem
Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).

'''

import sys

def skews(string):
    x = 0
    skew = []
    i = 1
    ind = {}
    voc = ['C', 'G']
    for item in string:
        if item == voc[0]:
            x -= 1
        if item == voc[1]:
            x += 1
        skew.append(x)
        #ind[x] = [i if x not in ind else ind[x].append(i)]
        if x in ind:
            ind[x].append(i)
        if x not in ind:
            ind[x] = [i]
        i += 1
    min_skew = min(skew)
    ind_min = ind[min_skew]
    return ind_min

if __name__ == "__main__":
    
    filename = sys.argv[1]
        
    with open(filename) as file:
        line = file.read().splitlines()
        string = line[0]

    print(skews(string))
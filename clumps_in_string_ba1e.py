'''

Find Patterns Forming Clumps in a String

Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times. For example, TGCA forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.

Clump Finding Problem
Find patterns forming clumps in a string.

Given: A string Genome, and integers k, L, and t.

Return: All distinct k-mers forming (L, t)-clumps in Genome.

'''


import sys
import re

def clumps(string, L, k, t):
    p = []
    for i in range(len(string)-L + 1):
        s = {}
        x  = string[i:i+L]
        for j in range(len(string)- k + 1):
            substr = x[j:j+k]
            if substr in s:
                s[substr] += 1
            elif substr not in s:
                s[substr] = 1
            
        p += [k for k, l in s.items() if t  == l]
    
    return set(p)

if __name__ == "__main__":
    
    filename = sys.argv[1]
        
    with open(filename) as file:
        line = file.read().splitlines()
        string = line[0]
        num = [int(s) for s in line[1].split() if s.isdigit()]
        k = num[0]
        L = num[1]
        t = num[2]

    print(clumps(string, L, k, t))
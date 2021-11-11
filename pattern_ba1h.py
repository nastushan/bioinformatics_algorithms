'''

Find All Approximate Occurrences of a Pattern in a String

We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.

Approximate Pattern Matching Problem
Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

'''


import sys

def hamming(str1, str2):
    return sum(x != y for x, y in zip(str1, str2))

def match(substr, string, d):
    p = []
    for i in range(len(string) - len(substr) + 1):
        
        if hamming(substr, string[i:i+len(substr)]) <= int(d):
            p.append(i)
    
    return p

if __name__ == "__main__":
    #print(match(input().strip(), input().strip(), int(input().strip())))
    filename = sys.argv[1]
        
    with open(filename) as file:
        line = file.read().splitlines()
        substr = line[0]
        string = line[1]
        d = line[2]
            

    p = match(substr, string, d)
    print(' '.join(map(str,p)))
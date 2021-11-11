'''

Implement DistanceBetweenPatternAndStrings


    DistanceBetweenPatternAndStrings(Pattern, Dna)
        k ← |Pattern|
        distance ← 0
        for each string Text in Dna
            HammingDistance ← ∞
            for each k-mer Pattern’ in Text
                if HammingDistance > HammingDistance(Pattern, Pattern’)
                    HammingDistance ← HammingDistance(Pattern, Pattern’)
            distance ← distance + HammingDistance
        return distance
    
Compute DistanceBetweenPatternAndStrings
Find the distance between a pattern and a set of strings.

Given: A DNA string Pattern and a collection of DNA strings Dna.

Return: DistanceBetweenPatternAndStrings(Pattern, Dna).

'''


import sys

def hamming(str1, str2):
    return sum(x != y for x, y in zip(str1, str2))

def PatternStringDistance(pattern, DNA):
    k = len(pattern)
    distance = 0
    for i in DNA:
        hammingdistance = float('inf')
        for kmer in range(len(i) - k + 1):
            if hammingdistance > hamming(pattern, i[kmer:kmer+k]):
                hammingdistance = hamming(pattern, i[kmer:kmer+k])
        distance += hammingdistance
    return distance


if __name__ == "__main__":
    
    filename = sys.argv[1]

    with open(filename) as file:
        DNA = [line.rstrip() for line in file]
        DNA.pop(0)
        
    pattern = 'CCTTCG'

            
    print(PatternStringDistance(pattern, DNA))
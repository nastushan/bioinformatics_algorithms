'''

Implement Greedy Motif Search

        GREEDYMOTIFSEARCH(Dna, k, t)
        BestMotifs ← motif matrix formed by first k-mers in each string
                      from Dna
        for each k-mer Motif in the first string from Dna
            Motif1 ← Motif
            for i = 2 to t
                form Profile from motifs Motif1, …, Motifi - 1
                Motifi ← Profile-most probable k-mer in the i-th string
                          in Dna
            Motifs ← (Motif1, …, Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
        
Implement GreedyMotifSearch
Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

'''


import sys

def count(motifs):
    L = "ATGC"
    count = {}
    k = len(motifs[0])
    for n in L:
        count[n] = []
        for j in range(k):
            count[n].append(0)

    t = len(motifs)
    for i in range(t):
        for j in range(k):
            n = motifs[i][j]
            count[n][j] += 1

    return count

def profile(motifs):
    L = "ATGC"
    t = len(motifs)
    k = len(motifs[0])
    profile = {}

    profile = count(motifs)
    
    for n in L:
        for j in range(k):
            profile[n][j] /= t

    return profile

def mostprob(motifs):
    L = "ATGC"
    k = len(motifs[0])
    count_ = count(motifs)

    mostprob = ""
    for j in range(k):
        m = 0
        freq = ""
        for n in L:
            if count_[n][j] > m:
                m = count_[n][j]
                freq = n
        mostprob += freq
    
    return mostprob

def score(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score_ = 0
    
    for i in range(t):
        for j in range(k):
             if motifs[i][j] != mostprob(motifs)[j]:
                 score_ += 1

    return score_

def profile_score(string, profile):
    p = 1
    for i in range(len(string)):
        seq = string[i]
        p *= profile[seq][i]
    return p

def profile_most_prob_kmer(string, k, profile):
    prob = 0
    mostprob = string[0:k]
    for i in range(len(string) - k + 1):
        kmer = string[i:k + i]
        if profile_score(kmer, profile) > prob:
            prob = profile_score(kmer, profile)
            mostprob = kmer
    return mostprob


def GreedyMotifSearch(DNA, k, t):
    bestmotifs = []
    for i in range(0, t):
        bestmotifs.append(DNA[i][0:k])
    for i in range(len(DNA[0])- k + 1):
        motifs = []
        motifs.append(DNA[0][i:i + k])
        for j in range(1, t):
            p = profile(motifs[0:j])
            motifs.append(profile_most_prob_kmer(DNA[j], k, p))
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs

if __name__ == "__main__":
    filename = sys.argv[1]
    #filename = 'rosalind_ba2d_.txt'
    with open(filename) as file:
        #line = file.read().splitlines()
        #DNA = line[1]
        DNA = [line.rstrip() for line in file]
        DNA.pop(0)
        #num = [int(s) for s in line[0].split() if s.isdigit()]
        #k = num[0]
        #t = num[1]

    k = 12
    t = 25
    #DNA = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    print(GreedyMotifSearch(DNA, k, t))
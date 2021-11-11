'''

Find a Highest-Scoring Local Alignment of Two Strings

Local Alignment Problem
Find the highest-scoring local alignment between two strings.

Given: Two amino acid strings.

Return: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty σ = 5. (If multiple local alignments achieving the maximum score exist, you may return any one.)

'''


import numpy as np

def local_alignment(str1, str2, pam, matrix):

    m = np.zeros((len(str2) + 1, len(str1) + 1))
    for i in range(len(str1)):
        m[0][i+1] = m[0][i] - 5
    for i in range(len(str2)):
        m[i+1][0] = m[i][0] - 5
    for i in range(len(str2)):
        for j in range(len(str1)):
            m[i+1][j+1] = max(0, m[i][j+1] - 5, m[i+1][j] - 5,
                                      m[i][j] + pam[matrix.index(str2[i])][matrix.index(str1[j])])
    score = 0
    for k in range(len(str2) + 1):
        for t in range(len(str1) + 1):
            if score < m[k][t]:
                score = m[k][t]
                i = k - 1
                j = t - 1
    x = []
    y = []

    while i != -1 or j != -1:
        max_ = m[i+1][j+1] - pam[matrix.index(str2[i])][matrix.index(str1[j])]
        if max_ == m[i][j]:
            x = [str1[j]] + x
            y = [str2[i]] + y
            i -= 1
            j -= 1
        else:
            max_ = max(m[i+1][j], m[i][j+1])
            if max_ == m[i+1][j]:
                x = [str1[j]] + x
                y = ['-'] + y
                j -= 1
            else:
                x = ['-'] + x
                y = [str2[i]] + y
                i -= 1
        if max_ == 0:
            break
    print(int(score))
    print(''.join(x))
    print(''.join(y))
    
    return score, x, y

if __name__ == "__main__":

    with open('PAM.txt', 'r') as file:
        matrix = file.readline().rstrip().split()
        pam = []
        for x in range(len(matrix)):
            line = file.readline().rstrip().split()
            pam.append([int(line[i]) for i in range(1, len(line))])
            
    with open('rosalind_ba5f.txt', 'r') as file:
        str1 = file.readline().rstrip()
        str2 = file.readline().rstrip()
    #str2 = 'PLEASANTLY'
    #str1 = 'MEANLY'
    
    local_alignment(str1, str2, pam, matrix)
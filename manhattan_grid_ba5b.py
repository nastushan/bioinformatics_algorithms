'''

Find the Length of a Longest Path in a Manhattan-like Grid

Length of a Longest Path in the Manhattan Tourist Problem
Find the length of a longest path in a rectangular city.

Given: Integers n and m, followed by an n × (m+1) matrix Down and an (n+1) × m matrix Right. The two matrices are separated by the "-" symbol.

Return: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid whose edges are defined by the matrices Down and Right.

'''


import numpy as np

def ManhattanLikeGrid(n, m, Down, Right):
    l = []
    for i in range(m + 1):
        l.append(0)
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            l.append(0)
        l[i][0] = l[i - 1][0] + Down[i - 1][0]
    
    for a in range(1, m + 1):
        l[0][a] = l[0][a - 1] + Right[0][a - 1]

    for i in range(1, n + 1) :
        for j in range (1, m + 1) :
            S[i][j] = max(S[i - 1][j] + Down[i - 1][j], S[i][j - 1] + Right[i][j - 1])

    return S[n][m]

if __name__ == "__main__":
    
    n = 4
    m = 17
    Down = np.array([[1,2,4,3,1,4,2,1,4,4,0,3,0,0,2,1,2,4],[2,2,1,4,4,3,0,3,1,3,2,4,2,1,1,2,0,3], [3,4,1,3,2,4,3,3,3,0,3,1,3,4,4,3,2,0], [1,3,1,2,4,4,3,4,0,3,2,0,0,2,3,3,2,1]])
    Right = np.array([[1,2,0,1,2,1,3,4,2,2,1,1,1,2,0,4,1],[4,1,1,0,4,3,4,4,0,1,3,4,3,2,3,2,0],[0,0,3,1,4,0,4,1,0,2,1,0,3,3,3,4,3],[2,0,4,1,0,4,2,4,4,3,1,3,1,3,3,0,1],[4,1,2,3,1,1,1,1,1,0,4,2,0,4,4,2,3]])
    print(ManhattanTourist(n, m, Down, Right))
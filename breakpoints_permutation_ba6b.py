'''

Compute the Number of Breakpoints in a Permutation

Number of Breakpoints Problem
Find the number of breakpoints in a permutation.

Given: A signed permutation P.

Return: The number of breakpoints in P.

'''


def breakpoints(data):
    num = 0
    for i in range(len(data) - 1):
        if int(data[i]) == int(data[i+1]) - 1:
            continue
        else:
            num += 1
    print(num)

if __name__ == "__main__":
    
    with open('rosalind_ba6b.txt', 'r') as file:
        line = file.readline().strip().split()
        for i in range(len(line)):
            data = [0] + line + [len(line) + 1]
            
    breakpoints(data)
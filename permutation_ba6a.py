'''

Implement GreedySorting to Sort a Permutation by Reversals

Implement GreedySorting
Given: A signed permutation P.

Return: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity permutation.

'''


def reverse(seq):
    seq = [-i for i in seq]
    return seq[::-1]


def answer(data):
    st = '('
    for i in data:
        st += ('+' + str(i) if i > 0 else str(i)) + ' '
    st = st[:-1]
    st += ')'
    file.write(st + '\n')
    
    return st

    
def greedysorting(data):
    for i in range(1, len(data) + 1):
        if i in data:
            j = data.index(i)
        else:
            j = data.index(-i)
        if j != i-1 or data[j] != i:
            data = data[:i-1] + reverse(data[i-1:j+1]) + data[j+1:]
            answer(data)
            if data[i-1] < 0:
                data[i-1] = i
                answer(data)
    return data


if __name__ == "__main__":
    with open("rosalind_ba6a.txt") as f:
        line = f.readline().strip()
        data = list(map(int, line.strip('()').split()))
    with open("out.txt", 'w') as file:
        greedysorting(data)
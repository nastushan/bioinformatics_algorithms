'''

Find Substrings of a Genome Encoding a Given Amino Acid String

There are three different ways to divide a DNA string into codons for translation, one starting at each of the first three starting positions of the string. These different ways of dividing a DNA string into codons are called reading frames. Since DNA is double-stranded, a genome has six reading frames (three on each strand), as shown in Figure 1.

We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide.

Peptide Encoding Problem
Find substrings of a genome encoding a given amino acid sequence.

Given: A DNA string Text and an amino acid string Peptide.

Return: All substrings of Text encoding Peptide (if any such substrings exist).

'''

def ReverseComplement(Pattern):
    return Pattern[::-1].replace('A', '-').replace('T', 'A').replace('-', 'T')\
                        .replace('C', '-').replace('G', 'C').replace('-', 'G')

def dna_to_rna(Text):
    return Text.replace('T','U')

def Translation(pattern, set_code, l):
    n = ''
    for i in range(l, len(pattern) + 1, 3):
        for x, y in set_code.items():
            if pattern[i:i + 3] == x:
                if y != 0:
                    n += y
                else:
                    n += '*'
    return n

def PeptideEncode(Text, Peptide, set_code):
    pos = []
    substring = []
    string = dna_to_rna(Text)
    rev_string = dna_to_rna(ReverseComplement(Text))
    string0 = Translation(string, set_code, 0)
    string1 = Translation(string, set_code, 1) 
    string2 = Translation(string, set_code, 2)
    reverse0 = Translation(rev_string, set_code, 0)
    reverse1 = Translation(rev_string, set_code, 1)
    reverse2 = Translation(rev_string, set_code, 2)
    read_frame = [string0, string1, string2, reverse0, reverse1, reverse2]    
    for i in range(0, len(read_frame)):
        for j in range(0, len(read_frame[i]) + 1, len(Peptide)):
            if read_frame[i][j:j + 2] == Peptide:
                pos.append(j)
                if i == 0: 
                    substring.append(Text[j*3:(j*3) + 6]) 
                elif i == 1:
                    substring.append(Text[(j + 1)*3:((j + 1)*3) + 6])
                elif i == 2:
                    substring.append(Text[(j + 2)*3:((j + 2)*3) + 6])
                elif i == 3:
                    rc = (ReverseComplement(Text)[j*3:(j*3) + 6])
                    substring.append(rc)
                elif i == 4:
                    rc = (ReverseComplement(Text)[(j + 1)*3:((j + 1)*3) + 6])
                    substring.append(rc)
                else:
                    rc = (ReverseComplement(Text)[(j + 2)*3:((j + 2)*3) + 6])
                    substring.append(rc)
    return substring

if __name__ == "__main__":
     
    filename = 'rosalind_ba4b.txt'
    with open(filename) as file:
        line = file.read().splitlines()
        Text = line[0]
        Peptide = line[1]
    
    set_code = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP', 'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

    print(PeptideEncode(Text, Peptide, set_code))
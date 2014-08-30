#Creating a Distance Matrix
#PDST

"""Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001."""

import numpy as np

def fasta_extract(f):
    """Extracts sequences and their title from text files with FASTA formatting"""
    from re import sub
    L = []
    seqs = []
    count = 0
    line = f.readline()
    titles = []
    while line:
        if line[0] == '>':
            if L:
                seqs.append(''.join(L))
            else:
                pass
            titles.append(line[1:])
            L = []
            count += 1
        else:
            L.append(line)
        line = f.readline()
    else:
        seqs.append(''.join(L))
    #get rid of newlines
    for index, sequence in enumerate(seqs):
        seqs[index] = sub('\n','',sequence)
    return seqs

f = open('rosalind_pdst.txt','r')
seqs = fasta_extract(f)
f.close()
    
D = np.zeros((len(seqs),len(seqs)))
for i,seq in enumerate(seqs):
    for j,seq2 in enumerate(seqs):
        if seq == seq2:
            break
        else: #do comparison
            d = 0
            for k,char in enumerate(seq):
                if char != seq2[k]:
                    d += 1
            D[i][j] = d/len(seq)
#D is diagonal, need to fill in other half (then print while we're cycling through
for i in range(len(D[i])):
    for j in range(len(D[j])):
        D[i][j] = D[j][i]
        print(str.format('{0:.5f}',D[i][j]),end = ' ')
    print('')
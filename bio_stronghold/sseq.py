#Finding a Spliced Motif
#SSEQ

"""Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one."""

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
    return(seqs)
    
seqs = fasta_extract(open('rosalind_sseq.txt','r'))
super = seqs[0]
sub = seqs[1]
x = -1
L = []
for char in sub:
    x = super.find(char,x+1)
    if x >= 0:
        L.append(x+1)
    else:
        print('sub not found in super')
        break

for l in L:
    print(l,end =' ')
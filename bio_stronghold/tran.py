#Transitions and Transversions
#TRAN

def fasta_extract(f):
    """Extracts sequences and their title from text files with FASTA formatting"""
    import re
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
        seqs[index] = re.sub('\n','',sequence)
    return(seqs)

seqs = fasta_extract(open('rosalind_tran.txt','r'))
print(seqs)    
d_comp = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
transition = 0
transversion = 0
for i, c in enumerate(seqs[0]):
    if seqs[1][i] == d_comp[c]:
        transition += 1
    elif seqs[1][i] == c:
        pass
    else:
        transversion += 1
    #print(c,seqs[1][i],transition,transversion,sep='\t')
        
ratio = transition/transversion
print(ratio)
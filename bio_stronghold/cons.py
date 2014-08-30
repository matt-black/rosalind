#Consensus and Profile
#CONS

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
    for index, title in enumerate(titles):
        titles[index] = title.rstrip()
    for index, sequence in enumerate(seqs):
        seqs[index] = re.sub('\n','',sequence)
    return (titles, seqs)
f = open('rosalind_cons.txt','r')
(names, sequences) = fasta_extract(f)

def consensus(seqs):
    """Generate consensus array and analyze it to generate consensus sequence"""
    from numpy import array
    from numpy import zeros
    from numpy import argmax
    #generate consensus sequence
    cons_array = zeros((4,len(seqs[0])),dtype=int)
    refD = {'A':0,'C':1,'G':2,'T':3}
    for seq in seqs:
        for index, char in enumerate(seq):
            cons_array[refD[char]][index] += 1
    #analyze cons_array
    refD2 = {0:'A',1:'C',2:'G',3:'T'}
    L = []
    for i in range(len(seqs[0])):
        col = cons_array[:,i]
        max_ind = argmax(col)
        L.append(refD2[max_ind]) 
    return (''.join(L),cons_array)

(cons_seq,cons_arr) = consensus(sequences)
#print the results
print(cons_seq)
refD2 = {0:'A',1:'C',2:'G',3:'T'}
for i in range(4):
    print(refD2[i]+':',end=' ')
    for j in range(len(cons_seq)):
        print(cons_arr[i][j],end=' ')
    print('',end='\n')
    
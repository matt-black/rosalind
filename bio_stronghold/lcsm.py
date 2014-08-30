#Finding a Shared Motif
#LCSM

"""Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)"""

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

seqs = fasta_extract(open('rosalind_lcsm.txt','r'))

def long_substr(seqs):
    substr = ''
    #check for data
    if len(seqs) > 1 and len(seqs[0]) > 0:
        #cycle through each letter in first string
        for i in range(len(seqs[0])):
            #only cycle through remaining letters
            for j in range(len(seqs[0])-i+1):
                if j > len(substr) and is_substr(seqs[0][i:i+j],seqs):
                    substr = seqs[0][i:i+j]
    return substr

is_substr = lambda sub, seqs: all(sub in seq for seq in seqs)

longsub = long_substr(seqs)
print(longsub)

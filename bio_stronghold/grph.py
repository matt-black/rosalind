#Overlap Graphs
#GRPH

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
            titles.append(line[1:].rstrip())
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
    return(titles, seqs)
    
def dict_construct(names, seqs):
    D = {}
    for i, name in enumerate(names):
        D[name] = (seqs[i][0:3],seqs[i][-3:])
    return D

def adjlist(d):
    for pref in d: #prefixes
        for suff in d: #suffixes
            #print(d[pref][0],d[suff][1])
            if d[pref][0] == d[suff][1] and pref != suff:
                #match found
                print(suff,pref,sep = ' ',end='\n')
    
(titles,seqs) = fasta_extract(open('rosalind_grph.txt','r'))
D = dict_construct(titles,seqs)
adjlist(D)
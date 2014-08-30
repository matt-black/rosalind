#Speeding up Motif Finding
#KMP

"""KMP Algorithm"""

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

def fail_array(seq):
    j = -1
    fail = [j]
    for ind, char in enumerate(seq):
        while j >= 0 and seq[j] != char:
            j = fail[j]
        j += 1
        fail.append(j)
    return fail[1:]
        
seq = fasta_extract(open('rosalind_kmp.txt','r'))
tseq = 'CAGCATGGTATCACAGCAGAG'
fail = fail_array(seq[0])
f = open('answer.txt','w')
f.write(' '.join(map(str,fail)))
f.close()

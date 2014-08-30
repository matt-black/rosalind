#Speeding Up Motif Finding
#KMP

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
    fail = [] #by convention, fail[0] = 0
    for i, char in enumerate(seq):
        j = i
        k = 1
        while j>0:
            pref = seq[0:j]
            try:
                suff = seq[k:i+1]
            except IndexError:
                suff = seq[1:]
            if pref == suff:
                fail.append(j)
                break                
            else:
                j -= 1
                k += 1
                continue
        else:
            fail.append(0)
    return fail

tseq = 'CAGCATGGTATCACAGCAGAG'
seqs = fasta_extract(open('rosalind_kmp.txt','r'))
x = fail_array(seqs[0])
for item in x:
    print(item,end = ' ')
#Locating Restriction Sites
#REVP

"""Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order."""

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
    return(seqs[0])

def find_candidates(seq, i):
    L = []
    d = {'A':'T','T':'A','C':'G','G':'C'}
    for j in range(3,11,2):
        try:
            if d[seq[i+j]] == seq[i]:
                L.append(seq[i:i+j+1])
        except IndexError:
            if seq[i:] == seq[i]:
                L.append(seq[i:])
            break
    #print(i, L)
    #print('-----------------')
    return L

def reverse_complement(seq):
    d = {'A':'T','T':'A','C':'G','G':'C'}
    rev_comp = []
    for char in seq[::-1]:
        rev_comp.append(d[char])
    return ''.join(rev_comp)

def caller(seq):
    result = []
    for i,c in enumerate(seq):
        cands = find_candidates(seq,i)
        for cand in cands:
            rev_comp_cand = reverse_complement(cand)
            if cand == rev_comp_cand:
                result.append((i+1,len(cand)))
    return result

tseq = fasta_extract(open('rosalind_revp.txt','r'))
tseq2 = 'TCAATGCATGCGGGTCTATATGCAT'
answers = caller(tseq)
for answer in answers:
    print(answer[0],answer[1])

    
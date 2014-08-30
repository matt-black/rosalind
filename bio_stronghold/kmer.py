#k-Mer Composition
#KMER

"""Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s."""

def fasta(file_in):
    seq = []
    for i,line in enumerate(file_in):
        if i != 0:
            seq.append(line.rstrip())
    return ''.join(seq)

def build_dict(num):
    from itertools import combinations_with_replacement as combos
    from itertools import permutations
    L = ['A','C','G','T']
    dkeys = list(combos(L,num))
    for key in dkeys:
        perms_k = permutations(key)
        for perm in perms_k:
            if perm not in dkeys:
                dkeys.append(perm)
    d = {''.join(dkeys[i]): 0 for i in range(len(dkeys))}
    return d
    
def kmer_array(seq,d):
    from re import findall
    karr = []
    for key in d:
        x = findall('(?=('+key+'))',seq)
        d[key] += len(x)
    #now sort the keys and go through them
    for key in sorted(d.keys()):
        karr.append(d[key])
    return karr

##testing    
tseq = 'TTGATTACCTTATTTGATCATTACACATTGTACGCTTGTGTCAAAATATCACATGTGCCT'
d = build_dict(2)
arr = kmer_array(tseq,d)
for ar in arr:
    print(ar,end=' ')
##actual - select below & run selection
f = open('rosalind_kmer.txt','r')
seq = fasta(f)
f.close()
d = build_dict(4)
arr = kmer_array(seq,d)
for ar in arr:
    print(ar,end=' ')    
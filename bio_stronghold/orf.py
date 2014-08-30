#Open Reading Frames
#ORF

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

(name, sequence) = fasta_extract(open('rosalind_orf.txt','r'))

def get_frames(sequence):
    seqs = []
    #convert DNA -> RNA
    M = []
    Rseqs = []
    for index, char in enumerate(sequence):
        if char == 'T':
            M.append('U')
        else:
            M.append(char)
    for i in range(3):
        Rseqs.append(''.join(M[i:]))
    #generate reverse complement
    N = []
    drev = {'A':'U','U':'A','C':'G','G':'C'}
    for i in range(len(Rseqs)):
        sequence2 = Rseqs[i][::-1]
        for char in sequence2:
            N.append(drev[char])
        Rseqs.append(''.join(N))
        N = []
    return Rseqs
def translate(RNA_list):
    dp = {"UUU":"F", "UUC":"F", "UUA":"L", 
    "UUG":"L","UCU":"S", "UCC":"S", "UCA":"S", 
    "UCG":"S","UAU":"Y", "UAC":"Y", "UAA":"Stop",        
    "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    prot_list = []
    for RNA in RNA_list:
        print(count)
        codons = []
        its = [x for x in range(len(RNA)) if x%3==0]
        for i in its:
            try: codons.append(RNA[i:i+3])
            except IndexError: codons.append(RNA[i:])
        if 'AUG' in codons:
            P = []
            for codon in codons:
                try: P.append(dp[codon])
                except KeyError: break
            prot_list.append(''.join(P))
    return prot_list
    
def get_orfs(aaseqs):
    for aaseq in aaseqs:
        while 'M' in aaseq:
            
x = get_frames(sequence[0])
print('------------------')
print(x)
y = translate(x)
print('------------------')
print(y)
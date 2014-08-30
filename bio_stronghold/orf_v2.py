#Open Reading Frames
#ORF

"""Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order."""

#Modify the line, below
seq_in = 'CGTGGGCGTGCATGCGTCGTTGACGATATGTTTACTAACCTATCGGAGCGAGTTGAGCCACGGCCCTGAGGAAGATTTGAAGTTCAGATAGAAGCGCAAACTTTATTCCGGTTTCCGACAGAATCCTTCTAGTCAGGCTAGGATTTCTGAGACTTCGATTTCTCATTGTAGGTGCTGCTTACCTATATTTATTAAAACAGACAATTGCTATTTGAGCCCGAAGGCTTCAGAGACGCAAGAAAAACAGACAAAAGGTTCGAGAACTAGAAGAAAATACAGGGATTCGGTCGTACTAGACGAACTAAAGTGACACGGTAACACTTCTGGGATGATGAATTCGCGTGCGCTAGCTCGGTTCTACTGAGGCCCTTCCTGCAGCGCGAAATGTCAGTCTCACCCCCCGCGTCCCAAGCTGTGCCCACCCTATTAGTGACACCGCAACAAAATAGTTAAAGTTAATGTATACGAGGTGAACAGCAGACAGACGCTAGCTAGCGTCTGTCTGCTGTTCACCTCGTATACATTAGCGGGAGCGGACTCCCAACAGACTGTATGCCAATGTTGCTACAACACATGTCTGTTACGCGCTAGGCCGAAACTTGAAACGACTAACACTAGAGGTTAACTGCGTACAGCATCATAAGCGTATTAGGATGCGGCCCCTCCCGGTGCGGCGTTCAGTTCTAATTCGCCATCTAACCGTGCGGACGGGGCGTCTCAGTGCGAACGTCCTCCGGCACTTGAGGTTAGCAGTACCCGATTATGCATGTCAAATCCTCTCCGCCCAGTCATTCCTGATCTTTCCAAGCACGTTGCTACCGGGAATTCATGACTTCGACGCGATGGCCGCCGCATTGACCCAGCTTTGTCTGTAATCACTGGTCAAGTTAGTCGTACAGGTCGGGATATATTGTGAGCTTGCCCCATGGAGGTCTATCTCGCTAACAGATAGTGTAACCGGTCTACGGGACTGAACCGGCAA'

def DNAtoRNA(DNAseq):
    DNA_list = []
    for char in seq:
        if char == 'T':
            DNA_list.append('U')
        else: 
            DNA_list.append(char)
    return ''.join(DNA_list)
    
def reverse_complement(seq):
    d = {'A':'T','T':'A','C':'G','G':'C'}
    rev_comp = []
    for char in seq[::-1]:
        rev_comp.append(d[char])
    return ''.join(rev_comp)
    
def get_seqs(seq,seq_rev):
    seqs_out = []
    for seq in (seq,seq_rev):
        for i in range(3):
            seqs_out.append(seq[i:])
    return seqs_out
    
def translate(seqs):
    #generate codon hashtable
    bases = ['T', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYYssCCsWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))
    #do the translation
    protseqs = []
    for seq in seqs:
        L = []
        iterlist = [x for x in range(len(seq)) if x%3 == 0]
        for i in iterlist:
            try: L.append(codon_table[seq[i:i+3]])
            except KeyError: break
        protseqs.append(''.join(L))
    return protseqs

rev_comp = reverse_complement(seq_in)
DNAseqs = get_seqs(seq_in,rev_comp)
protseqs = translate(DNAseqs)

def find_seqs(protseqs):
    import re
    L = []
    for protseq in protseqs:
        #print(protseq)
        match = re.findall(r'(?=(M[A-Z]*)s)',protseq)
        for item in match:
            if item not in L:
                L.append(item)
    return L
x = find_seqs(protseqs)
for seq in x:
    print(seq)

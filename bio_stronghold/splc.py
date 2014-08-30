#RNA Splicing
#SPLC

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
    super = seqs[0]
    subs = seqs[1:]
    return(super, subs)

def splice_convert(sequence, introns):
    for intron in introns:
        exon = sequence.replace(intron,'')
    for i in range(len(exon)):
        if exon[i] == 'T':
            exon[i] =='U'
        else:
            pass
    start_ind = exon.find('AUG')
    if start_ind > 0:
        ex_out = exon[start_ind:]
    else:
        raise('Start codon not found')
    return ex_out
    
def translate(RNAseq):
    """Translates a given RNA sequence, where the first codon is the start codon"""
    d = {"UUU":"F", "UUC":"F", "UUA":"L", 
    "UUG":"L","UCU":"S", "UCC":"s", "UCA":"S", 
    "UCG":"S","UAU":"Y", "UAC":"Y", "UAA":"STOP",        
    "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
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
    iterlist = [x for x in range(len(RNAseq)) if x%3 ==0]
    protlist = []
    for i in iterlist:
        protlist.append(d[RNAseq[i:i+3]])
    return ''.join(protlist)
    
(main, introns) = fasta_extract(open('rosalind_splc.txt','r'))
RNA = splice_convert(main, introns)
print(translate(RNA)

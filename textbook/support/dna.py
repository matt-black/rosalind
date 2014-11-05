"""
Support stuff for dealing with DNA
"""

def reverse_complement(sequence):
    sequence = sequence.upper()

    #construct dict of mappings based on sequence type (dna/rna)
    mappings = {'C':'G',
                'G':'C'}
    if sequence.find('T') >= 0:  #dna
        mappings['A'] = 'T'
        mappings['T'] = 'A'
    else:  #rna
        mappings['A'] = 'U'
        mappings['U'] = 'A'

    #build the reverse complement
    opp_strand = []
    for nuc in sequence:
        opp_strand.append(mappings[nuc])
    return ''.join(opp_strand)[::-1]


def hamming_distance(string1, string2):
    if len(string1) != len(string2):
        raise ValueError("strings must be of equal length")
    s1 = list(string1)
    s2 = list(string2)
    hamming = 0
    for i in zip(s1,s2):
        if i[0] != i[1]:
            hamming += 1
    return hamming

"""
Peptide Encoding Problem
"""
from support.translate import rna_to_protein_dict
from support.dna import reverse_complement

rna_to_prot = rna_to_protein_dict()


def main(rna, prot, is_rev_comp=False):
    for seq in get_encoding_seqs(rna,prot):
        if is_rev_comp:
            print(reverse_complement(seq).replace('U','T'))
        else:
            print(seq.replace('U','T'))


def get_encoding_seqs(rna, prot):
    codons = codon_generator(rna)
    len_encoding_seq = len(prot)*3
    for i, codon in codons:
        if rna_to_prot[codon] == prot[0]:
            #check rest of the sequence
            if _check_rest(rna[i+3:i+len_encoding_seq],prot[1:]):
                yield rna[i:i+len_encoding_seq]


def _check_rest(rna, prot):
    for i in range(0,len(prot)):
        j = i*3
        if rna_to_prot[rna[j:j+3]] == prot[i]:
            continue
        else:
            return False
    return True


def codon_generator(rna, step=1):
    end = 3
    while end <= len(rna):
        yield end-3, rna[end-3:end]
        end += step


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        dna = f.readline().strip()
        prot = f.readline().strip()
    main(dna.replace('T', 'U'), prot)
    main(reverse_complement(dna).replace('T','U'), prot, True)

"""
Protein Translation Problem
"""
from support.translate import rna_to_protein_dict


def main(rna):
    rna_dict = rna_to_protein_dict()
    codons = codon_generator(rna)
    found_start = False
    while not found_start:
        codon = next(codons)
        if rna_dict[codon] == 'M':
            found_start = True
    prot_seq = ['M']
    while True:
        try:
            protein = rna_dict[next(codons)]
            if protein == 'Stop':
                break
            prot_seq.append(protein)
        except StopIteration:
            break
    print(''.join(prot_seq))


def codon_generator(rna):
    start, end = 0, 3
    while end <= len(rna):
        yield rna[start:end]
        start = end
        end += 3


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        rna = f.readline().strip()
    main(rna)

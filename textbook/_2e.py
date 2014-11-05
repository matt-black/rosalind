"""
Cyclopeptide Sequencing Problem
"""
from itertools import permutations

aminoacid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def main(spectrum):
    amino_acids, chunks = split_spectrum(spectrum)
    amino_acids = list([a] for a in amino_acids)

    print(amino_acids)
    print(chunks)
    peptides = assemble_sequences(amino_acids, amino_acids, chunks)
    #print the results
    for peptide in peptides:
        print('-'.join(map(str,peptide)), end=' ')
    print('')


def assemble_sequences(amino_acids, peptides, chunks):
    """
    Assemble the possible sequences made up of peptides, based on given chunks
    using branch-and-bound
    """
    new_peptides = []
    if len(chunks) == 1:
        for peptide in peptides:
            for amino_acid in amino_acids:
                ind = _try_append(peptide, amino_acid, chunks)
                if ind is not None:
                    new_peptides.append(peptide + amino_acid)
        return new_peptides

    for peptide in peptides:
        for amino_acid in amino_acids:
            ind = _try_append(peptide, amino_acid, chunks)
            if ind is not None:
                new_peptides.append(peptide + amino_acid)
                chunks.pop(ind)
    return assemble_sequences(amino_acids, new_peptides, chunks)


def _try_append(base_peptide, new_amino_acid, chunks):
    """
    Appends new_amino_acid to base_peptide and checks if it forms a valid
    chunk in the chunks array
    """
    new_peptide = base_peptide + new_amino_acid
    try:
        return chunks.index(sum(new_peptide))
    except ValueError:
        return None


def split_spectrum(spectrum):
    """
    Splits the experimental spectrum, returning the part of the spectrum
    representing the amino acids in the peptide and the combinations
    """
    #split the spectrum out to stuff we know isn't an amino acid
    total = 0
    i = -1
    while total != spectrum:
        i += 1
        if spectrum[i] > aminoacid_masses[-1]:
            i -= 1
            break
        elif spectrum[i] == aminoacid_masses[-1]:
            break
        total += spectrum[i]

    pep_cands = spectrum[1:i+1]  #potential aa's in the peptide
    seq_cands = spectrum[i+1:]  #potential peptide sequences

    #find any pep_cands that aren't amino acids, move to seqs
    k = 0  #track how many times we've popped
    for j,cand in enumerate(list(pep_cands)):
        if cand not in aminoacid_masses:
            seq_cands.append(pep_cands.pop(j-k))
            k += 1

    return pep_cands, sorted(seq_cands)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        spectrum = [int(val) for val in f.readline().strip().split()]
    main(spectrum)

"""
Generating Theortical Spectrum Problem
"""
from support.mass_spec import amino_acid_map


def main(peptide):
    aa_weight_map = amino_acid_map(int)
    masses = [0, peptide_weight(peptide, aa_weight_map)]
    #calculate all subpeptide weights
    for sp_len in range(1,len(peptide)):
        for sp in peptides(peptide, sp_len):
            masses.append(peptide_weight(sp, aa_weight_map))
    print(' '.join(map(str, sorted(masses))))


def peptide_weight(peptide, aa_mass_map):
    mass = 0
    for aa in peptide:
        mass += aa_mass_map[aa]
    return mass


def peptides(peptide, length):
    if length > len(peptide):
        raise ValueError("subpeptide length can't be greater than peptide")
    pep = ''.join([peptide]*2)
    i, j = -1, length-1
    peps = []
    while j <= len(pep)-1:
        i +=1
        j += 1
        p = pep[i:j]
        if i < len(pep)/2:
            yield p
        else:
            if p in peps:
                continue
            else:
                yield p
        peps.append(p)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        peptide = f.readline().strip()
    main(peptide)

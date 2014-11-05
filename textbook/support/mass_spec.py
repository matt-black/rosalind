"""
Mass spectroscopy utilities
"""
import os

def amino_acid_map(precision=int):
    mapping = dict()
    with open(os.path.join(os.path.dirname(__file__),
                           "aa_mass_table.txt")) as f:
        for line in f:
            l = line.strip().split()
            mapping[l[0]] = precision(float(l[1]))
    return mapping

if __name__ == "__main__":
    print(amino_acid_map(int))

"""
Utilities for translation-related tasks
"""
import os

def rna_to_protein_dict():
    rna_dict = {}
    with open(os.path.join(os.path.dirname(__file__), 'rna_codon_table.txt')) as f:
        for line in f:
            data = line.strip().split()
            rna_dict[data[0]] = data[1]
    return rna_dict

## for testing
if __name__ == "__main__":
    print(rna_to_protein_dict())

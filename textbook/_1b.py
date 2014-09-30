"""
Reverse Complement Problem
"""
import sys

complement = {
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C"
}

def main(input_file):
    seq = make_sequence_list(input_file)
    rev_comp = make_reverse_complement(seq)
    print(rev_comp)

def make_sequence_list(input_file):
    """
    Read in a sequence from a file and return a list of nucleotides
    from that sequence
    """
    with open(input_file) as f:
        seq = f.readline().strip()
    return list(seq)

def make_reverse_complement(sequence):
    rev_comp = []
    while sequence:
        rev_comp.append(complement[sequence.pop()])
    return ''.join(rev_comp)

if __name__ == "__main__":
    main(sys.argv[1])

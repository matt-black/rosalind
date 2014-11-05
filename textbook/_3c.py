"""
Profile-most Probable k-mer Problem
"""

from operator import mul


def main(sequence, k, profile):
    best_pattern = ""
    best_probability = float(0)
    for kmer in seq_kmers(sequence, k):
        new_probability = calculate_probability(kmer, profile)
        if new_probability > best_probability:
            best_pattern = kmer
            best_probability = new_probability
    print best_pattern


def calculate_probability(kmer, profile, mappings={'A':0,'C':1,'G':2,'T':3}):
    t = []
    for i in range(len(kmer)):
        row = mappings[kmer[i]]
        t.append(profile[row][i])
    return reduce(mul, t, 1)


def seq_kmers(sequence, k):
    seq = list(sequence)
    while len(seq) >= k:
        yield ''.join(seq[0:k])
        seq.pop(0)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        sequence = f.readline().strip()
        k = int(f.readline().strip())
        profile = [list(map(float,line.strip().split())) for line
                   in f.readlines()]

    main(sequence, k, profile)

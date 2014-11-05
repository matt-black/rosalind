"""
Median String Problem
"""

from support.dna import hamming_distance
from itertools import product
from operator import itemgetter

def main(sequences, k):
    d = dict()
    strings = dict((''.join(string), 0) for string in product('ATCG', repeat=k))
    for sequence in sequences:
        for string in strings:
            if string not in d:
                d[string] = get_hamming_dist(string, sequence)
            else:
                d[string] += get_hamming_dist(string, sequence)
    #find the min d value
    sorted_d = sorted(d.items(), key=itemgetter(1))
    print(sorted_d[0][0])


def get_hamming_dist(kmer, sequence):
    k = len(kmer)
    seq_kmers = [sequence[i:i+k] for i in range(0,len(sequence)-k)]
    if kmer in seq_kmers:
        return 0
    else:
        min_hd = k+1
        for sk in seq_kmers:
            if hamming_distance(sk, kmer) < min_hd:
                min_hd = hamming_distance(sk, kmer)
        return min_hd

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        k = int(f.readline().strip())
        sequences = [line.strip() for line in f.readlines()]
    main(sequences, k)

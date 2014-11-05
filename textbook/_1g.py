"""
Frequent Words with Mismatches Problem
"""
from itertools import combinations, product
from _1a import get_freq_kmers

def main(genome, k, d):
    genome = list(genome)
    kmers = get_approx_kmers(genome, k, d)
    most_freq = get_freq_kmers(kmers)
    print(' '.join(most_freq))


def get_approx_kmers(genome, k, d):
    kmers = dict()
    muts = dict()
    for kmer in sequence_kmers(genome, k):
        approxes = muts.get(kmer,
                            get_mutations_for_kmer(kmer, d))
        for a in approxes:
            kmers[a] = kmers.get(a, 0) + 1
    return kmers


def get_mutations_for_kmer(kmer, d, charset='ATCG'):
    mutations = [kmer]
    for inds in combinations(range(len(kmer)), d):
        for reps in product(charset, repeat=d):
            mutation = list(kmer)
            for i, r in zip(inds, reps):
                mutation[i] = r
            mutations.append(''.join(mutation))
    return list(set(mutations))


def sequence_kmers(genome, k):
    while len(genome) >= k:
        yield ''.join(genome[0:k])
        genome.pop(0)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        text = f.readline().strip()
        k, d = map(int, f.readline().strip().split())
    main(text, k, d)

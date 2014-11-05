"""
Frequent Words with Mismatchse and Reverse Complements Problem
"""

from _1a import get_freq_kmers
from _1g import get_mutations_for_kmer, sequence_kmers
from support.dna import reverse_complement

def main(genome, k, d):
    genome = list(genome)
    kmers = get_approx_kmers_with_revcomp(genome, k, d)
    most_freq = get_freq_kmers(kmers)
    print(' '.join(most_freq))


def get_approx_kmers_with_revcomp(genome, k, d):
    kmers = dict()
    muts = dict()
    for kmer in sequence_kmers(genome, k):
        approxes = muts.get(kmer,
                            get_mutations_for_kmer(kmer,d))
        rev_comp = reverse_complement(kmer)
        approxes_rev = muts.get(rev_comp,
                                get_mutations_for_kmer(rev_comp,d))
        for a in approxes + approxes_rev:
            kmers[a] = kmers.get(a,0) + 1
    return kmers


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        text = f.readline().strip()
        k, d = map(int, f.readline().strip().split())
    main(text, k, d)

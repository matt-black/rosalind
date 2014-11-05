"""
Motif Enumeration
"""
# look up planted motif search for help on this
from itertools import combinations, product

def main(sequences, k, d):
    motifs = implanted_motifs(sequences, k, d)
    print(' '.join(motifs))

def implanted_motifs(sequences, k, d):
    kmer_dict = {}
    for sequence in sequences:
        seq_kmers = []
        #find all unique (k,d)-kmers in the sequence
        for kmer in sequence_kmers(sequence, k):
            if kmer in seq_kmers:
                pass
            else:
                seq_kmers.append(kmer)
            for mut in get_mutations_for_kmer(kmer,d):
                if mut in seq_kmers:
                    continue
                else:
                    seq_kmers.append(mut)
        #add each kmer to the dict-tally
        for kmer in seq_kmers:
            if kmer in kmer_dict:
                kmer_dict[kmer] += 1
            else:
                kmer_dict[kmer] = 1
    #find common kmers
    common = dict((kmer, occur) for kmer, occur
                  in kmer_dict.items()
                  if occur == len(sequences))
    return common.keys()

def sequence_kmers(sequence, k):
    seq = list(sequence)
    while len(seq) >= k:
        yield(''.join(seq[0:k]))
        seq.pop(0)

def get_mutations_for_kmer(kmer, d, charset='ATCG'):
    mutations = []
    for inds in combinations(range(len(kmer)), d):
        for reps in product(charset, repeat=d):
            mutation = list(kmer)
            for i, r in zip(inds, reps):
                mutation[i] = r
            yield ''.join(mutation)

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        k, d = map(int, f.readline().strip().split())
        seqs = [line.strip() for line in f.readlines()]
    main(seqs, k, d)

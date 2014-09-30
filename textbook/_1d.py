"""
Clump Finding Problem
"""
import sys
from _1a import KmerSequence

def main(input_file):
    #read in values from file
    with open(input_file) as f:
        genome = f.readline().strip()
        k, l, t = map(int, f.readline().strip().split())
    clumps, kmers  = initialize_sequence(genome, k, l, t)
    clumps = find_more_clumps(genome, k, l, t, clumps, kmers)
    print(' '.join(clumps))

def find_more_clumps(sequence, k, l, t, clumps, kmers):
    """
    Find all (L,t)-clumps of length k in the genome, seq, after
    that seq has been initialized
    """
    start, end = 0, l+2  #starting values for the reading frame
    while end <= len(sequence):
        kmer_to_add = sequence[end-k:end]
        if not kmer_to_add in kmers:
            kmers[kmer_to_add] = 1
        else:
            kmers[kmer_to_add] += 1
            if kmers[kmer_to_add] == t:
                clumps = tryadd_clumps(kmer_to_add, clumps)
        kmer_to_remove = sequence[start:start+k]
        kmers[kmer_to_remove] -= 1
        #advance the reading frame
        start += 1
        end += 1
    return clumps

def initialize_sequence(seq, k, l, t):
    """
    Initialize the sequence for further finding and starts
    the clumps dictionary that tracks (L,t) clumps
    """
    kmers = {}
    clumps = []
    init_seq = KmerSequence(seq[0:l+1], k)
    while True:
        try:
            kmer = next(init_seq)
            if not kmer in kmers:
                kmers[kmer] = 1
            else:
                kmers[kmer] += 1
                if kmers[kmer] == t:
                    clumps = tryadd_clumps(kmer, clumps)
        except StopIteration:
            break
    return clumps, kmers

def tryadd_clumps(kmer, clumps):
    """Add a kmer to the clumps list if it isn't already in it"""
    #print(kmer + ' | ' + ';'.join(clumps))
    if kmer not in clumps:
        clumps.append(kmer)
    return clumps

if __name__ == "__main__":
    main(sys.argv[1])

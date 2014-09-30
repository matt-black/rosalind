"""
Frequent Words Problem
"""
import sys

def main(file_path):
    with open(file_path) as input_file:
        #read in the file
        seq = input_file.readline().rstrip()
        kmer_len = int(input_file.readline().rstrip())
    sequence = KmerSequence(seq, kmer_len)
    kmer_dict = {}
    while True:
        try:
            kmer = next(sequence)
            if not kmer  in kmer_dict:
                kmer_dict[kmer] = 1
            else:
                kmer_dict[kmer] += 1
        except StopIteration:
            break
    kmers = get_freq_kmers(kmer_dict)
    print(' '.join(kmers))

def get_freq_kmers(kmer_dict, max_val=0):
    """
    Given a kmer_dict of frequencies, returns a list of the most frequent ones
    """
    freq_kmers = []
    for k in sorted(kmer_dict, key=kmer_dict.get, reverse=True):
        new_val = kmer_dict.get(k)
        if new_val >= max_val:
            freq_kmers.append(k)
            max_val = new_val
        else:
            return freq_kmers

class KmerSequence:
    def __init__(self, sequence, kmer_length):
        self.i = 0
        self.sequence = sequence
        self.kmer_len = kmer_length

    def __next__(self):
        start, end = self.i, self.i + self.kmer_len
        if end >= len(self.sequence):
            raise StopIteration
        else:
            self.i += 1  #move the index
            return self.sequence[start:end]

if __name__ == "__main__":
    main(sys.argv[1])

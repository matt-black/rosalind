"""
Pattern Matching Problem
"""
import sys
from _1a import KmerSequence

def main(input_file):
    #read in file contents
    with open(input_file) as f:
        pattern = f.readline().strip()
        genome = f.readline().strip()
    seq = KmerSequence(genome, len(pattern))
    inds = []
    count = -1
    while True:
        count += 1
        try:
            s = next(seq)
            if s == pattern:
                inds.append(count)
        except StopIteration:
            break
    print(' '.join(map(str,inds)))

if __name__ == "__main__":
    main(sys.argv[1])

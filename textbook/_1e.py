"""
Minimum Skew Problem
"""
import sys

def main(genome):
    skew = form_skew_array(genome)
    min_skew = min(skew)
    print(' '.join(map(str,[i for (i,sk) in enumerate(skew) if sk == min_skew])))


def form_skew_array(genome):
    """
    Make a skew array for the given genome
    """
    skew_arr = [0]  #initialize the array
    for nuc in get_next_nucleotide(genome):
        if nuc == 'C':
            skew_arr.append(skew_arr[-1]-1)
        elif nuc == 'G':
            skew_arr.append(skew_arr[-1]+1)
        else:  # nuc == 'A' or nuc == 'T'
            skew_arr.append(skew_arr[-1])
    return skew_arr

def get_next_nucleotide(sequence):
    while sequence:
        yield sequence.pop(0)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        genome = f.readline().strip()
    main(list(genome))

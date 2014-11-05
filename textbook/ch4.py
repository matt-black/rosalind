#! /usr/bin/env python3
"""
Chapter 4 Problems

Run with python3 ch4.py --problem=[a-f] --test?
"""
from argparse import ArgumentParser


letter_problem_mapping = {
    "a": "string_composition",
    "b": "overlap_graph"
}


def string_composition(k, text):
    """
    Generate the k-mer composition of a string

    Given: an integer k and a string Text
    Return: Composition_k(Text), where k-mers are in lexicographic order

    >>> string_composition_problem(5, 'CAATCCAAC')
    """
    kmers = []
    for kmer in kmer_generator(text, k):
        kmers.append(kmer)
    return kmers.sort()


def kmer_generator(sequence, k, dist=1):
    """
    Yields consecutive kmers separated by the provided value
    """
    seq = list(sequence)
    while len(seq) >= k:
        yield ''.join(seq[0:k])
        #pop values off the front for however many we next want to skip
        for i in range(dist):
            seq.pop(0)


if __name__ == "__main__":
    #create a parser to detect the problem we want to run
    parser = ArgumentParser()
    parser.add_argument("problem", help="the problem to solve, valid values are a-f")
    parser.add_argument("test", help="run the tests")
    args = parser.parse_args()

    if args.test:  #run test for that problem
        import doctest
        doctest.run_docstring_examples(args.problem, globals())
        sys.exit(0)

    #grab the file we want to look at

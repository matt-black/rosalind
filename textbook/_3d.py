"""
Greedy Motif Search
"""


def main(sequences, k, t):


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        k, t = map(int, f.readline().strip().split())
        sequences = [line.strip() for line in f.readlines()]

    main(sequences, k, t)

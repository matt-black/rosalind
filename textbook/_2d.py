"""
Counting Pepties with Given Mass Problem
"""

aminoacid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def main(mass):
    print(num_possible_peptides(mass, aminoacid_masses))


def _peptides(n, d, masses):
    for m in masses:
        if n-m in d:
            d[n] = d.get(n,0) + d[n-m]
    return d


def num_possible_peptides(M, masses):
    d = {0:1}
    _min = min(masses)
    for i in range(M-_min+1):
        j = i + _min
        _peptides(j, d, masses)
    return d[M]


if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))

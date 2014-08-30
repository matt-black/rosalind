#Maximum Matchings and RNA Secondary Structures
#MMCH

"""Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s."""

def read_in(f):
    L = []
    for i,l in enumerate(f):
        if i != 0:
            L.append(l.rstrip())
    return ''.join(L)

def build_graph(seq):
    D = {i:[] for i in range(len(seq))}
    d_match = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    for i, c1 in enumerate(seq):
        for j, c2 in enumerate(seq):
            if d_match[c1] == c2:
                D[i].append(j)
            else:
                pass
    return D
    
f = open('rosalind_mmch.txt','r')
seq = read_in(f)
f.close()

print(build_graph(seq))
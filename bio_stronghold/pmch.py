#Perfect Matchings and RNA Secondary Structures
#PMCH

"""Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s."""

from math import factorial

seq = 'UCAUGAUAGACGAAGUAGAUUGCUCGUUCGUCAAUCGGGGGCUCCACUUACCACCGGAUAGCACGCGCUGGCAGCU'
#a & c are counters for number of 'A' & 'C' bases in seq
a = 0
c = 0
for char in seq:
    if char == 'A':
        a += 1
    elif char == 'C':
        c += 1
ans = factorial(a) * factorial(c)
print(ans)

## Undirected Graph Class (Ignore)
class undirected_graph(dict):
    """An undirected graph edge list
 
    In an undirected graph edges are symmetric, so vertex order doesn't matter.
    Store lists or dictionaries to represent attributes.
 
    >>> a = undirected_graph()
    >>> a[4,5] = True
    >>> a[5,4]
    True
    >>> pair = (1,8)
    >>> a[pair] = {"weight":5,"color":"red"}
    >>> a[8,1]['color']
    'red'
    """
 
    def __getitem__(self, key, second=None):
        return super(undirected_graph, self).__getitem__(tuple(sorted(key)))
 
    def __setitem__(self, key, value):
        super(undirected_graph, self).__setitem__(tuple(sorted(key)), value)

graph = undirected_graph()

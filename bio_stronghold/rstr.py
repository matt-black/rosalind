#Matching Random Motifs
#RSTR

"""Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once."""

from math import floor, factorial
from itertools import combinations_with_replacement as combos


f = open('rosalind_rstr.txt','r')
n,GCcon,seq = read_file(f)
f.close()

def read_file(f):
    from re import search
    for i, line in enumerate(f):
        if i == 0:
            match = search('(\d+) (0\.\d+)',line)
            if match:
                n = int(match.group(1))
                GC = float(match.group(2))
            else: raise Exception("didn't find n & GC content in first line of file")
        else:
            seq = line.rstrip()
    return (n,GC,seq)

'''Calculate the number of possible strings for a given length and GC content
'''
def calculate_possibilities(gc_content, n):

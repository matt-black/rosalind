#Introduction to Random Strings
#PROB

def deconstruct(f):
    """Take in file, separate into appropriate lines"""
    seq = f.readline().rstrip()
    A_str = f.readline()
    #turn A_str into number array
    L = A_str.split(' ')
    A = []
    for item in L:
        A.append(float(item))
    return (seq,A)
    
f = open('rosalind_prob.txt','r')
(seq,A) = deconstruct(f)

def analyze_prob(seq,A_k):
    from math import log10
    probG_C = A_k/2
    probT_A = (1-A_k)/2
    d = {'G':probG_C,'C':probG_C,'T':probT_A,'A':probT_A}
    prob = 1 #initialize
    for char in seq:
        prob *= d[char]
    return log10(prob)
    
L = []
for k in A:
    L.append(analyze_prob(seq,k))
    
for l in L:
    print(l,end=' ')
else:
    print('',end='\n')
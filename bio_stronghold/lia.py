#Independent Alleles
#LIA

"""Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors."""

def prob(k,N):
    from fractions import Fraction as F
    from math import factorial as fac
    nCr = lambda n,r: int(fac(n)/(fac(r)*fac(n-r)))
    progeny_k = 2**k
    i = N
    prob_out = 0
    while i <= progeny_k:
        prob_ = (F(1/4)**i * F(3,4)**(progeny_k-i)) * nCr(progeny_k,i)
        dummy = (F(1/4)**i * F(3,4)**(progeny_k-i))
        prob_out += prob_
        print(i,dummy,nCr(progeny_k,i),prob_,sep='\t')
        i+=1
    return float(prob_out)
print(prob(6,19))
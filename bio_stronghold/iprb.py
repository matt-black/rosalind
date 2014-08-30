#Introduction to Mendelian Inheritance
#IPRB

def prob(k, m, n):
    """calculates probability that 2 randomly selected mating organisms will produce an individual with a dominant allele"""
    #k = # homozygous dominant
    #m = # heterozygous
    #n = # homozygous recessive
    
    from fractions import Fraction
    from itertools import combinations_with_replacement
    from itertools import permutations
    
    result = 0
    tot = k+m+n
    probs = []
    L = ['k','m','n']
    perms = []
    
    combos = combinations_with_replacement(L,2)
    for combo in combos:
        perms_comb = permutations(combo)
        for perm in perms_comb:
            if not perm in perms:
                perms.append(perm)
                
    D1 = {} #probability of parent matchup
    D2 = {} #probability of dominant given matchup
    for perm in perms:
        # assign values for D1
        if perm[0] == perm[1]:
            D1[perm] = Fraction(eval(perm[0]),tot)*Fraction(eval(perm[1])-1,tot-1)
        else:
            D1[perm] = Fraction(eval(perm[0]),tot)*Fraction(eval(perm[1]),tot-1)
        # assign values for D2
        if 'k' in perm:
            D2[perm] = 1
        else:
            if perm[0] != perm[1]:
                D2[perm] = Fraction(1,2)
            else:
                if 'n' in perm: D2[perm] = 0
                else: D2[perm] = Fraction(3,4)

    for key in D1:
        result += D1[key]*D2[key]
    return result
    
answer = prob(24,22,16)
print(float(answer))
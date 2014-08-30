# -*- coding: utf-8 -*-
"""
Given: Positive integers n and m with 0≤m≤n≤2000.

Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000.
"""

#define combination formula

from math import factorial

def mod_exp(base,exp,m):
    """Compute b^e mod m"""
    e = 1
    sol = 1
    while e <= exp:
        sol = (sol*base) % m
        #print e, sol
        e += 1
    return sol
    
print mod_exp(4,13,497)    

def mod_factorial(x,m):
    count = x
    sol = 0
    while count > 0:
        sol = (sol + count*(count-1)) % m
        print sol, count
        count -= 1
    return sol
    
print mod_factorial(10,100000)

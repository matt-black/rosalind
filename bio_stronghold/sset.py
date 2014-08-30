#Counting Subsets
#SSET

"""Given: A positive integer n (n≤1000).

Return: The total number of subsets of {1,2,…,n} modulo 1,000,000."""

n = 930 #GIVEN

from itertools import combinations
from math import factorial

nCk = lambda n,k: factorial(n)/(factorial(k)*factorial(n-k))
I = range(1,n+1)
ans = 1
for i in I:
    ans += nCk(n,i)
ans = ans % 1000000
print(ans)
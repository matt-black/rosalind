#Partial Permutations
#PPER

"""Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000."""

from math import factorial

n = 88
k = 9

nCk = lambda n,k: factorial(n)/(factorial(k)*factorial(n-k))

nPk = lambda n,k: factorial(n)/factorial(n-k)

x = nPk(n,k) % 1000000
print(x)
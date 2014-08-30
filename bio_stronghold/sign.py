#Enumerating Oriented Gene Orderings
#SIGN

"""Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order)."""

from itertools import permutations

n = 5 #given
L = list(range(-n,n+1))
L.remove(0) #get rid of zero value
perms = permutations(L,n)
ans = []
for perm in perms:
    for val in perm:
        #look for n/-n pairings in perm
        if -val in perm:
            break
    else: #made it through w/o finding a n/-n pair
        ans.append(perm)
print(len(ans))
for an in ans:
    for a in an:
        print(a,end=' ')
    print('')
#Longest Increasing Subsequence
#LGIS

from re import findall

f = open('rosalind_lgis.txt','r')

#extract n and sequence from file
for i, line in enumerate(f):
    if i == 0:
        n = int(line.rstrip())
    else:
        P = findall('(\d+)',line)
P = list(map(int, P)) #convert to ints
Q = [2, 6, 3, 4, 1, 2, 9, 5, 8] #testing

def build_S(perm):
    S = [perm[0]] #initialize S
    for i in perm[1:]:
        if i > S[-1]:
            S.append(i)
        else:
            #find smallest val in S >= i
            repl = min([x for x in S if x >= i])
            #replace that value with i
            S[S.index(repl)] = i
    I = [] #initialize list of indices of vals in S
    for j in S:
        I.append(perm.index(j))
    return S,I
    
def build_parent(S,I,perm):
    pass


    
#http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
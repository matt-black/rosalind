#Completing a Tree
#TREE

"""Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree."""

def read_in(file):
    count = 0
    from re import findall
    x = []
    for i,line in enumerate(file):
        if i == 0: n =int(line.rstrip())
        else:
            L = list(map(int,findall('\d+',line)))
            x.append((L[0],L[1]))
            count += 1
    return n, count

n,x = read_in(open('rosalind_tree.txt','r'))
print(n-x-1) #<-- SOLUTION

##Make Tree (Don't need this part for solution)
#generate dict with nodes to represent graph
graph = {}
for i in range(1,n+1):
    graph[i] = []
    
for tup in edges:
    graph[tup[0]].append(tup[1])
    graph[tup[1]].append(tup[0])
print(graph)
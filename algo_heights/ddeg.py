"""
Double-Degree Array
"""

def main(n, m, edges):
    adj_list = form_adjacency_list(n, edges)
    results = []  #initialize
    for node in sorted(adj_list):
        #sum all neighbors of that node and add to results
        neighbors = adj_list[node]
        results.append(sum([len(adj_list[nn])
                            for nn in neighbors]))
    print(' '.join(map(str,results)))

def form_adjacency_list(n, edges):
    adj_list = dict((x, []) for x in range(1,n+1))  #initialize
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    return adj_list


if __name__ == "__main__":
    import sys
    #read data in from file
    with open(sys.argv[1]) as f:
        n, m = map(int, f.readline().strip().split())
        edges = [tuple(map(int,line.strip().split())) for line in f.readlines()]
    #call main
    main(n, m, edges)

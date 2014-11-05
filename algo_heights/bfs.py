"""
Breadth-First Search
"""

def main(n, m, edges):
    graph = form_graph(n, edges)
    result = []
    for node in graph:
        result.append(find_shortest_path(graph,1,node))
    print(' '.join(map(str,result)))

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return len(path)
    if start not in graph:
        return None
    shortest = path
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return len(shortest)

def form_graph(n, edges):
    #initialize the graph
    graph = dict((i, []) for i in range(1, n+1))
    #populate it
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return graph

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        n, m = map(int, f.readline().strip().split())
        edges = [tuple(map(int, line.strip().split()))
                 for line in f.readlines()]
    main(n, m, edges)

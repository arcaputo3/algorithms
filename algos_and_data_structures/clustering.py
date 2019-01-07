""" Clustering using Greedy Algorithms. """
import networkx as nx
#from networkx.utils.union_find import UnionFind

def get_graph(filename):
    G = nx.Graph()
    X = nx.utils.union_find.UnionFind()
    edges = []
    with open("C:/Users/rcapu/algorithms/algos_and_data_structures/{}".format(filename)) as file:
        for line in file.readlines():
            line = tuple(int(x) for x in line.split(" "))
            X[line[0]]
            X[line[1]]
            edges.append(line)
    G.add_weighted_edges_from(edges)
    return G, X

def get_clusters(filename, k=4):
    G, X = get_graph(filename)
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    for i, edge in enumerate(edges):
        X.union(edge[0], edge[1])
        if len(X.parents.values()) == k:
            break

    for edge in edges:
        x, y = X.parents[edge[0]], X.parents[edge[1]]
        #print(x, y, edge)
        if x != y:
            return edge[-1]

print(get_clusters("clustering_small.txt"))

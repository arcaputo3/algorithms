# Compute a*b in O(log(n)) time where a = n
def rec_russian(a,b):
    if a == 0:
        return 0
    if a % 2 == 0: return 2*rec_russian(a/2,b)
    return b + 2*rec_russian((a-1)/2,b)

print(rec_russian(100123,2**24))
print(100123*(2**24))

def clique(n):
    print("in a clique...")
    for j in range(n):
        for i in range(j):
            print(i, "is friends with", j)

print(clique(4))

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def next_node(edge, current):
    return edge[0] if current == edge[1] else edge[1]

def remove_edge(raw_list, discard):
    return [item for item in raw_list if item != discard]

def find_eulerian_tour(graph):
    search = [[[], graph[0][0], graph]]
    while search:
        path, node, unexplore = search.pop()
        path += [node]

        if not unexplore:
            return path

        for edge in unexplore:
            if node in edge:
                search += [[path, next_node(edge, node), remove_edge(unexplore, edge)]]

print(find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))

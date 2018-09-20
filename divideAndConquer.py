# REC_RUSSIAN:  Compute a*b in O(log(n)) time where a = n
# Input:        integers a, b
# Output:       integer a*b 
def rec_russian(a,b):
    if a == 0:
        return 0
    if a % 2 == 0: return 2*rec_russian(a/2,b)
    return b + 2*rec_russian((a-1)/2,b)

# Example and comparison against built-in *
print(rec_russian(100123,2**24))
print(100123*(2**24))

# find_eulerian_tour: Finds a Eulerian Tour in a graph (each node traversed exactly once, starting and ending at same node)
# Original Publisher: Wentao - StackOverflow Jul 15 '16 at 23:56
# Input:        A graph represented as a list of tuples (edged between nodes)
# Output:       A list of nodes that represent a Eulerian Tour

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

# Example:
print(find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))

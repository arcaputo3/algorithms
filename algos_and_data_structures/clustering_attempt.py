class Node:
	def __init__(self):
		self.parent = None

class UnionFind(object):

	def __init__(self):
		#To hold the clusters
		self.clusters = []

	#create a new set(cluster) with a node
	def makeSet(self, node):
		#set the nodes parent to the node itself
		node.parent = node
		#set initial rank of node to 0
		node.rank = 0
		#add the node to cluster list
		self.clusters.append(node)

	#union the nodeA and nodeB clusters
	def union(self, nodeA, nodeB):

		self.link(self.findSet(nodeA), self.findSet(nodeB))

	#link the nodeA to nodeB or vice versa based upon the rank(number of nodes in the cluster) of the cluster
	def link(self, nodeA, nodeB):

		if nodeA.rank > nodeB.rank:
			nodeB.parent = nodeA
			#remove the nodeB from the cluster list, since it is merged with nodeA
			self.clusters.remove(nodeB)
		else:
			nodeA.parent = nodeB
			#remove the nodeA from the cluster list, since it is merged with nodeB
			self.clusters.remove(nodeA)
			#increade the rank of the cluster after merging the cluster
			if nodeA.rank == nodeB.rank:
				nodeB.rank = nodeB.rank + 1
	#find set will path compress(makes the nodes in cluster points to single leader/parent)  and returns the leader/parent of the cluster
	def findSet(self, node):

		if node != node.parent:
			node.parent = self.findSet(node.parent)
		return node.parent

	#get cluster size
	def clusterSize(self):
		return len(self.clusters)


def get_edges(filename):
	X = UnionFind()
	edges = []
	with open("C:/Users/rcapu/algorithms/algos_and_data_structures/{}".format(filename)) as file:
		for line in file.readlines():
			line = tuple(int(x) for x in line.split(" "))
			X.makeSet(Node(line[0]))
			X.makeSet(Node(line[1]))
			edges.append(line)
	edges.sort(key=lambda x: x[-1])
	return X, edges


def get_clusters(filename, k=4):
    X, edges = get_edges(filename)
    for edge in edges:
        if len(X.clusters) == k:
            break
        X.union(edge[0], edge[1])

    for edge in edges:
        x, y = X.findSet(edge[0]), X.findSet(edge[1])
        #print(x, y, edge)
        if x != y:
            return edge[-1]

print(get_clusters("clustering1.txt"))

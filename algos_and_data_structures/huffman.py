""" Computing Huffman Codes. """
from collections import defaultdict


class Node:
    """ Data structure for building tree bottom up. """
    def __init__(self, val):
        self.val = val
        self.id = None
        self.left = None
        self.right = None


def get_weights(filename="huffman.txt"):
    """ Upload and sort weights."""
    weights = []
    with open("C:/Users/rcapu/algorithms/algos_and_data_structures/{}".format(filename)) as file:
        for i, line in enumerate(file.readlines()):
            node = Node(int(line))
            # Ensure unique ids for each node
            node.id = i
            weights.append(node)
    return sorted(weights, key=lambda n: n.val)


def reader(filename):
    with open("C:/Users/rcapu/algorithms/algos_and_data_structures/{}".format(filename)) as file:
        while True:
            # read next character
            char = file.read(1)
            # if not EOF, then at least 1 character was read, and
            # this is not empty
            if char:
                if char != '\n':
                    yield char
            else:
                return


def get_text_freq(filename="macbeth.txt"):
    freq = defaultdict(int)
    r = reader(filename)
    for c in iter(r):
        freq[c] += 1

    weights = []
    for key, val in freq.items():
        node = Node(val)
        node.id = key
        weights.append(node)
    return weights


def get_weights(filename="huffman.txt"):
    """ Upload and sort weights."""
    weights = []
    with open("C:/Users/rcapu/algorithms/algos_and_data_structures/{}".format(filename)) as file:
        for i, line in enumerate(file.readlines()):
            node = Node(int(line))
            # Ensure unique ids for each node
            node.id = i
            weights.append(node)
    return sorted(weights, key=lambda n: n.val)



def build_tree(weights):
    """ Build tree bottom up. """
    while len(weights) > 1:
        # Combine least weighted nodes
        tree = Node(weights[0].val + weights[1].val)
        # Assign children accordingly
        tree.right = weights[0]
        tree.left = weights[1]
        # Merge values in weights array
        weights.pop(0)
        weights[0] = tree
        # Keep invariant that
        weights.sort(key=lambda n: n.val)
    return weights[0]


def get_codes(tree):
    """ Traverses tree top down to get codes. """
    codes = {}
    def encode(node, pat=''):
        if not node.left and not node.right:
            codes[node.id] = pat
        else:
            encode(node.left, pat+"0")
            encode(node.right, pat+"1")
        return codes
    return encode(tree)


if __name__ == "__main__":
    weights         = get_text_freq()
    tree            = build_tree(weights)
    code_dict       = get_codes(tree)
    vals            = list(code_dict.values())
    print(code_dict)

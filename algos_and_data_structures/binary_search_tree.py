# Binary search tree data structure implemented as python class

class Node:
    # Tree node: left and right child + value of node
    def __init__(self, val):
        # Node constructor
        # Left and right children
        self.left = None
        self.right = None
        # Value of node
        self.value = val
        # Size, useful for finding number of nodes <= t for some t
        self.size = 1


    def insert(self, val):
        # Check if we have an assigned value
        # Keep only unique values
        if self.value == val:
            return
        if self.value:
            self.size += 1
            # If value to insert is less than current node,
            # traverse left
            if val < self.value:
                # If node has no left child, set val = left child
                if self.left is None:
                    self.left = Node(val)
                # Else, insert recursively from left node
                else:
                    self.left.insert(val)
            # Similar for right node
            elif val > self.value:
                    if self.right is None:
                        self.right = Node(val)
                    else:
                        self.right.insert(val)
        else:
            self.value = val


    def lookup(self, val, parent=None):
        # Get the parent and node of a given value
        # If val is less than self value, traverse left
        if val < self.value:
            # Check if we have left child: if not, return None
            if self.left is None:
                return None, None
            # Traverse left
            # Set parent equal to current node
            return self.left.lookup(val, self)
        # If val is greater than self value, traverse left
        elif val > self.value:
            # Check if we have right child: if not, return None
            if self.right is None:
                return None, None
            # Traverse right
            # Set parent equal to current node
            return self.right.lookup(val, self)
        # If value is equal to current node, we are done
        # Return current node and its parent
        return self, parent


    def children_count(self):
        # Returns number of children of node
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


    def delete(self, val):
        # Lookup val for node and parent
        node, parent = self.lookup(val)

        # If node exists, we need to delete
        if node is not None:
            if parent:
                parent.size -= 1
            # Get number of children
            children_count = node.children_count()
            # If node has no children, we can easily remove
            if children_count == 0:
                # If node has a parent, set appropriate child to None
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.value = None
            # If node has one child, make child parent and delete node
            elif children_count == 1:
                # Check whether child is left or right
                if node.left:
                    n = node.left
                else:
                    n = node.right
                # If parent exists, we need to swap parents child with new child
                if parent:
                    # Check whether node is left or right child of parent
                    # Set child equal to n as appropriate
                    if parent.left is Node:
                        parent.left = n
                    else:
                        parent.right = n
                    # Delte node from tree
                    del node
                # If node has no parent (i.e. top of tree)
                else:
                    self.left = n.left
                    self.right = n.right
                    self.value = n.value
            # If we have two children, find successor
            else:
                parent = node
                successor = node.right
                # Traverse all the way left from node's right child
                while successor:
                    parent = successor
                    successor = successor.left
                # Replace current node value with successor value
                node.value = successor.value
                # Point to new value
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right


    def tree_data(self):
        # Generator to get all the values of our tree
        stack = []
        node = self
        # Loop while we have nodes left
        while node or stack:
            # If node is non-empty, add to stack
            if node:
                stack.append(node)
                node = node.left
            # Otherwise, we generate node value
            else:
                node = stack.pop()
                yield node.value
                node = node.right


    def get_max(self):
        # Returns node with max value
        node = self
        # Simply traverse all the way right
        while node.right:
            node = node.right
        return node


    def get_min(self):
        # Returns node with min value
        node = self
        # Traverse all the way left
        while node.left:
            node = node.left
        return node


    def rank(self, t):
        # Return the number of nodes with value <= t in the subtree rooted at this node.
        # Get appropriate size of left subtree
        left_size = 0 if self.left is None else self.left.size
        # Check if t is equal
        if t == self.value:
            # Return size of left tree including current node
            return left_size + 1
        # Check if t is less than current value
        elif t < self.value:
            # If t is too low, no nodes have value less than t
            if self.left is None:
                return 0
            # Else recurse down left subtree
            else:
                return self.left.rank(t)
        # Otherwise, t > current value
        else:
            # If no right child, return left_size including current node
            if self.right is None:
                return left_size + 1
            # Else recurse down right subtree, adding left_size including current node
            else:
                return self.right.rank(t) + left_size + 1


    def rotate(self, kind='left'):
        if kind == 'left':
            y, x = self.lookup(self.right.value)
            if y:
                if y.left:
                    x.right = y.left
                    y.left = x
                else:
                    y.left = x
        elif kind == 'right':
            x, y = self.lookup(self.left.value)
            if x:
                if x.right:
                    y.left = x.right
                    x.right = y
                else:
                    x.right = y


# Testing
# Implementation depends on node and root of node
root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(14)
for val in root.tree_data():
    print(val)

print(root.get_max().value)
print(root.get_min().value)
print(root.rank(11))

# File for linked lists
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

# setup some nodes and connect them to each other
# the linked list looks like:
# (head) n5 -> n4 -> n3 -> n2 -> n1 -> None
n1 = Node("Hello", None)
n2 = Node("21", n1)
n3 = Node("Green", n2)
n4 = Node("Blue", n3)
n5 = Node("Daniel", n4)

# assign a node to the head which functions
# as the entry into our linked list
head = n5

# setup pointers to both start
# at the head of the linked list
fastPointer = head
slowPointer = head

# loop through the linked list
# when fastPointer reaches the end of the list
# then slowPointer will be at the middle node
while fastPointer.next != None and fastPointer.next.next != None:
  fastPointer = fastPointer.next.next
  slowPointer = slowPointer.next

# slowPointer is now at the middle node in the linked list
print(slowPointer.data)


# Now, let's implement a doubly linked list
# Note that we default to a single linked list
class Dnode(Node):
    def __init__(self, data, next, prev = None):
        Node.__init__(self, data, next)
        self.prev = prev

# setup some nodes
# a doubly linked list looks as follows:
# (head) n5 <-> n4 <-> n3 <-> n2 <-> n1 (tail)
n5 = Dnode(5, n4, None)
n4 = Dnode(4, n3, n5)
n3 = Dnode(3, n2, n4)
n2 = Dnode(2, n1, n3)
n1 = Dnode(1, None, n2)

head = n5
tail = n1

# Now let's implement the same algorithm, but starting at the tail.
fastPointer = slowPointer = tail

# loop through the linked list
# when fastPointer reaches the end of the list
# then slowPointer will be at the middle node
while fastPointer.prev != None and fastPointer.prev.prev != None:
  fastPointer = fastPointer.prev.prev
  slowPointer = slowPointer.prev

print(slowPointer.data)

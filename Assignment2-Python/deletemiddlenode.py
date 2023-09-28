#2.3 Delete Middle Node (p. 93)
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def delete_node(node):
    if node is None or node.next is None:
        return False  
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    return True  

def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Test Case
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# Linking the nodes
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print("Original Linked List:")
print_list(a)  # Output: a -> b -> c -> d -> e -> f -> None

# Deleting node 'c'
delete_node(c)

print("Linked List After Deletion:")
print_list(a)  # Output: a -> b -> d -> e -> f -> None

#Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
#the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
#that node.
#EXAMPLE
#Input: the node c from the linked list a - >b- >c - >d - >e- >f
#Result: nothing is returned, but the new linked list looks like a - > b - > d - > e - > f
#Hints: #72
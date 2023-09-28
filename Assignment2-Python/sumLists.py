#2.5 Sum Lists (p. 95)

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

def sum_lists_reverse(l1, l2):
    carry = 0
    dummy_head = Node()
    current = dummy_head

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.data
            l1 = l1.next
        if l2:
            total += l2.data
            l2 = l2.next
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next

    return dummy_head.next

def get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length

def pad_list(node, padding):
    head = node
    for _ in range(padding):
        new_node = Node(0)
        new_node.next = head
        head = new_node
    return head

def sum_helper(l1, l2):
    if not l1 and not l2:
        return 0, None

    carry, next_node = sum_helper(l1.next, l2.next)
    total = l1.data + l2.data + carry
    current = Node(total % 10)
    current.next = next_node
    return total // 10, current

def sum_lists_forward(l1, l2):
    len1, len2 = get_length(l1), get_length(l2)
    
    if len1 < len2:
        l1 = pad_list(l1, len2 - len1)
    else:
        l2 = pad_list(l2, len1 - len2)

    carry, result = sum_helper(l1, l2)
    
    if carry:
        return Node(carry, result)
    return result


l1_forward = Node(6, Node(1, Node(7)))  # Represents 617 in forward order
l2_forward = Node(2, Node(9, Node(5)))  # Represents 295 in forward order

# For forward order
result_forward = sum_lists_forward(l1_forward, l2_forward)
print_list(result_forward)  # Output should be 9 -> 1 -> 2 -> None


'''Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: ( 7 - > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295,
Output:9 -> 1 -> 2,Thatis,912.
Hints: #7, #30, #71 #95, #109'''
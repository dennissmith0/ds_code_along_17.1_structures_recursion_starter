class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# def search(head, value):
#     current = head
#     while(current is not None):
#         if(current.value == value):
#             return True
#         current = current.next
#     return False

def search(head, value):
    if head is None:
        return False
    if head.value == value:
        return True
    return search(head.next, value)


# This function searches a linked list built from the provided listNode class, returning True if an element is found in the linked list. It returns False otherwise.

# Convert it to a recursive solution, i.e., the search function must call itself instead of using a loop.

# Hint: what is the base case?
    # Found the value or reached the end of the list

# Test cases:
head = listNode(3)
head.next = listNode(6)
head.next.next = listNode(9)
# The linked list is 3 -> 6 -> 9 (3 is the head of the list)

print(search(head, 3)) # True
print(search(head, 0)) # False
print(search(head, 9)) # True

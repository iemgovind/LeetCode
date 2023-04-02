# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Create a dummy node to point to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers, one to traverse the list
        # and the other to keep track of the previous node
        prev = dummy
        current = head
        
        # Traverse the list
        while current:
            # If the current node's value matches the given value,
            # delete the current node by skipping it
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            
            # Move to the next node
            current = current.next
        
        # Return the head of the updated list
        return dummy.next

# Create a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

# Remove all nodes with value 6
solution = Solution()
new_head = solution.removeElements(head, 6)

# Print the updated linked list
current_node = new_head
while current_node:
    print(current_node.val, end=' ')
    current_node = current_node.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize three pointers, one to the previous node,
        # one to the current node, and one to the next node
        prev = None
        current = head
        next_node = None
        
        # Traverse the list and reverse the links
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Return the new head of the reversed list
        return prev


# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the linked list
solution = Solution()
new_head = solution.reverseList(head)

# Print the reversed linked list
current_node = new_head
while current_node:
    print(current_node.val, end=' ')
    current_node = current_node.next

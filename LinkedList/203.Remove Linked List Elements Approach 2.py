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

        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next

# Create a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(6)
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

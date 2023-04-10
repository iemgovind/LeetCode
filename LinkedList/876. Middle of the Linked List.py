class Solution:
    def middleNode(self, head):
        slow, fast = head, head
        
        # Move the fast pointer two nodes ahead of the slow pointer at each step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the input linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create an instance of the Solution class
sol = Solution()

# Call the middleNode() method on the input linked list
middle_node = sol.middleNode(head)

# Print the value of the middle node
print(middle_node.val)  # Output: 3

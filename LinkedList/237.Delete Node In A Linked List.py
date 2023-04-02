#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Since we are not given the head of the linked list,
        # we can't traverse the list to find the previous node.
        # Instead, we copy the value of the next node into the
        # current node and delete the next node.
        
        # Copy the value of the next node into the current node
        node.val = node.next.val
        
        # Delete the next node
        node.next = node.next.next

# Test case
# Create a linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

# Delete node with value 5
node_to_delete = head.next
solution = Solution()
solution.deleteNode(node_to_delete)

# Print the updated linked list
current_node = head
while current_node:
    print(current_node.val, end=' ')
    current_node = current_node.next

"""The idea behind this solution is to copy the value of the next node into the current node and then delete the next node. Since we are not given the head of the linked list, we cannot traverse the list to find the previous node. Therefore, we have to use this approach to delete the given node.

The function takes in a single argument, node, which is the node that needs to be deleted. The function modifies the linked list in-place and does not return anything."""
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balanced(node):
            if not node:
                return 0
            left_height = check_balanced(node.left)
            if left_height == -1:
                return -1
            right_height = check_balanced(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return check_balanced(root) != -1

my_sol = Solution()
# Test case 1
# Expected output: True
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(my_sol.isBalanced(root1))

# Test case 2
# Expected output: True
root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))
print(my_sol.isBalanced(root2))

# Test case 3
# Expected output: True
root3 = None
print(my_sol.isBalanced(root3))

# Test case 4
# Expected output: True
root4 = TreeNode(1)
print(my_sol.isBalanced(root4))


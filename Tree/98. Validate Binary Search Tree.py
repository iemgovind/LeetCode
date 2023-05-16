# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return isBST(node.left, min_val, node.val) and isBST(node.right, node.val, max_val)
        
        return isBST(root, float('-inf'), float('inf'))

# Create a binary tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Create an instance of the Solution class
solution = Solution()

# Call the isValidBST function and print the result
print(solution.isValidBST(root))  # Output: True

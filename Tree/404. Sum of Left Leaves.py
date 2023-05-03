# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def traverse(node, is_left):
            if not node.left and not node.right: # leaf node
                if is_left:
                    return node.val
                else:
                    return 0
            left_sum = traverse(node.left, True) if node.left else 0
            right_sum = traverse(node.right, False) if node.right else 0
            return left_sum + right_sum
        
        return traverse(root, False)

# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Compute the sum of all left leaves
sol = Solution()
print(sol.sumOfLeftLeaves(root)) # Output: 24

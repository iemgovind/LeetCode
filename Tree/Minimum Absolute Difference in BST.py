# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_diff = float('inf')
        self.prev_val = None
        
        def inorder_traversal(node: TreeNode):
            if node is None:
                return
            inorder_traversal(node.left)
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.min_diff

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
print(solution.getMinimumDifference(root))  # Output: 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if not root:
            return False
        
        # check if it is a leaf node and its value is equal to target sum
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        # traverse left and right subtrees
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

s = Solution()
assert s.hasPathSum(root, 22) == True
assert s.hasPathSum(root, 26) == True


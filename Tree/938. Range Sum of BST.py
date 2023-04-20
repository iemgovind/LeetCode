# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Helper function to perform inorder traversal and accumulate sum
        def inorderTraversal(node):
            if node is None:
                return 0
            # If node value is within the range, add it to the sum
            if low <= node.val <= high:
                return node.val + inorderTraversal(node.left) + inorderTraversal(node.right)
            # If node value is less than low, traverse only right subtree
            elif node.val < low:
                return inorderTraversal(node.right)
            # If node value is greater than high, traverse only left subtree
            else:
                return inorderTraversal(node.left)
        
        # Call the helper function starting from the root of the BST
        return inorderTraversal(root)


# Test case 1
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right.left = None
root1.right.right = TreeNode(18)
sol = Solution()
print(sol.rangeSumBST(root1, 7, 15)) # Output: 32

# Test case 2
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(18)
root2.left.left.left = TreeNode(1)
root2.left.left.right = None
root2.left.right.left = TreeNode(6)
sol = Solution()
print(sol.rangeSumBST(root2, 6, 10)) # Output: 23

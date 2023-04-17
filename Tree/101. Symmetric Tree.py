# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Define a helper function to check if two nodes are symmetric
        def isSymmetricNodes(left, right):
            # If both nodes are None, they are symmetric
            if left is None and right is None:
                return True
            # If only one node is None, they are not symmetric
            if left is None or right is None:
                return False
            # If the values of the nodes are not equal, they are not symmetric
            if left.val != right.val:
                return False
            # Recursively check the left and right subtrees
            return isSymmetricNodes(left.left, right.right) and isSymmetricNodes(left.right, right.left)
        
        # Call the helper function starting from the root of the binary tree
        return isSymmetricNodes(root, root)


# Test case 1
# Input: root = [1,2,2,3,4,4,3]
# Output: true
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)
sol = Solution()
print(sol.isSymmetric(root1)) # Output: True

# Test case 2
# Input: root = [1,2,2,null,3,null,3]
# Output: false
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)
print(sol.isSymmetric(root2)) # Output: False

# Test case 3
# Input: root = [1]
# Output: true
root3 = TreeNode(1)
print(sol.isSymmetric(root3)) # Output: True

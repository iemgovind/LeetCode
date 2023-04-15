# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        # Initialize an empty list to store the inorder traversal result
        inorder = []
        
        # Define a helper function to perform the inorder traversal recursively
        def traverse(node):
            if node is None:
                return
            # Traverse the left subtree
            traverse(node.left)
            # Append the current node's value to the inorder list
            inorder.append(node.val)
            # Traverse the right subtree
            traverse(node.right)
        
        # Call the helper function starting from the root of the binary tree
        traverse(root)
        
        # Return the inorder traversal result
        return inorder

# Test case 1
# Input: root = [1,null,2,3]
# Output: [1,3,2]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
sol = Solution()
print(sol.inorderTraversal(root1)) # Output: [1,3,2]

# Test case 2
# Input: root = []
# Output: []
root2 = None
print(sol.inorderTraversal(root2)) # Output: []

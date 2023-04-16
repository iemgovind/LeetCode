# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Initialize a variable to keep track of the maximum diameter
        self.max_diameter = 0
        
        # Define a helper function to calculate the height of a binary tree
        def height(node):
            if node is None:
                return 0
            # Calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the maximum diameter by comparing with the sum of heights of left and right subtrees
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        # Call the helper function starting from the root of the binary tree
        height(root)
        
        # Return the maximum diameter
        return self.max_diameter


# Test case 1
# Input: root = [1,2,3,4,5]
# Output: 3
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
sol = Solution()
print(sol.diameterOfBinaryTree(root1)) # Output: 3

# Test case 2
# Input: root = [1,2]
# Output: 1
root2 = TreeNode(1)
root2.left = TreeNode(2)
print(sol.diameterOfBinaryTree(root2)) # Output: 1

# Test case 3
# Input: root = []
# Output: 0
root3 = None
print(sol.diameterOfBinaryTree(root3)) # Output: 0

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invertTree(root):
    """
    Inverts a binary tree in-place using recursive approach
    """
    if root is None:
        return None
    
    # Swap left and right subtrees
    root.left, root.right = root.right, root.left
    
    # Recursively invert left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root


# Test case 1
# Input: 
#      1
#     / \
#    2   3
#   / \
#  4   5
# Output: 
#      1
#     / \
#    3   2
#       / \
#      5   4
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print("Original Binary Tree:")
# Print original binary tree
def print_tree(root):
    if root:
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

print_tree(root1)

# Invert binary tree
invertTree(root1)

print("\nInverted Binary Tree:")
# Print inverted binary tree
print_tree(root1)

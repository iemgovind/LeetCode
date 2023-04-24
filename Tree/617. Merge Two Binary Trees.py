from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Function to merge two binary trees
    def mergeTrees(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

# Function to print the tree in in-order traversal for testing
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val, end=" ")
        print_tree(root.right)

# Function to create a binary tree from a list representation
def create_tree(nodes):
    if not nodes:
        return None

    def build_tree(idx):
        if idx >= len(nodes) or nodes[idx] is None:
            return None

        node = TreeNode(nodes[idx])
        node.left = build_tree(2 * idx + 1)
        node.right = build_tree(2 * idx + 2)
        return node

    return build_tree(0)

# Test the mergeTrees() function
my_merge = Solution()
# Example 1
root1 = create_tree([1, 3, 2, 5])
root2 = create_tree([2, 1, 3, None, 4, None, 7])
merged = my_merge.mergeTrees(root1, root2)

# Diagram representation of input trees and expected output
# Input Tree 1:
#      1
#     / \
#    3   2
#   / \
#  5   None
#
# Input Tree 2:
#      2
#     / \
#    1   3
#   /   / \
# None 4   7
#
# Expected Merged Tree:
#      3
#     / \
#    4   5
#   / \   \
# None 4   7
print("Input Tree 1:")
print_tree(root1)
print("\nInput Tree 2:")
print_tree(root2)
print("\nExpected Merged Tree:")
print_tree(merged)
print("\n")

# Example 2
root1 = create_tree([1])
root2 = create_tree([2])
merged = my_merge.mergeTrees(root1, root2)

# Diagram representation of input trees and expected output
# Input Tree 1:
#      1
#
# Input Tree 2:
#      2
#
# Expected Merged Tree:
#      3
print("Input Tree 1:")
print_tree(root1)
print("\nInput Tree 2:")
print_tree(root2)
print("\nExpected Merged Tree:")
print_tree(merged)
print("\n")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: # If both nodes are None
            return True
        if not p or not q: # If one node is None and the other is not
            return False
        if p.val != q.val: # If the values of the nodes are not equal
            return False
        
        # Recursively check for left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Test case example
# Tree 1
#     1
#    / \
#   2   3
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Tree 2
#     1
#    / \
#   2   3
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# Create an instance of the Solution class
s = Solution()

# Test the isSameTree() function
assert s.isSameTree(tree1, tree2) == True, "Error: Test Case 1"

# Tree 3
#     1
#    / \
#   2   3
#  /
# 4
tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.right = TreeNode(3)
tree3.left.left = TreeNode(4)

# Tree 4
#     1
#    / \
#   2   3
tree4 = TreeNode(1)
tree4.left = TreeNode(2)
tree4.right = TreeNode(3)

# Test the isSameTree() function
assert s.isSameTree(tree3, tree4) == False, "Error: Test Case 2"

# Tree 5
#     1
#    / \
#   2   3
#       \
#        4
tree5 = TreeNode(1)
tree5.left = TreeNode(2)
tree5.right = TreeNode(3)
tree5.right.right = TreeNode(4)

# Tree 6
#     1
#    / \
#   2   3
#  /
# 4
tree6 = TreeNode(1)
tree6.left = TreeNode(2)
tree6.right = TreeNode(3)
tree6.left.left = TreeNode(4)

# Test the isSameTree() function
assert s.isSameTree(tree5, tree6) == False, "Error: Test Case 3"

# Test case with None
assert s.isSameTree(None, None) == True, "Error: Test Case 4"
assert s.isSameTree(tree1, None) == False, "Error: Test Case 5"
assert s.isSameTree(None, tree2) == False, "Error: Test Case 6"

print("All test cases pass.")

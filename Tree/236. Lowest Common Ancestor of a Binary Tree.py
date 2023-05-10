# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        if left_lca and right_lca:
            return root
        else:
            return left_lca or right_lca

# Test case 1
# Tree:
#        3
#       / \
#      5   1
#     / \   \
#    6   2   8
#       / \
#      7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
p = root.left  # 5
q = root.right.right  # 8
assert Solution().lowestCommonAncestor(root, p, q).val == 3

# Test case 2
# Tree:
#        1
#       / \
#      2   3
#     / \     
#    4   5   
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
p = root.left.left  # 4
q = root.right  # 3
assert Solution().lowestCommonAncestor(root, p, q).val == 1

# Test case 3
# Tree:
#        1
#       / \
#      2   3
#     / \     
#    4   5   
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
p = root.left.right  # 5
q = root.right  # 3
assert Solution().lowestCommonAncestor(root, p, q).val == 1

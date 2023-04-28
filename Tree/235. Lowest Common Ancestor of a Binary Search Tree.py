# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

my_LCA = Solution()
# Test case 1
# Expected output: 6
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(8)
print(my_LCA.lowestCommonAncestor(root, p, q).val)

# Test case 2
# Expected output: 2
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(4)
print(my_LCA.lowestCommonAncestor(root, p, q).val)

# Test case 3
# Expected output: 6
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(6)
q = TreeNode(5)
print(my_LCA.lowestCommonAncestor(root, p, q).val)

# Test case 4
# Expected output: 2
root = TreeNode(2)
root.left = TreeNode(1)
p = TreeNode(2)
q = TreeNode(1)
print(my_LCA.lowestCommonAncestor(root, p, q).val)

# Test case 5
# Expected output: 1
root = TreeNode(1)
root.right = TreeNode(2)
p = TreeNode(1)
q = TreeNode(2)
print(my_LCA.lowestCommonAncestor(root, p, q).val)

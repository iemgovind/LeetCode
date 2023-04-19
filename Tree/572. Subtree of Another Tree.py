# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Define a helper function to check if two trees are identical
        def isIdentical(s, t):
            # If both nodes are None, they are identical
            if s is None and t is None:
                return True
            # If only one node is None, they are not identical
            if s is None or t is None:
                return False
            # If the values of the nodes are not equal, they are not identical
            if s.val != t.val:
                return False
            # Recursively check the left and right subtrees
            return isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
        
        # Define a helper function to traverse the tree and check for identical subtree
        def traverseTree(root, subRoot):
            # If root is None, there is no subtree
            if root is None:
                return False
            # If root is identical to subRoot, then subRoot is a subtree of root
            if isIdentical(root, subRoot):
                return True
            # Recursively check the left and right subtrees of root
            return traverseTree(root.left, subRoot) or traverseTree(root.right, subRoot)
        
        # Call the helper function starting from the root of root tree
        return traverseTree(root, subRoot)


# Test case 1
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
root1 = TreeNode(3)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)
subRoot1 = TreeNode(4)
subRoot1.left = TreeNode(1)
subRoot1.right = TreeNode(2)
sol = Solution()
print(sol.isSubtree(root1, subRoot1)) # Output: True

# Test case 2
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
root2.left.right.left = TreeNode(0)
subRoot2 = TreeNode(4)
subRoot2.left = TreeNode(1)
subRoot2.right = TreeNode(2)
sol = Solution()
print(sol.isSubtree(root2, subRoot2)) # Output: False

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            cnt = 0
            if node.val >= max_val:
                cnt = 1
                max_val = node.val
            cnt += dfs(node.left, max_val)
            cnt += dfs(node.right, max_val)
            return cnt
        
        return dfs(root, float('-inf'))

my_sol = Solution()
# Test case 1
#        3
#       / \
#      1   4
#     / \   \
#    3   1   5
root = TreeNode(3, TreeNode(1, TreeNode(3), TreeNode(1)), TreeNode(4, right=TreeNode(5)))
assert my_sol.goodNodes(root) == 4

# Test case 2
#        10
#       / \
#      5  15
#     / \   \
#    1   8   7
#root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(15, right=TreeNode(7)))
#assert my_sol.goodNodes(root) == 3

# Test case 3
#   2
#    \
#     4
#    / \
#   10  8
#root = TreeNode(2, right=TreeNode(4, TreeNode(10), TreeNode(8)))
#assert my_sol.goodNodes(root) == 2

# Test case 4
#   1
#    \
#     2
#    / \
#   3  -5
#root = TreeNode(1, right=TreeNode(2, TreeNode(3), TreeNode(-5)))
#assert my_sol.goodNodes(root) == 3

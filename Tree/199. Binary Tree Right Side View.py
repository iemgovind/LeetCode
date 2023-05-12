from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        last_nodes = {}
        while queue:
            node, level = queue.popleft()
            last_nodes[level] = node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
                
        return [last_nodes[level] for level in last_nodes]


# Example usage
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(Solution().rightSideView(root)) # Output: [1, 3, 4]


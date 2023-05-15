from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        queue = [(target, 0)]
        visited = set()
        result = []
        
        while queue:
            node, distance = queue.pop(0)
            visited.add(node)

            if distance == k:
                result.append(node.val)

            if distance > k:
                break

            if node.left and node.left not in visited:
                queue.append((node.left, distance + 1))
            if node.right and node.right not in visited:
                queue.append((node.right, distance + 1))
            if node.parent and node.parent not in visited:
                queue.append((node.parent, distance + 1))

        return result


# Example usage
root = TreeNode(3,
                TreeNode(5,
                         TreeNode(6),
                         TreeNode(2, TreeNode(7), TreeNode(4))),
                TreeNode(1, TreeNode(0), TreeNode(8)))

target = TreeNode(5)
k = 2

print(Solution().distanceK(root, target, k))  # Output: [7, 4, 1]

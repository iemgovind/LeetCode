from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    level = 0

    while queue:
        level_vals = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_vals.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level % 2 == 1:
            level_vals.reverse()

        result.append(level_vals)
        level += 1

    return result

# Testing the function
# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Perform zigzag level order traversal
result = zigzagLevelOrder(root)
print(result)

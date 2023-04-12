print("Solution Using Recursion")
### Using Recursion
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class to calculate the maximum depth of a binary tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: If root is None, return 0
        if root is None:
            return 0
        
        # Recursively calculate the maximum depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return the maximum depth among left and right subtrees, plus 1 for the root node
        return max(left_depth, right_depth) + 1


# Test cases
# Example 1
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

solution = Solution()
print("Example 1:")
print("Input: root = [3,9,20,null,null,15,7]")
print("Output:", solution.maxDepth(root1))

# Example 2
# Input: root = [1,null,2]
# Output: 2
root2 = TreeNode(1)
root2.right = TreeNode(2)

print("\nExample 2:")
print("Input: root = [1,null,2]")
print("Output:", solution.maxDepth(root2))

print('\n')
print("Solution Without Recursion")
## Without Using Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# Create a TreeNode class as per the definition given in the problem statement
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class to calculate the maximum depth of a binary tree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: If root is None, return 0
        if root is None:
            return 0
        
        # Use a queue to perform level-order traversal of the binary tree
        queue = deque([(root, 1)])  # tuple of (node, depth)
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)  # Update max depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth

# Test cases
# Example 1
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

solution = Solution()
print("Example 1:")
print("Input: root = [3,9,20,null,null,15,7]")
print("Output:", solution.maxDepth(root1))

# Example 2
# Input: root = [1,null,2]
# Output: 2
root2 = TreeNode(1)
root2.right = TreeNode(2)

print("\nExample 2:")
print("Input: root = [1,null,2]")
print("Output:", solution.maxDepth(root2))

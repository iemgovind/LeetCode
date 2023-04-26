# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        def dfs(node: TreeNode, path: str):
            # Base case: if node is None, return
            if not node:
                return
            
            # Add the current node's value to the path
            if not path:
                path += str(node.val)
            else:
                path += "->" + str(node.val)
            
            # If the current node is a leaf, add the path to the result list
            if not node.left and not node.right:
                result.append(path)
            
            # Recursively call dfs on the left and right child nodes
            dfs(node.left, path)
            dfs(node.right, path)
        
        # Initialize an empty list to store the result paths
        result = []
        
        # Call dfs on the root node with an empty path
        dfs(root, "")
        
        # Return the result list of root-to-leaf paths
        return result


# Test case 1: Example input
# Expected output: ['1->2->5', '1->3']
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)

solution = Solution()
result1 = solution.binaryTreePaths(root1)
print("Test Case 1 Output: ", result1)

# Test case 2: Empty tree
# Expected output: []
root2 = None

result2 = solution.binaryTreePaths(root2)
print("Test Case 2 Output: ", result2)

# Test case 3: Tree with only root node
# Expected output: ['1']
root3 = TreeNode(1)

result3 = solution.binaryTreePaths(root3)
print("Test Case 3 Output: ", result3)

# Test case 4: Tree with only left child nodes
# Expected output: ['1->2->4', '1->2->5', '1->3']
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.left.left = TreeNode(4)
root4.left.right = TreeNode(5)

result4 = solution.binaryTreePaths(root4)
print("Test Case 4 Output: ", result4)

# Test case 5: Tree with only right child nodes
# Expected output: ['1->3->6', '1->3->7']
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(3)
root5.right.left = TreeNode(6)
root5.right.right = TreeNode(7)

result5 = solution.binaryTreePaths(root5)
print("Test Case 5 Output: ", result5)

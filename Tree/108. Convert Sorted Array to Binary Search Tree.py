# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        # Helper function to construct a balanced BST from a sorted array
        def constructBST(left, right):
            if left > right:
                return None
            # Find the middle element of the current subarray
            mid = left + (right - left) // 2
            # Create a new TreeNode with the middle element as the value
            root = TreeNode(nums[mid])
            # Recursively construct the left and right subtrees
            root.left = constructBST(left, mid - 1)
            root.right = constructBST(mid + 1, right)
            return root
        
        # Call the helper function starting from the entire array
        return constructBST(0, len(nums) - 1)


def print_tree(root):
    """
    Print the binary tree structure in a visual format.
    """
    if not root:
        return "[]"

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    # Remove trailing null values
    while result[-1] == "null":
        result.pop()

    return "[" + ",".join(result) + "]"


# Test case 1
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
sol = Solution()
nums1 = [-10, -3, 0, 5, 9]
root1 = sol.sortedArrayToBST(nums1)
print(print_tree(root1))  # Output: [0,-3,9,-10,null,5]

# Test case 2
# Input: nums = [1,3]
# Output: [3,1]
sol = Solution()
nums2 = [1, 3]
root2 = sol.sortedArrayToBST(nums2)
print(print_tree(root2))  # Output: [3,1]

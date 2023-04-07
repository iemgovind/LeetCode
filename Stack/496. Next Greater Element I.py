class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # Create a dictionary to store the next greater element for each element in nums2
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        # If an element in nums1 is in next_greater, use its corresponding value as the result
        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))
        return result
# Instantiate the Solution class
sol = Solution()

# Define the input lists
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

# Call the nextGreaterElement method and print the result
result = sol.nextGreaterElement(nums1, nums2)
print(result) #Output [ -1, 3, -1]



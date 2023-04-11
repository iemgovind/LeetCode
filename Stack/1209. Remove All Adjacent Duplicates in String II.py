class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            # If the stack is not empty and the current character is equal to the top of the stack
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                # If the count of the current character is equal to k, pop k elements from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Append the current character with count 1 to the stack
                stack.append([char, 1])

        # Construct the final string from the characters left in the stack
        result = ''
        for char, count in stack:
            result += char * count

        return result

sol = Solution()

# Test case 1
s1 = "abcd"
k1 = 2
output1 = sol.removeDuplicates(s1, k1)
expected_output1 = "abcd"
print("Input: s = {}, k = {}".format(s1, k1))
print("Output: {}".format(output1))
print("Expected Output: {}".format(expected_output1))
print()

# Test case 2
s2 = "deeedbbcccbdaa"
k2 = 3
output2 = sol.removeDuplicates(s2, k2)
expected_output2 = "aa"
print("Input: s = {}, k = {}".format(s2, k2))
print("Output: {}".format(output2))
print("Expected Output: {}".format(expected_output2))
print()

# Test case 3
s3 = "pbbcggttciiippooaais"
k3 = 2
output3 = sol.removeDuplicates(s3, k3)
expected_output3 = "ps"
print("Input: s = {}, k = {}".format(s3, k3))
print("Output: {}".format(output3))
print("Expected Output: {}".format(expected_output3))
print()

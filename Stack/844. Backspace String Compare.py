class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for char in s:
            if char == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)
        
        for char in t:
            if char == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)
        
        return stack_s == stack_t


# Instantiate the Solution class
sol = Solution()

# Define the input strings
s = "ab#c"
t = "ad#c"

# Call the backspaceCompare method and print the result
result = sol.backspaceCompare(s, t)
print(result)

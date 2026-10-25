# 394. Decode String
# Problem: https://leetcode.com/problems/decode-string/
# Submitted: 2026-10-25 12:55 EDT
# Intuition: Each bracketed section needs its own string and repeat count, so nested sections fit a stack.
# Approach: Save the prefix and count on opening brackets; on closing brackets, repeat and combine the section.
# Complexity: O(n*L) worst-case time from repeated string copies, O(n + L) space; L is decoded length.

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        curr_str = ""
        curr_count = ""

        for char in s:
            
            # digit so append to curr_count
            if char.isdigit():
                curr_count += char
            
            # opening bracket so push to stack and reset curr
            elif char == "[":
                stack.append((curr_str, int(curr_count)))
                curr_str = ""
                curr_count = ""
            
            # closing bracket so pop, repeat stack count times and prepend stack str
            elif char == "]":
                prev_str, repeat = stack.pop()
                curr_str = prev_str + (curr_str * repeat)
            
            # alpha char so just append to curr
            else:
                curr_str += char
        
        return curr_str


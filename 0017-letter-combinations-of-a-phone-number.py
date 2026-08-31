# 17. Letter Combinations of a Phone Number
# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Submitted: 2026-08-31 16:45 EDT
# Intuition: Each digit contributes one character from its keypad letters.
# Approach: Backtrack through the mapped letters and join the path at each complete combination.
# Complexity: O(n*4^n) worst-case time and output space; O(n) auxiliary space.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = [
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]
        answer = []

        def explore(i, current):

            if i == len(digits):
                answer.append("".join(current))
                return
            
            options = mapping[int(digits[i])]
            
            for char in options:
                current.append(char)
                explore(i+1, current)
                current.pop()
                
        explore(0,[])

        return answer

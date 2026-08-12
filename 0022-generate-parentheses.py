# 22. Generate Parentheses
# Problem: https://leetcode.com/problems/generate-parentheses/
# Submitted: 2026-08-12 14:09 EDT
# Intuition: A valid prefix never closes more brackets than it has opened.
# Approach: Backtrack with remaining open/close counts, adding only legal next brackets.
# Complexity: O(n*C_n) time and output space; O(n) auxiliary space, C_n is the nth Catalan number.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [];
        curr = [];
        
        def backtrack(open_count, close_count):
            # all open and closed used, so add valid
            if open_count == 0 and close_count == 0:
                result.append("".join(curr));
                return;
            # add open
            if open_count > 0:
                curr.append("(");
                backtrack(open_count - 1, close_count);
                curr.pop();
            # add close
            if close_count > open_count:
                curr.append(")");
                backtrack(open_count, close_count - 1);
                curr.pop();

        backtrack(n, n);

        return result;


            
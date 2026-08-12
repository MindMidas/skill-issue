# 150. Evaluate Reverse Polish Notation
# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Submitted: 2026-08-12 13:52 EDT
# Intuition: Postfix operators consume the two most recent unfinished values.
# Approach: Push numbers and evaluate each operator with the top two stack entries.
# Complexity: O(n) time, O(n) space under bounded arithmetic.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ["+", "-", "*", "/"]
        stack = [];

        for token in tokens:
            
            if token in operators:

                b = stack.pop();
                a = stack.pop();
                match token:
                    case "+":
                        stack.append(a + b);
                    case "-":
                        stack.append(a - b);
                    case "*":
                        stack.append(a * b);
                    case "/":
                         stack.append(int(a / b));
                
                continue;

            stack.append(int(token));
        
        return stack.pop()
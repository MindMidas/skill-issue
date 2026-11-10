# 2303. Calculate Amount Paid in Taxes
# Problem: https://leetcode.com/problems/calculate-amount-paid-in-taxes/
# Submitted: 2026-11-09 19:41 EST
# Intuition: Each bracket taxes only the income between its lower and upper limits.
# Approach: Track the previous upper limit, add the tax on the portion of income in each bracket, and stop when the current bracket covers the remaining income.
# Complexity: O(b) time and O(1) extra space, where b is the number of brackets.

class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:

        owing = 0
        prev = 0

        for amount, rate in brackets:
            taxable = min(income,amount) - prev
            owing += taxable * rate / 100

            if income <= amount:
                break
            prev = amount

        return owing

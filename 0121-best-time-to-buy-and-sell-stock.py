# 121. Best Time to Buy and Sell Stock
# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Submitted: 2026-08-24 13:36 EDT
# Intuition: The best sale today uses the lowest price seen before it.
# Approach: Track the running minimum price and maximum achievable profit in one pass.
# Complexity: O(n) time, O(1) space.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        best = 0

        for price in prices:
            
            if price >= lowest:  
                best = max(best, price-lowest) 
            else:
                lowest = price
        
        return best                
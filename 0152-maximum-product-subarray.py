# 152. Maximum Product Subarray
# Problem: https://leetcode.com/problems/maximum-product-subarray/
# Submitted: 2026-11-04 13:51 EST
# Intuition: A negative number can turn the smallest product into the largest.
# Approach: At each number, start fresh or extend either extreme from the previous index.
# Complexity: O(n) time and O(n) extra space because nums[1:] makes a copy.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        # largest product of a subarray ending at prev index
        max_prod = nums[0]
        # smallest product of a subarray ending at the prev index
        min_prod = nums[0]
        # largest product found anywhere so far
        result = nums[0]

        for n in nums[1:]:

            # three possible choices
            a = n # start fresh
            b = n * max_prod # extend the previous maximum
            c = n * min_prod # extend the previous minimum

            # update max and min
            max_prod = max(a,b,c)
            min_prod = min(a,b,c)

            # check if we have a better result
            result = max(result, max_prod)

        return result

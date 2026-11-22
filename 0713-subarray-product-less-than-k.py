# 713. Subarray Product Less Than K
# Problem: https://leetcode.com/problems/subarray-product-less-than-k/
# Submitted: 2026-11-22 14:45 EST
# Intuition: Each valid window contributes all subarrays ending at its right edge.
# Approach: Multiply in the next value, shrink until the product is below k,
# then add the window length to the count.
# Complexity: O(n) time and O(1) extra space.


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        product = 1
        count = 0
        for right in range(len(nums)):
            product = product * nums[right]
            while product >= k and left <= right:
                product = product // nums[left]
                left += 1
            count += right - left + 1

        return count

# 238. Product of Array Except Self
# Problem: https://leetcode.com/problems/product-of-array-except-self/
# Submitted: 2026-08-11 17:38 EDT
# Intuition: Each answer is the product of values before it times the product after it.
# Approach: Write prefix products, then multiply by suffix products in a reverse pass.
# Complexity: O(n) time, O(1) auxiliary space plus O(n) output space.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)
        
        product = 1

        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]
        
        return answer
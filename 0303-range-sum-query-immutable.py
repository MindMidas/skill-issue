# 303. Range Sum Query - Immutable
# Problem: https://leetcode.com/problems/range-sum-query-immutable/
# Submitted: 2026-11-04 12:53 EST
# Intuition: The array stays fixed, so build the running sums once.
# Approach: Subtract the sum before left from the sum through right.
# Complexity: O(n) time to build, O(1) time per query, O(n) extra space.

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix_sum = []

        # build prefix sum list
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            self.prefix_sum.append(running_sum)

    def sumRange(self, left: int, right: int) -> int:

        # when left is 0, there is no earlier prefix to subtract
        if left == 0:
            return self.prefix_sum[right]

        return self.prefix_sum[right] - self.prefix_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

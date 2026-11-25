# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Problem: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Submitted: 2026-11-25 10:50 EST
# Intuition: A window qualifies when its maximum minus minimum is within the limit.
# Approach: Maintain increasing and decreasing deques for window extrema,
# shrinking from the left until the window becomes valid.
# Complexity: O(n) time and O(n) space.

from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        best = 0
        left = 0
        min_q = deque()
        max_q = deque()

        for right in range(len(nums)):
            num = nums[right]
            while min_q and num < min_q[-1]:
                min_q.pop()
            min_q.append(num)
            while max_q and num > max_q[-1]:
                max_q.pop()
            max_q.append(num)

            while max_q[0] - min_q[0] > limit:
                if nums[left] == min_q[0]:
                    min_q.popleft()
                if nums[left] == max_q[0]:
                    max_q.popleft()
                left += 1

            best = max(best, right - left + 1)

        return best

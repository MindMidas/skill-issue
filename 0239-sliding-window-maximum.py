# 239. Sliding Window Maximum
# Problem: https://leetcode.com/problems/sliding-window-maximum/
# Submitted: 2026-08-26 12:23 EDT
# Intuition: A smaller value behind a newer larger one can never become a window maximum.
# Approach: Maintain decreasing candidate indices in a deque and remove expired indices.
# Complexity: O(n) time, O(k) auxiliary space plus O(n-k+1) output space.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i, num in enumerate(nums):

            # candidate no longer in window
            if q and q[0] < i - k + 1:
                q.popleft()

            # loop and compare to curr max
            while q and num >= nums[q[-1]]:
                q.pop()
            
            # add curr
            q.append(i)

            # check is for 1st window, only add after 
            if i >= k - 1:
                result.append(nums[q[0]])
        
        return result

        
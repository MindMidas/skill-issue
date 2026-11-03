# 560. Subarray Sum Equals K
# Problem: https://leetcode.com/problems/subarray-sum-equals-k/
# Submitted: 2026-11-03 12:25 EST
# Note: Worked through this one with external help.
# Intuition: A subarray sums to k when the current prefix sum minus an earlier prefix sum equals k.
# Approach: Count earlier prefix sums in a dictionary; add the frequency of running_sum - k before storing the current sum.
# Complexity: O(n) expected time, O(n) extra space.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # count how often each earlier prefix sum appears
        running_sum = 0
        result = 0
        freq = {0:1} # empty prefix has sum 0

        for num in nums:

            # add curr num to running sum
            running_sum += num

            # current prefix - earlier prefix = k
            target = running_sum - k

            # if target exists, each occurrence gives a valid subarray
            if target in freq:
                result += freq[target]

            # store after counting, so we only use earlier prefixes
            freq[running_sum] = freq.get(running_sum, 0) + 1

        return result

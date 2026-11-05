# 1539. Kth Missing Positive Number
# Problem: https://leetcode.com/problems/kth-missing-positive-number/
# Submitted: 2026-11-05 15:27 EST
# Intuition: At index i, arr[i] - (i + 1) counts the missing positives so far.
# Approach: Binary search for the first index with at least k missing. Add that index to k to account for the numbers present before the answer.
# Complexity: O(log n) time and O(1) extra space.

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        left = 0
        right = len(arr)

        while left < right:

            mid = (left+right) // 2

            # subtract the number of positives present through mid
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid

        return left + k

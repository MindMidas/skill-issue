# 978. Longest Turbulent Subarray
# Problem: https://leetcode.com/problems/longest-turbulent-subarray/
# Submitted: 2026-11-26 13:38 EST
# Intuition: A turbulent window alternates its expected comparison at each step.
# Approach: Track the left boundary and expected comparison. Reset on equal
# values and restart from the previous element when the alternation breaks.
# Complexity: O(n) time and O(1) extra space.

import operator


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        left = 0
        sign = None
        best = 1

        for right in range(1, len(arr)):
            if sign is None:
                if arr[right - 1] < arr[right]:
                    sign = operator.gt
                    left = right - 1
                elif arr[right - 1] > arr[right]:
                    sign = operator.lt
                    left = right - 1
                else:
                    sign = None
                    left = right
            else:
                if arr[right - 1] == arr[right]:
                    left = right
                    sign = None
                elif not sign(arr[right - 1], arr[right]):
                    left = right - 1
                    if arr[right - 1] < arr[right]:
                        sign = operator.gt
                    else:
                        sign = operator.lt
                else:
                    sign = operator.gt if sign == operator.lt else operator.lt

            best = max(best, right - left + 1)

        return best

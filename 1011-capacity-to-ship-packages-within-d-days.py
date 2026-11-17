# 1011. Capacity To Ship Packages Within D Days
# Problem: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Submitted: 2026-11-17 11:53 EST
# Intuition: If a capacity can ship everything on time, any larger capacity can too.
# Approach: Binary search between the largest weight and the total weight,
# simulating the shipping days needed for each candidate capacity.
# Complexity: O(n log(S - M + 1)) time and O(1) extra space, where S is the
# total weight and M is the largest weight.


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def can_ship(capacity):
            used = 1
            curr = 0

            for w in weights:
                if (w + curr) <= capacity:
                    curr += w
                else:
                    curr = w
                    used += 1

                if used > days:
                    return False

            return True

        while left < right:
            mid = (left + right) // 2

            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left

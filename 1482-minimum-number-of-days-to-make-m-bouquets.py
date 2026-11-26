# 1482. Minimum Number of Days to Make m Bouquets
# Problem: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
# Submitted: 2026-11-26 12:37 EST
# Intuition: If enough bouquets can be made on a day, later days also work.
# Approach: Binary search the first feasible day, scanning for disjoint groups
# of k adjacent bloomed flowers for each candidate.
# Complexity: O(n log(D + 1)) time and O(1) extra space, where D is the
# difference between the latest and earliest bloom days.


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def canMakeBouquets(day):
            bouquets = 0
            consecutive = 0
            for d in bloomDay:
                if d > day:
                    consecutive = 0
                else:
                    consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            return bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1

        return left

# 47. Permutations II
# Problem: https://leetcode.com/problems/permutations-ii/
# Submitted: 2026-11-19 16:05 EST
# Intuition: Equal values must be chosen in a consistent order to avoid duplicate permutations.
# Approach: Sort the input and backtrack over unused indices, skipping a repeated
# value when its preceding equal value has not been used in the current path.
# Complexity: O(n * n!) worst-case time and O(n) auxiliary space, excluding output.


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        def dfs(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in used:
                    continue

                path.append(nums[i])
                used.add(i)
                dfs(path, used)
                path.pop()
                used.remove(i)

        dfs([], set())
        return ans

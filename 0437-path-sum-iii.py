# 437. Path Sum III
# Problem: https://leetcode.com/problems/path-sum-iii/
# Submitted: 2026-11-21 16:46 EST
# Intuition: Each node can be the start of a downward path with the target sum.
# Approach: Visit every possible starting node and recursively count matching
# path sums through its descendants.
# Complexity: O(n^2) worst-case time and O(h) recursion space for tree height h.

from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def countPaths(node, total):
            if not node:
                return 0

            total += node.val
            count = 1 if total == targetSum else 0
            count += countPaths(node.left, total)
            count += countPaths(node.right, total)
            return count

        def dfs(node):
            if not node:
                return 0

            count = countPaths(node, 0)
            count += dfs(node.left)
            count += dfs(node.right)
            return count

        return dfs(root)

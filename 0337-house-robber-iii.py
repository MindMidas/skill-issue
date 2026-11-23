# 337. House Robber III
# Problem: https://leetcode.com/problems/house-robber-iii/
# Submitted: 2026-11-23 11:26 EST
# Intuition: At each house, choose to rob or skip while respecting its parent's choice.
# Approach: Memoize DFS by node and whether robbing it is allowed. Robbing
# prevents robbing its children, while skipping allows both children to choose.
# Complexity: O(n) time and O(n) space.

from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: TreeNode | None) -> int:
        memo = {}

        def dfs(node, can_rob):
            if not node:
                return 0
            if (node, can_rob) in memo:
                return memo[(node, can_rob)]

            if not can_rob:
                result = dfs(node.left, True) + dfs(node.right, True)
            else:
                rob = node.val + dfs(node.left, False) + dfs(node.right, False)
                skip = dfs(node.left, True) + dfs(node.right, True)
                result = max(rob, skip)

            memo[(node, can_rob)] = result
            return result

        return dfs(root, True)

# 129. Sum Root to Leaf Numbers
# Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Submitted: 2026-11-25 13:23 EST
# Intuition: Each root-to-leaf path builds a number one digit at a time.
# Approach: Use BFS carrying the current number, extending it by multiplying
# by ten and adding the child digit. Sum the numbers at leaf nodes.
# Complexity: O(n) time and O(w) queue space for maximum tree width w.

from __future__ import annotations

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def join_nums(a, b):
            return a * 10 + b

        total = 0
        queue = deque([(root, root.val)])
        while queue:
            node, num = queue.popleft()
            if node.left is None and node.right is None:
                total += num
                continue

            if node.left:
                queue.append((node.left, join_nums(num, node.left.val)))
            if node.right:
                queue.append((node.right, join_nums(num, node.right.val)))

        return total

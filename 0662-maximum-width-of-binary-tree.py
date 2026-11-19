# 662. Maximum Width of Binary Tree
# Problem: https://leetcode.com/problems/maximum-width-of-binary-tree/
# Submitted: 2026-11-18 19:53 EST
# Intuition: Perfect-tree positions preserve the gaps between nodes at each level.
# Approach: Use BFS with positions 2*p and 2*p+1 for each node's children.
# At each level, measure the distance between the first and last positions.
# Complexity: O(n) node visits and O(w) queued entries for maximum level size w,
# treating position arithmetic as constant time. Python position integers can
# grow to O(h) bits at tree height h.

from __future__ import annotations

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0
        while queue:
            level = len(queue)
            leftmost = queue[0][1]
            rightmost = queue[-1][1]
            max_width = max(max_width, rightmost - leftmost + 1)

            for _ in range(level):
                node, position = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * position))
                if node.right:
                    queue.append((node.right, 2 * position + 1))

        return max_width

# 103. Binary Tree Zigzag Level Order Traversal
# Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Submitted: 2026-10-24 16:26 EDT
# Intuition: Zigzag traversal is normal level-order traversal with every other level reversed.
# Approach: BFS with a queue, collect each level left to right, and reverse odd-numbered levels.
# Complexity: O(n) time, O(n) space; reversing alternate levels still touches each value at most once.

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        if not root:
            return []

        queue = deque([root])

        result = []

        while queue:

            level = []

            for _ in range(len(queue)):

                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
            if len(result) % 2 == 1:
                level.reverse()

            result.append(level)
            
        return result
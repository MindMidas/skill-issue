# 102. Binary Tree Level Order Traversal
# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Submitted: 2026-08-29 14:07 EDT
# Intuition: Nodes reached at the same depth belong in the same output level.
# Approach: DFS left-to-right, creating a result list when first reaching each depth.
# Complexity: O(n) time, O(n) output space and O(h) auxiliary space.

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def explore(self, root: Optional[TreeNode], depth: int):

        if root is None:
            return
        if len(self.result) == depth:
            self.result.append([])
        self.result[depth].append(root.val)

        self.explore(root.left, depth + 1)
        self.explore(root.right, depth + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.result = []

        self.explore(root,0)

        return self.result
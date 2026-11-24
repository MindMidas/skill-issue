# 114. Flatten Binary Tree to Linked List
# Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Submitted: 2026-11-24 18:17 EST
# Intuition: Flattened left and right subtrees can be joined in preorder.
# Approach: Recursively obtain each subtree's tail, move the left subtree to
# the right, append the original right subtree, and return the final tail.
# Complexity: O(n) time and O(h) recursion space for tree height h.

from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """Modify root in place."""
        def dfs(node):
            if not node:
                return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            right_head = node.right
            if left_tail:
                left_tail.right = right_head
                node.right = node.left
                node.left = None
            return right_tail or left_tail or node

        dfs(root)

# 450. Delete Node in a BST
# Problem: https://leetcode.com/problems/delete-node-in-a-bst/
# Submitted: 2026-11-20 12:58 EST
# Intuition: A deleted node's right subtree can replace it, with the left
# subtree attached to the smallest node in that right subtree.
# Approach: Find the target and its parent using BST ordering, build the
# replacement subtree, and reconnect it to the parent or return the new root.
# Complexity: O(h) time and O(h) recursion space for tree height h.

from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def replaceNode(node):
            if not node.right:
                return node.left
            if not node.left:
                return node.right

            right = node.right
            while right.left:
                right = right.left
            right.left = node.left
            return node.right

        def findNode(node, parent=None):
            if not node:
                return None, None
            if node.val > key:
                return findNode(node.left, node)
            elif node.val < key:
                return findNode(node.right, node)
            else:
                return node, parent

        target, parent = findNode(root)
        if not target:
            return root

        replacement = replaceNode(target)
        if not parent:
            return replacement

        if parent.left == target:
            parent.left = replacement
        else:
            parent.right = replacement

        return root

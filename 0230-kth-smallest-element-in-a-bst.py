# 230. Kth Smallest Element in a BST
# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Submitted: 2026-08-30 11:58 EDT
# Intuition: Inorder traversal visits BST values in sorted order.
# Approach: Traverse inorder, decrement k, and save the value when the count reaches zero.
# Complexity: O(n) time, O(h) space; this version continues traversing after finding the answer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def explore(self, root: Optional[TreeNode]):

        if root is None:
            return
        
        self.explore(root.left)

        self.count -= 1

        if self.count == 0:
            self.answer = root.val

        self.explore(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.answer = None
        self.count = k

        self.explore(root)
        return self.answer
        
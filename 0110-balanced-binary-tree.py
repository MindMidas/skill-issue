# 110. Balanced Binary Tree
# Problem: https://leetcode.com/problems/balanced-binary-tree/
# Submitted: 2026-08-28 21:59 EDT
# Intuition: A tree is balanced only when every node's child heights differ by at most one.
# Approach: Compute heights bottom-up and record any imbalance during the same traversal.
# Complexity: O(n) time, O(h) space.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def explore(self, root: Option[TreeNode]) -> int:

        if root is None:
            return 0
        
        d_left = self.explore(root.left)
        d_right = self.explore(root.right)

        if abs(d_left - d_right) > 1:
            self.balanced = False
        
        return max(d_left, d_right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.explore(root)
        return self.balanced
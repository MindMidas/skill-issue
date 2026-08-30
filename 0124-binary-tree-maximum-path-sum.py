# 124. Binary Tree Maximum Path Sum
# Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Submitted: 2026-08-30 15:56 EDT
# Intuition: A path through a node can use both child gains, but a parent can use only one.
# Approach: DFS for each best downward gain while updating the best left-node-right total.
# Complexity: O(n) time, O(h) space; h is tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def explore(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        left = max(self.explore(root.left), 0)
        right = max(self.explore(root.right), 0)

        self.max_sum = max(
            self.max_sum,
            root.val + left + right
        )

        return root.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        self.explore(root)
        return self.max_sum
        
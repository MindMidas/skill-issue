# 98. Validate Binary Search Tree
# Problem: https://leetcode.com/problems/validate-binary-search-tree/
# Submitted: 2026-08-29 15:31 EDT
# Intuition: Each node must lie strictly inside bounds inherited from all its ancestors.
# Approach: DFS with narrowed lower and upper bounds for left and right subtrees.
# Complexity: O(n) time, O(h) space; h is tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exploreValidity(self, root: Optional[TreeNode], lower_bound: Optional[int], upper_bound: Optional[int]):

        if root is None:
            return
        
        if lower_bound < root.val < upper_bound:
            self.exploreValidity(root.left, lower_bound, root.val)
            self.exploreValidity(root.right, root.val, upper_bound)
        else:
            self.is_valid = False
            return

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.is_valid = True

        self.exploreValidity(root, float("-inf"), float("inf"))

        return self.is_valid
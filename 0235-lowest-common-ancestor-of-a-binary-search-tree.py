# 235. Lowest Common Ancestor of a Binary Search Tree
# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Submitted: 2026-08-29 13:17 EDT
# Intuition: The first BST node where the targets split is their lowest common ancestor.
# Approach: Walk left or right while both target values are on the same side.
# Complexity: O(h) time, O(1) space.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while (p.val > root.val and q.val > root.val) or (p.val < root.val and q.val < root.val):

            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
        
        return root
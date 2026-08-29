# 543. Diameter of Binary Tree
# Problem: https://leetcode.com/problems/diameter-of-binary-tree/
# Submitted: 2026-08-28 21:39 EDT
# Intuition: The longest path through a node joins its left and right subtree heights.
# Approach: Compute heights with DFS while updating the largest sum of child heights.
# Complexity: O(n) time, O(h) space.

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

        d_left = self.explore(root.left)
        d_right = self.explore(root.right) 

        self.max_diameter = max(self.max_diameter, d_left + d_right)
        
        return max(d_left, d_right) + 1
            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_diameter = 0

        self.explore(root)

        return self.max_diameter
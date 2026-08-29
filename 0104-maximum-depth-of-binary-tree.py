# 104. Maximum Depth of Binary Tree
# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Submitted: 2026-08-28 21:21 EDT
# Intuition: A node's maximum depth is one plus its deeper child's depth.
# Approach: Recursively compute child depths, using zero for missing children.
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

        depth_left = 0
        depth_right = 0
        
        if root.left is not None:
            depth_left += self.explore(root.left)
        if root.right is not None:
            depth_right += self.explore(root.right)

        if depth_left >= depth_right:
            return depth_left + 1
        else:
            return depth_right + 1
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.explore(root)
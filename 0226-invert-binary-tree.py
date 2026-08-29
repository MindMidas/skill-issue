# 226. Invert Binary Tree
# Problem: https://leetcode.com/problems/invert-binary-tree/
# Submitted: 2026-08-28 20:22 EDT
# Intuition: Mirroring a tree swaps the left and right subtree at every node.
# Approach: Recursively invert both children, then swap their pointers.
# Complexity: O(n) time, O(h) space.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self, root: Optional[TreeNode]) -> None:
        
        if root is None:
            return None
        if root.left is not None: 
            self.swap(root.left)
        if root.right is not None:
            self.swap(root.right)

        dummy = root.left
        root.left = root.right
        root.right = dummy
            
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap(root)
        return root
        
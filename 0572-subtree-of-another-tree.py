# 572. Subtree of Another Tree
# Problem: https://leetcode.com/problems/subtree-of-another-tree/
# Submitted: 2026-08-29 12:45 EDT
# Intuition: A matching subtree must have the same values and structure at some root.
# Approach: Try each tree node and recursively compare it against the candidate subtree.
# Complexity: O(n*m) worst-case time, O(h1 + h2) space for the two tree heights.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compareSubtree(self, subRoot1: Optional[TreeNode], subRoot2: Optional[TreeNode]) -> bool:
        
        if subRoot1 is None and subRoot2 is None:
            return True
        
        if subRoot1 is not None and subRoot2 is not None:
            if subRoot1.val != subRoot2.val:
                return False
            return (
                self.compareSubtree(subRoot1.left, subRoot2.left)
                and
                self.compareSubtree(subRoot1.right, subRoot2.right)
            )
        else:
            return False

        
    def exploreTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        
        if root is None:
            return

        if self.compareSubtree(root, subRoot):
            self.is_subtree = True
            return
            
        self.exploreTree(root.left, subRoot)
        self.exploreTree(root.right, subRoot)        


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.is_subtree = False
        self.exploreTree(root, subRoot)
        return self.is_subtree
        
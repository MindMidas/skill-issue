# 100. Same Tree
# Problem: https://leetcode.com/problems/same-tree/
# Submitted: 2026-08-29 12:03 EDT
# Intuition: Equal trees have equal node values and matching left and right structure.
# Approach: Recursively compare corresponding nodes and mark any value or shape mismatch.
# Complexity: O(n + m) upper-bound time, O(h) recursion space.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def compare(self, p: Optional[TreeNode], q: Optional[TreeNode]):

        if p is None and q is None:
            return
        
        if p is not None and q is not None:
            if p.val != q.val:
                self.same = False
                return
            self.compare(p.left, q.left)
            self.compare(p.right, q.right)
            
        else:
            self.same = False
            return
        
            
        


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.same = True

        self.compare(p,q)

        return self.same
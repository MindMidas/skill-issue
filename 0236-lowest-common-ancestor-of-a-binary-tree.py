# 236. Lowest Common Ancestor of a Binary Tree
# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Submitted: 2026-11-03 11:53 EST
# Intuition: If p and q are found on opposite sides of a node, that node is their lowest common ancestor.
# Approach: DFS returns a target or an LCA; combine results from both children, or pass up the nonempty side.
# Complexity: O(n) time, O(h) extra space for recursion, where h is the tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def dfs(node):
            
            # empty subtree has no match
            if node == None:
                return 
            
            # return a target as soon as we find it
            if node == p:
                return node
            if node == q:
                return q
            
            # explore left and right
            left = dfs(node.left)
            right = dfs(node.right)

            # matches on both sides make this node the LCA
            if left and right:
                return node
            
            # pass up the match or LCA from the nonempty side
            return left if left else right


        return dfs(root)

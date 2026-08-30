# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Submitted: 2026-08-30 15:54 EDT
# Intuition: The first preorder value is the root and partitions the inorder traversal.
# Approach: Find its inorder index and recursively construct subtrees from sliced lists.
# Complexity: O(n^2) worst-case time and space from searches and retained slices.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recurseBuild(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.recurseBuild(preorder[1:mid+1], inorder[:mid])
        root.right = self.recurseBuild(preorder[mid+1:], inorder[mid+1:])

        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        return self.recurseBuild(preorder, inorder)
        
        
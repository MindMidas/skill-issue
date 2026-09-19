# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Submitted: 2026-09-19 14:00 EDT
# Intuition: The final postorder value is the root, splitting inorder into two subtrees.
# Approach: Find the root in inorder and recursively build from sliced traversal lists.
# Complexity: O(n^2) worst-case time and space due to repeated searches and retained slices.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        
        if not inorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left_size = len(left_inorder)

        left_postorder = postorder[:left_size]
        right_postorder = postorder[left_size:-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
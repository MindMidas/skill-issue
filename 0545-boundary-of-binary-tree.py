# 545. Boundary of Binary Tree
# Problem: https://leetcode.com/problems/boundary-of-binary-tree/
# Submitted: 2026-10-29 12:01 EDT
# Intuition: Build the counterclockwise boundary in separate pieces, excluding leaves from the side boundaries to avoid duplicates.
# Approach: Add the root, left boundary top-down, leaves left-to-right, and right boundary bottom-up.
# Complexity: O(n) time, O(h) auxiliary space plus O(n) output space; h is tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        # Traverse counterclockwise: root, left boundary, leaves, then the right boundary bottom-up.
        # Collect leaves separately so boundary leaves appear only once.
        result = []

        def dfsLeft(node):

            # Stop at an empty child.
            if not node:
                return

            # Leave leaf nodes for the separate leaf traversal.
            if not node.left and not node.right:
                return

            result.append(node.val)

            # Follow the left edge, falling back to the right child when needed.
            if node.left:
                dfsLeft(node.left)
            else:
                dfsLeft(node.right)
            
        def dfsLeaves(node):
            
            # Stop at an empty child.
            if not node:
                return
            
            # Collect leaves from left to right.
            if not node.left and not node.right:
                result.append(node.val)
                return
            
            dfsLeaves(node.left)
            dfsLeaves(node.right)

        def dfsRight(node):

            # Stop at an empty child.
            if not node:
                return
            # Leave leaf nodes for the separate leaf traversal.
            if not node.left and not node.right:
                return
            
            # Follow the right edge, falling back to the left child when needed.
            if node.right:
                dfsRight(node.right)
            else:
                dfsRight(node.left)
            
            # Append while unwinding so the right boundary is collected bottom-up.
            result.append(node.val)

        # An empty tree has no boundary.
        if not root:
            return []
        
        # Add the root once, then collect the non-leaf left boundary.
        result.append(root.val)
        dfsLeft(root.left)

        # Skip the leaf traversal for a single-node tree; its root is already included.
        if root.left or root.right:
            dfsLeaves(root)

        # Finish with the non-leaf right boundary in reverse order.
        dfsRight(root.right)

        return result
# 968. Binary Tree Cameras
# Problem: https://leetcode.com/problems/binary-tree-cameras/
# Submitted: 2026-10-29 15:26 EDT
# Intuition: Put a camera at the parent of an uncovered child to cover the child, itself, and its parent.
# Approach: DFS bottom-up with three states; add a final camera if the root is uncovered.
# Complexity: O(n) time, O(h) extra space for recursion, where h is the tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        
        # 0 = uncovered, needs a camera from parent
        # 1 = covered, no camera here
        # 2 = has a camera

        cameras = 0

        def dfs(node):
            nonlocal cameras

            # empty children are covered and never need a camera
            if not node:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)

            # an uncovered child needs a camera here
            if left == 0 or right == 0:
                cameras += 1
                return 2
            
            # a child's camera already covers this node
            if left == 2 or right == 2:
                return 1
            
            # ask the parent to cover this node
            return 0
        
        # root has no parent, so cover it here if needed
        if dfs(root) == 0:
            cameras += 1
        
        return cameras

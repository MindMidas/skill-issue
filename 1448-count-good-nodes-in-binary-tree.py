# 1448. Count Good Nodes in Binary Tree
# Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Submitted: 2026-08-29 15:13 EDT
# Intuition: A node is good when it matches or exceeds the maximum on its root path.
# Approach: DFS while carrying the path maximum and incrementing a shared count.
# Complexity: O(n) time, O(h) space; h is tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findGoodNodes(self, root: Optional[TreeNode], max_so_far: Optional[int]):

        if root is None:
            return 
        
        if max_so_far is None:
            max_so_far = root.val
    
        if root.val >= max_so_far:
            self.total_good += 1
        
        max_so_far = max(max_so_far, root.val)
        
        self.findGoodNodes(root.left, max_so_far)
        self.findGoodNodes(root.right, max_so_far)
        
    def goodNodes(self, root: TreeNode) -> int:

        self.total_good = 0

        self.findGoodNodes(root, None)

        return self.total_good


        
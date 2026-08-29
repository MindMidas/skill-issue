# 199. Binary Tree Right Side View
# Problem: https://leetcode.com/problems/binary-tree-right-side-view/
# Submitted: 2026-08-29 14:24 EDT
# Intuition: Visiting right children first reveals the rightmost node at every depth.
# Approach: DFS right before left and record the first value seen at each depth.
# Complexity: O(n) time, O(h) space including the view and recursion.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exploreDFS(self, root: Optional[TreeNode], depth: int):
        if root is None:
            return

        # first node seen at this depth = rightmost node
        if depth == len(self.answer):
            self.answer.append(root.val)

        # explore right first
        self.exploreDFS(root.right, depth + 1)
        self.exploreDFS(root.left, depth + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.exploreDFS(root, 0)
        return self.answer
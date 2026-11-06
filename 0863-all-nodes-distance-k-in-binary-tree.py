# 863. All Nodes Distance K in Binary Tree
# Problem: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Submitted: 2026-11-06 14:01 EST
# Intuition: Nodes at distance k lie below the target or through an ancestor in an opposite subtree.
# Approach: DFS finds the target, collects descendants at distance k, and returns distances while checking ancestors and opposite subtrees.
# Complexity: O(n) time and O(h) auxiliary space, excluding output, where h is the tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: 'TreeNode', target: 'TreeNode', k: int) -> list[int]:

        # Intuition: use DFS to find target and explore its children at distance k
        # then backtrack to ancestors, tracking their distance to the target
        # and exploring opposite subtrees for other valid nodes

        result = []

        def getKthNodes(node, dist):

            if not node:
                return

            # we found a valid kth node from target
            if dist == k:
                result.append(node.val)
                return

            # explore down left and right
            getKthNodes(node.left, dist+1)
            getKthNodes(node.right, dist+1)

        def dfs(node):

            if not node:
                return -1

            # found target so explore possible children and return 0
            if node is target:
                # explore its children and append valid
                getKthNodes(node, 0)
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # left subtree contains target
            if left >= 0:
                dist = left + 1

                if k == dist:
                    result.append(node.val)
                elif k > dist:
                    getKthNodes(node.right, dist + 1)

                return dist

            # right subtree contains target
            elif right >= 0:
                dist = right + 1

                if k == dist:
                    result.append(node.val)
                elif k > dist:
                    getKthNodes(node.left, dist + 1)

                return dist

            # subtree does not contain target
            else:
                return -1

        dfs(root)

        return result

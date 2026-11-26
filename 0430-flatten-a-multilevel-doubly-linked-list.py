# 430. Flatten a Multilevel Doubly Linked List
# Problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Submitted: 2026-11-26 10:57 EST
# Intuition: Child lists should be visited before the parent's next node.
# Approach: Recursively flatten children, reconnect their tails to the saved
# next nodes, update both link directions, and clear child pointers.
# Complexity: O(n) time and O(n) worst-case recursion space.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if not node:
                return None

            curr_next = node.next
            child_tail = None
            if node.child:
                child_tail = dfs(node.child)
                if curr_next:
                    curr_next.prev = child_tail
                    child_tail.next = curr_next

                node.next = node.child
                node.child.prev = node
                node.child = None

            next_tail = dfs(curr_next)
            return next_tail or child_tail or node

        dfs(head)
        return head

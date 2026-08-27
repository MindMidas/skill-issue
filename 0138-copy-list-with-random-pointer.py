# 138. Copy List with Random Pointer
# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/
# Submitted: 2026-08-27 18:18 EDT
# Intuition: A map preserves the correspondence between every original node and its copy.
# Approach: Create all cloned nodes first, then assign next and random pointers through the map.
# Complexity: O(n) time, O(n) space.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # handle empty list
        if head is None:
            return None

        hashtable = {}
        curr_node = head

        # add none to hashtable to avoid a crash
        hashtable[None] = None

        # create new nodes
        while curr_node is not None:
            hashtable[curr_node] = Node(curr_node.val, None, None)
            curr_node = curr_node.next

        # add next and random
        curr_node = head
        while curr_node is not None:
            hashtable[curr_node].next = hashtable[curr_node.next]
            hashtable[curr_node].random = hashtable[curr_node.random]

            curr_node = curr_node.next

        return hashtable[head]
        
# 24. Swap Nodes in Pairs
# Problem: https://leetcode.com/problems/swap-nodes-in-pairs/
# Submitted: 2026-11-18 13:08 EST
# Intuition: The node before each pair lets us reconnect the list after a swap.
# Approach: Use a dummy head, swap adjacent nodes by changing links, and advance
# the previous pointer and head to the next pair.
# Complexity: O(n) time and O(1) extra space.

from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head

        while head and head.next:
            a = head
            b = head.next
            a.next = b.next
            b.next = a
            prev.next = b
            prev = a
            head = a.next

        return dummy_head.next

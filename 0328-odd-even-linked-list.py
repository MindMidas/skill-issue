# 328. Odd Even Linked List
# Problem: https://leetcode.com/problems/odd-even-linked-list/
# Submitted: 2026-11-24 14:41 EST
# Intuition: Track the odd- and even-position tails while preserving each group's order.
# Approach: Alternate appending nodes to the two groups, keep the odd tail
# connected to the even head, and update the links as each group grows.
# Complexity: O(n) time and O(1) extra space.

from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        odd_tail = head
        even_tail = head.next
        even_head = head.next
        append_to = odd_tail
        curr = even_tail.next if even_tail else None

        while curr:
            to_append = curr
            curr = curr.next
            append_to.next = to_append
            if append_to == odd_tail:
                odd_tail = odd_tail.next
                odd_tail.next = even_head
                append_to = even_tail
                even_tail.next = curr
            else:
                even_tail = even_tail.next
                append_to = odd_tail

        return head

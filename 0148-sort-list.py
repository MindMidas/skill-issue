# 148. Sort List
# Problem: https://leetcode.com/problems/sort-list/
# Submitted: 2026-11-19 18:28 EST
# Intuition: Merge sort works on a linked list by splitting and relinking nodes.
# Approach: Find the midpoint with slow and fast pointers, recursively sort
# both halves, then merge them using a dummy head.
# Complexity: O(n log n) time and O(log n) recursion space.

from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        curr.next = left if left else right
        return dummy.next

    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

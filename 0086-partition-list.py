# 86. Partition List
# Problem: https://leetcode.com/problems/partition-list/
# Submitted: 2026-11-22 12:16 EST
# Intuition: Build two lists while preserving the order in which nodes appear.
# Approach: Append nodes to either the less-than or greater-than-or-equal list,
# terminate the latter, then join both lists using dummy heads.
# Complexity: O(n) time and O(1) extra space.

from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        lt_dummy = ListNode()
        gt_dummy = ListNode()
        curr = head
        curr_lt = lt_dummy
        curr_gt = gt_dummy

        while curr:
            if curr.val < x:
                curr_lt.next = curr
                curr_lt = curr_lt.next
            else:
                curr_gt.next = curr
                curr_gt = curr_gt.next
            curr = curr.next

        curr_gt.next = None
        curr_lt.next = gt_dummy.next
        return lt_dummy.next

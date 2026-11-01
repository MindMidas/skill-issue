# 142. Linked List Cycle II
# Problem: https://leetcode.com/problems/linked-list-cycle-ii/
# Submitted: 2026-11-01 12:56 EST
# Intuition: Fast and slow meet inside a cycle; restarting one at the head lets them meet again at its entry.
# Approach: Detect a meeting with two speeds, then move both one step at a time to find the cycle's start.
# Complexity: O(n) time, O(1) extra space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head

        # fast catches slow if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # loop ended without meeting, so there is no cycle
            return None

        # restart one pointer; moving both one step makes them meet at the cycle entry
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

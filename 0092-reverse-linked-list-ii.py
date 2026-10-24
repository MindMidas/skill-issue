# 92. Reverse Linked List II
# Problem: https://leetcode.com/problems/reverse-linked-list-ii/
# Submitted: 2026-10-24 15:49 EDT
# Intuition: Reverse only the requested segment, then reconnect it to the untouched ends.
# Approach: Find left, reverse pointers through right, and reconnect the segment's new head and tail.
# Complexity: O(n) time, O(1) extra space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        curr = head
        i = 1

        dummy_left = None

        while i != left:
            dummy_left = curr
            curr = curr.next
            i += 1
        
        tail = curr
        prev = None

        while i <= right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i += 1
        
        tail.next = curr

        if dummy_left:
            dummy_left.next = prev
        else:
            head = prev

        return head
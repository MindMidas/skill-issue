# 1290. Convert Binary Number in a Linked List to Integer
# Problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Submitted: 2026-10-24 14:26 EDT
# Intuition: Each next bit doubles the value so far, then adds the new bit.
# Approach: Walk the list and update dec = dec * 2 + head.val at each node.
# Complexity: O(n) time, O(1) extra space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        
        dec = 0

        while head:

            dec = (dec * 2) + head.val
            head = head.next

        return dec
            

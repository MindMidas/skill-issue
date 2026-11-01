# 876. Middle of the Linked List
# Problem: https://leetcode.com/problems/middle-of-the-linked-list/
# Submitted: 2026-11-01 12:55 EST
# Intuition: When a pointer moving two steps reaches the end, a pointer moving one step is at the middle.
# Approach: Move fast twice and slow once per iteration; return slow, which gives the second middle for even lengths.
# Complexity: O(n) time, O(1) extra space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        # fast moves twice as far, so slow stops at the middle

        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

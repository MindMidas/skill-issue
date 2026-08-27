# 19. Remove Nth Node From End of List
# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Submitted: 2026-08-27 17:54 EDT
# Intuition: A fixed gap lets the leading pointer locate the nth node from the end.
# Approach: Start from a dummy node, advance fast n+1 steps, then move both and unlink slow.next.
# Complexity: O(n) time, O(1) space; n here is the list length.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        new_head = ListNode(0, head)
        fast = new_head
        slow = new_head

        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return new_head.next
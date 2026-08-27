# 21. Merge Two Sorted Lists
# Problem: https://leetcode.com/problems/merge-two-sorted-lists/
# Submitted: 2026-08-27 15:48 EDT
# Intuition: The smallest remaining node is always at the head of one of the sorted lists.
# Approach: Relink the smaller head repeatedly, then attach the remaining tail.
# Complexity: O(n + m) time, O(1) auxiliary space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        c1 = list1
        c2 = list2
        tail = None

        if c1.val <= c2.val:
            head = c1
            tail = c1
            c1 = c1.next
        else:
            head = c2
            tail = c2
            c2 = c2.next
        
        while c1 is not None and c2 is not None:
            
            # move the tail
            if c1.val <= c2.val:
                tail.next = c1
                tail = c1
                c1 = c1.next
            else:
                tail.next = c2
                tail = c2
                c2 = c2.next

        if c1 is None:
            tail.next = c2
        if c2 is None:
            tail.next = c1
        
        return head



        
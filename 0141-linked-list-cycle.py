# 141. Linked List Cycle
# Problem: https://leetcode.com/problems/linked-list-cycle/
# Submitted: 2026-08-27 16:33 EDT
# Intuition: Inside a cycle, a pointer moving twice as fast eventually meets a slower one.
# Approach: Advance slow by one link and fast by two until they meet or reach the end.
# Complexity: O(n) time, O(1) space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       
        if head is None:
            return False
        
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            
            # move fast by 1
            fast = fast.next.next

            # move slow by 1 
            slow = slow.next
            
            # we have a cycle
            if fast == slow:
                return True
        
        return False
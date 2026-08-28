# 2. Add Two Numbers
# Problem: https://leetcode.com/problems/add-two-numbers/
# Submitted: 2026-08-28 16:55 EDT
# Intuition: Digits are already stored least-significant first, so carries move forward.
# Approach: Traverse both lists, append each summed digit, and propagate the carry.
# Complexity: O(n + m) time, O(max(n, m)) output space; O(1) auxiliary space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        carry = 0
        total = 0
        answer = None
        curr = answer

        while l1 is not None and l2 is not None:
            
            total = l1.val + l2.val + carry

            carry = total // 10
            digit = total % 10

            if curr is None:
                curr = ListNode(val = digit, next = None)
                answer = curr
            else:
                curr.next = ListNode(val = digit, next = None)
                curr = curr.next

            l1 = l1.next
            l2 = l2.next
        
        if l1 is not None:
            while l1 is not None:
                total = l1.val + carry
                
                carry = total // 10
                digit = total % 10
                
                curr.next = ListNode(val = digit, next = None)
                curr = curr.next

                l1 = l1.next
        
        if l2 is not None:
            while l2 is not None:
                total = l2.val + carry
                
                carry = total // 10
                digit = total % 10
                
                curr.next = ListNode(val = digit, next = None)
                curr = curr.next

                l2 = l2.next

        if carry != 0:
            curr.next = ListNode(val = carry, next = None)
            curr = curr.next
        
        return answer

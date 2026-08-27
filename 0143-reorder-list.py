# 143. Reorder List
# Problem: https://leetcode.com/problems/reorder-list/
# Submitted: 2026-08-27 17:29 EDT
# Intuition: The required order alternates nodes from the front and the reversed back half.
# Approach: Find the midpoint, reverse the second half, and weave the two halves in place.
# Complexity: O(n) time, O(1) space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head

        # split into two halves using midpoint
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        # reverse 2nd half
        prev_node = None
        curr_node = second_half
        
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # weave 1st half with 2nd half
        weave_node = prev_node
        curr_node = head
        
        while weave_node is not None:
            
            # remember the tail
            tail = curr_node.next

            # weave the new node and move weave_node to next in second half
            curr_node.next = weave_node
            weave_node = weave_node.next

            # make newly weaved node next point to tail
            curr_node.next.next = tail

            # move current node forward
            curr_node = tail
# 206. Reverse Linked List
# Problem: https://leetcode.com/problems/reverse-linked-list/
# Submitted: 2026-08-27 15:13 EDT
# Intuition: Reversing a list means redirecting every next pointer to the previous node.
# Approach: Walk once while saving the next node and reversing the current pointer.
# Complexity: O(n) time, O(1) space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p_node = None
        c_node = head
        n_node = None

        while c_node is not None:

            # set next node
            n_node = c_node.next

            # set current node next to the previous
            c_node.next = p_node

            # set previous node to current node
            p_node = c_node

            # set current node to be the next node
            c_node = n_node

        
        return p_node


            
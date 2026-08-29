# 25. Reverse Nodes in k-Group
# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Submitted: 2026-08-28 20:03 EDT
# Intuition: Each complete group of k nodes can be reversed independently.
# Approach: Detach full groups, reverse their pointers, and reconnect their heads and tails.
# Complexity: O(n) time, O(1) space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
        
        prev_node = None
        tail = head

        while head is not None:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node     
        
        return prev_node, tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        chunk = k
        chunk_head = head

        answer = None
        prev_chunk_tail = None

        while head is not None:
            chunk -= 1

            if chunk == 0:
                next_node = head.next
                head.next = None

                r_c_head, r_c_tail= self.reverse(chunk_head)

                if answer is None:
                    answer = r_c_head
                else:
                    prev_chunk_tail.next = r_c_head

                r_c_tail.next = next_node
                prev_chunk_tail = r_c_tail

                head = r_c_tail
                chunk_head = next_node
                chunk = k

            head = head.next

        
        return answer
            
            

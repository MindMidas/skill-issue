# 2074. Reverse Nodes in Even Length Groups
# Problem: https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
# Submitted: 2026-11-01 11:51 EST
# Intuition: Find each group's actual length and reverse its links only when that length is even.
# Approach: Walk groups of increasing size, reverse even groups in place, and reconnect through the previous tail.
# Complexity: O(n) time, O(1) extra space; each node is visited at most twice.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: ListNode | None) -> ListNode | None:
        
        def reverse(head, tail):
            after = tail.next  # first node after the group
            prev = after # node to link the current node to
            curr = head # first node to reverse

            # reverse until we reach the next group
            while curr != after:
                nxt = curr.next # save the next node
                curr.next = prev # reverse the link
                prev = curr # move prev forward
                curr = nxt # move curr forward

            return prev # new head of the reversed group
        

        dummy = ListNode(0, head)
        prev_tail = dummy
        group_size = 0

        while prev_tail.next:
            group_size += 1 # new group size
            group_head = prev_tail.next
            group_tail = group_head
            actual_len = 1

            # walk until we reach the expected size or end of list
            while actual_len < group_size and group_tail.next:
                group_tail = group_tail.next
                actual_len += 1
            
            # use the actual length, since the last group may be shorter
            if actual_len % 2 == 0:
                new_head = reverse(group_head, group_tail)
                prev_tail.next = new_head # reconnect the previous group
                prev_tail = group_head # old head is now tail
            else:
                prev_tail = group_tail # odd, no need to reverse, just advance
        
        return dummy.next

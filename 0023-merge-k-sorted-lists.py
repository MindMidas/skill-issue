# 23. Merge k Sorted Lists
# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# Submitted: 2026-08-28 19:05 EDT
# Intuition: Merging lists in pairs keeps the number of merge rounds logarithmic.
# Approach: Repeatedly merge adjacent list pairs by relinking their existing nodes.
# Complexity: O(N log(k+1) + k) time, O(k) space; N total nodes, k lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummy = ListNode()
        tail = dummy
        dummy.next = tail
        

        while l1 is not None and l2 is not None:

            if l1.val <= l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        
        if l1 is not None:
            tail.next = l1

        if l2 is not None:
            tail.next = l2
        
        return dummy.next
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
    
        while len(lists) != 1:

            temp_list = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                merged = l1

                if i + 1 <= len(lists) - 1:
                    l2 = lists[i+1]
                    merged = self.merge(l1, l2)

                temp_list.append(merged)
            
            lists = temp_list

        return lists[0]
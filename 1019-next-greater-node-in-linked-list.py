# 1019. Next Greater Node In Linked List
# Problem: https://leetcode.com/problems/next-greater-node-in-linked-list/
# Submitted: 2026-11-23 16:57 EST
# Intuition: A decreasing stack holds nodes still waiting for a greater value.
# Approach: Traverse the list, resolving smaller stacked values with the current
# node's value. Leave zero for positions with no greater node to their right.
# Complexity: O(n) time and O(n) space.

from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        answer = []
        stack = []
        curr = head
        i = 0
        while curr:
            answer.append(0)
            while stack and curr.val > stack[-1][1]:
                j, val = stack.pop()
                answer[j] = curr.val
            stack.append((i, curr.val))
            i += 1
            curr = curr.next

        return answer

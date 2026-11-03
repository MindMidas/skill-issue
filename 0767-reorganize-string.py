# 767. Reorganize String
# Problem: https://leetcode.com/problems/reorganize-string/
# Submitted: 2026-11-03 11:25 EST
# Intuition: Use the most frequent available letter, keeping the previous letter aside so it cannot repeat immediately.
# Approach: Build a max heap of counts, delay reinserting the last letter, and return empty if some copies remain unused.
# Complexity: O(n) time for the fixed 26-letter alphabet, O(n) extra space for the result; the heap uses O(1) space.

import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # create a freq dict
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # create a max heap
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        solution = []
        prev = None # hold the last character out of the heap

        # use the most frequent available character
        while max_heap:
            
            # pop and append to solution
            count, char = heapq.heappop(max_heap)
            solution.append(char)
            count += 1

            # the previous character is safe to reuse after placing a different one
            if prev:
                heapq.heappush(max_heap, prev)
            
            # hold this character back if it still has copies left
            if count == 0:
                prev = None
            else:
                prev = (count, char)
        
        # leftover copies could not be separated
        if len(solution) != len(s):
            return ""

        return ''.join(solution)

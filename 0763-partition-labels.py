# 763. Partition Labels
# Problem: https://leetcode.com/problems/partition-labels/
# Submitted: 2026-09-03 15:40 EDT
# Intuition: A partition must extend to the last occurrence of every character it contains.
# Approach: Record last indices and close each partition when the scan reaches its boundary.
# Complexity: O(n) time, O(n) space including output; O(1) auxiliary map for lowercase letters.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        valid_lens = []

        if s[0] == s[-1]:
            return [len(s)]
        
        last_index = {}

        for i, char in enumerate(s):
            last_index[char] = i

        substrings = []
        curr_end = last_index[s[0]]
        start_index = 0
        
        for i, char in enumerate(s):
            
            if last_index[char] > curr_end:
                curr_end = last_index[char]
            if i == curr_end:
                substrings.append(i - start_index + 1)
                start_index = i + 1
                if start_index != len(s):
                    curr_end = last_index[s[start_index]]


        return substrings
            


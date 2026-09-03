# 1899. Merge Triplets to Form Target Triplet
# Problem: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# Submitted: 2026-09-03 14:58 EDT
# Intuition: A triplet exceeding the target anywhere can never help form it.
# Approach: Ignore unsafe triplets and track whether each of the three target values is met.
# Complexity: O(n) time, O(1) space for fixed-size triplets.

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        merge = [None] * len(target)

        for triplet in triplets:

            is_safe = True

            for i in range(len(target)):

                if triplet[i] > target[i]:
                    is_safe = False
                    break
            
            if is_safe:
                for i in range(len(target)):
                    if triplet[i] == target[i]:
                        merge[i] = target[i]
            
            if merge == target:
                return True
        
        return False
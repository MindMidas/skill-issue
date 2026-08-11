# 347. Top K Frequent Elements
# Problem: https://leetcode.com/problems/top-k-frequent-elements/
# Submitted: 2026-08-11 16:37 EDT
# Intuition: Frequencies range from 1 to n, so buckets can replace sorting.
# Approach: Count values, group them by frequency, and collect the highest buckets first.
# Complexity: O(n) average time, O(n) space.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        for num, count in frequency.items():
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, -1, -1):
            
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
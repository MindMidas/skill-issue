# 4. Median of Two Sorted Arrays
# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Submitted: 2026-08-27 14:42 EDT
# Intuition: A valid partition puts half the values on the left with no crossing inversions.
# Approach: Binary-search the smaller array's cut and read the median from the boundary values.
# Complexity: O(log(min(n, m) + 1)) time, O(1) space.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # search smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
    
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        left = 0 
        right = len(nums1)

        while left <= right:

            cut1 = left + (right - left) // 2
            cut2 = half - cut1

            l1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            r1 = nums1[cut1] if cut1 < len(nums1) else float("inf")

            l2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")
            r2 = nums2[cut2] if cut2 < len(nums2) else float("inf")

            if l1 > r2:
                right = cut1 - 1 
            elif l2 > r1:
                left = cut1 + 1
            else:
                
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
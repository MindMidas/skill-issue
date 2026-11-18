# 438. Find All Anagrams in a String
# Problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Submitted: 2026-11-18 12:42 EST
# Intuition: An anagram has the same character frequencies as the pattern.
# Approach: Maintain a window of at most len(p) characters and compare its
# frequency dictionary with the pattern's, removing keys whose count reaches zero.
# Complexity: O(len(s) + len(p)) time for lowercase English letters and O(1)
# auxiliary space, plus O(len(s)) space for the output.


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k = len(p)
        freq_p = {}
        for c in p:
            freq_p[c] = freq_p.get(c, 0) + 1

        freq_s = {}
        left = 0
        ans = []
        for right, c in enumerate(s):
            c = s[right]
            freq_s[c] = freq_s.get(c, 0) + 1

            if right - left + 1 > k:
                c_left = s[left]
                if freq_s[c_left] == 1:
                    del freq_s[c_left]
                else:
                    freq_s[c_left] -= 1
                left += 1

            if freq_s == freq_p:
                ans.append(left)

        return ans

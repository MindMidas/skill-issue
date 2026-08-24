# 76. Minimum Window Substring
# Problem: https://leetcode.com/problems/minimum-window-substring/
# Submitted: 2026-08-24 19:39 EDT
# Intuition: A valid window must contain every target character with enough copies.
# Approach: Expand right, test all required counts, and shrink left while the window stays valid.
# Complexity: O(len(t) + len(s)*a) time, O(a + len(s)) space including output; a distinct characters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def is_valid(s_freq, t_freq):
            for char in t_freq:
                if s_freq.get(char, 0) < t_freq[char]:
                    return False
            return True

        t_freq = {}
        s_freq = {}
        left = 0
        best_start=0
        best_len=float("inf")

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        for right, char in enumerate(s):
            s_freq[char] = s_freq.get(char, 0) + 1
            
            while is_valid(s_freq, t_freq):

                window_len = right - left + 1
                
                if window_len < best_len:
                    best_len = window_len
                    best_start = left
                
                s_freq[s[left]] -= 1
                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start: best_start + best_len]
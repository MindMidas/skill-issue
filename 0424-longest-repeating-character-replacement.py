# 424. Longest Repeating Character Replacement
# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/
# Submitted: 2026-08-24 14:22 EDT
# Intuition: A window needs its length minus its most frequent count replacements.
# Approach: Expand right and shrink left when the replacement budget is exceeded.
# Complexity: O(n) time, O(1) space for the fixed uppercase alphabet.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left=0
        counts={}
        max_freq=0
        best=0

        for right, char in enumerate(s):

            # add new char to dictionary window
            counts[char] = counts.get(char,0) + 1

            # update max freq
            max_freq = max(max_freq, counts[char])

            # update current window size
            window_size = right - left + 1

            # check if char meets the threshhold or move left updating window_size and max_freq
            while window_size - max_freq > k:
                
                # decrease count in dict
                counts[s[left]] -= 1

                # shrink window
                left += 1

                # update max freq
                max_freq = max(counts.values())

                window_size = right - left + 1
            
            # update best
            best = max(best, window_size)

    
        return best

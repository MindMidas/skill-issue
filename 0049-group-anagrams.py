# 49. Group Anagrams
# Problem: https://leetcode.com/problems/group-anagrams/
# Submitted: 2026-08-11 16:16 EDT
# Intuition: Anagrams share the same frequency signature for their 26 lowercase letters.
# Approach: Count letters per word and group words by their tuple of counts.
# Complexity: O(C + n) time, O(n) auxiliary space with a fixed alphabet; C total characters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create dict
        groups = {}

        # go over words
        for word in strs:
            counts = [0] * 26
            
            # go over word chars and add count for each char
            for char in word:
                index = ord(char) - ord('a')
                counts[index] += 1
            
            # create signature and add word to dict
            signature = tuple(counts)
            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]
        
        return list(groups.values())
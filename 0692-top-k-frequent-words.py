# 692. Top K Frequent Words
# Problem: https://leetcode.com/problems/top-k-frequent-words/
# Submitted: 2026-11-18 13:35 EST
# Intuition: Sort distinct words by decreasing frequency, breaking ties alphabetically.
# Approach: Count word occurrences, sort the dictionary keys using frequency
# and word as the ordering key, and return the first k.
# Complexity: O(n + u log u) time and O(u + k) space for n words and u unique
# words, treating word lengths as bounded.


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        sorted_keys = sorted(freq, key=lambda word: (-freq[word], word))

        result = []
        for i in range(k):
            result.append(sorted_keys[i])
        return result

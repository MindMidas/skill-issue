# 127. Word Ladder
# Problem: https://leetcode.com/problems/word-ladder/
# Submitted: 2026-09-05 14:50 EDT
# Intuition: Words differing in one position share a wildcard pattern.
# Approach: Build wildcard buckets and BFS through their words to find the shortest ladder.
# Complexity: O(N*L^2 + N*L*B) time, O(N*L^2) space; length L, max bucket size B.

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        valid_next = {}

        def setValidNext(parent: str):
            
            for i in range(len(parent)):
                key = parent[:i] + "*" + parent[i+1:]

                if key not in valid_next:
                    valid_next[key] = [parent]
                else:
                    valid_next[key].append(parent)
        
        def getValidNext(parent: str):
            
            children = []

            for i in range(len(parent)):
                key = parent[:i] + "*" + parent[i+1:]
                children.extend(valid_next[key])

            return children
        


        setValidNext(beginWord)
        for parent in wordList:
          setValidNext(parent)
            
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:

            word, curr_len = queue.popleft()

            if word == endWord:
                return curr_len

            for next_word in getValidNext(word):

                if next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, curr_len + 1))
        
        return 0
# 126. Word Ladder II
# Problem: https://leetcode.com/problems/word-ladder-ii/
# Submitted: 2026-10-26 13:06 EDT
# Intuition: BFS finds the shortest distance, but every parent from the same level can lead to another shortest ladder.
# Approach: Record parents level by level, stop after reaching endWord's level, then backtrack to build every shortest path.
# Complexity: O(N*W^2 + P*D^2) time, O(N*W + D^2 + P*D) space, including copied paths.
# N = word count including beginWord, W = word length, P = shortest path count, D = words per path.

from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # return valid words that differ by exactly 1 char
        def getNeighbors(word) -> list[str]:

            neighbors = []
            
            # try replacing each char
            for i in range(len(word)):
                
                for char in "abcdefghijklmnopqrstuvwxyz":
        
                    if char == word[i]:
                        continue
                    
                    new_word = word[:i] + char + word[i+1:] 

                    if new_word in wordSet:
                        neighbors.append(new_word)

            return neighbors
        

        # init BFS with starting word
        queue = deque([beginWord])
        visited = {beginWord}
        parents = defaultdict(list)

        found = False
        
        # explore paths level by level
        while queue and not found:
            
            # track words visited in this level
            level_visited = set()

            # process all paths at the current level
            for _ in range(len(queue)):

                word = queue.popleft()

                # explore valid neighbor words
                for new_word in getNeighbors(word):
                    
                    # skip words from earlier levels
                    if new_word in visited:
                        continue

                    # record another shortest-path parent
                    parents[new_word].append(word)
                    
                    # only queue each word once per level
                    if new_word not in level_visited:
                        level_visited.add(new_word)
                        queue.append(new_word)
                    
                    # target found at this level
                    if new_word == endWord:
                        found = True

            # mark this level's words as visited
            visited.update(level_visited)

        # return empty if target was not found
        if not found:
            return []

        shortest_paths = []

        # build paths backwards using parents
        def dfs(word, path):

            # reached starting word, reverse and save path
            if word == beginWord:
                shortest_paths.append(path[::-1])
                return

            # explore every parent of current word
            for parent in parents[word]:
                dfs(parent, path + [parent])

        # reconstruct paths from endWord
        dfs(endWord, [endWord])

        return shortest_paths


# 212. Word Search II
# Problem: https://leetcode.com/problems/word-search-ii/
# Submitted: 2026-08-31 11:35 EDT
# Intuition: A trie prunes board paths that cannot start any target word.
# Approach: Build the word trie and backtrack from each cell, collecting complete matches in a set.
# Complexity: O(S + m*n*L*3^L) upper-bound time, O(S + L^2) auxiliary space; S total word length, L max word length.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word: str):

        root = self.root

        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_end = True

class Solution:

    def getDirections(self, board: List[List[str]], visited: set, r: int, c: int):
        valid = []
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < len(board) and 0 <= nc < len(board[nr]) and (nr,nc) not in visited:
                valid.append((nr,nc))
        
        return valid

    def explore(self, board: List[List[str]], visited: set, node: TrieNode, path: str, r: int, c: int):
        
        char = board[r][c]

        if char not in node.children:
            return

        node = node.children[char]
        path += char

        if node.is_end:
            self.matching_words.add(path)

        visited.add((r, c))
        next_candidates = self.getDirections(board, visited, r, c)
        
        for nr, nc in next_candidates:
            self.explore(board, visited, node, path, nr, nc)

        visited.remove((r, c))

        return False
       

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.add_word(word)
        
        self.matching_words = set()

        for r in range(len(board)):
            for c in range(len(board[r])):
                self.explore(board, set(), trie.root,"", r, c)


        
        return list(self.matching_words)
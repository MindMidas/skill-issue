# 208. Implement Trie (Prefix Tree)
# Problem: https://leetcode.com/problems/implement-trie-prefix-tree/
# Submitted: 2026-08-30 16:45 EDT
# Intuition: Words with shared prefixes can share the same chain of trie nodes.
# Approach: Follow or create one child per character, marking nodes that end a word.
# Complexity: O(L) time per operation, O(S) stored space; L query length, S inserted characters.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        root = self.root

        for key in word:

            if key not in root.children:
                root.children[key] = TrieNode()
            
            root = root.children[key]
        
        root.is_end = True

    def search(self, word: str) -> bool:

        root = self.root

        for key in word:

            if key not in root.children:
                return False
            
            root = root.children[key]
        
        return root.is_end
        

    def startsWith(self, prefix: str) -> bool:
        
        root = self.root

        for key in prefix:

            if key not in root.children:
                return False
            
            root = root.children[key]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
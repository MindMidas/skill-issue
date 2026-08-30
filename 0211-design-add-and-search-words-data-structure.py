# 211. Design Add and Search Words Data Structure
# Problem: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Submitted: 2026-08-30 17:34 EDT
# Intuition: A trie handles exact letters directly; a dot may follow any child.
# Approach: Insert letters into trie nodes and recursively branch when searching a wildcard.
# Complexity: O(L) insert, O(R*L) search upper bound from slicing; O(S + L^2) space, R visited states, S stored characters.

class WordNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        root = self.root

        for key in word:
            if key not in root.children:
                root.children[key] = WordNode()

            root = root.children[key]

        root.is_end = True
            
    def explore(self, root, word: str) -> bool:

        if not word:
            return root.is_end
        
        if word[0] == ".":
            for key in root.children:
                if self.explore(root.children[key], word[1:]):
                    return True
        else:
            if word[0] in root.children:
                return self.explore(root.children[word[0]], word[1:])
        
        return False
        
    def search(self, word: str) -> bool:
        return self.explore(self.root, word)


                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
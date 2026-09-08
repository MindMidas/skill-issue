# 146. LRU Cache
# Problem: https://leetcode.com/problems/lru-cache/
# Submitted: 2026-09-08 13:42 EDT
# Intuition: A hash map finds items quickly while a linked list tracks recency.
# Approach: Move accessed items to the MRU end and evict from the LRU end when full.
# Complexity: O(1) average time per get/put, O(c) space for capacity c.

class Node:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nxt = nxt
        
class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity 
        self.hashmap = {}
        self.lru = Node()
        self.mru = Node()
        self.lru.nxt = self.mru
        self.mru.prev = self.lru
    
    def remove(self, node):
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
        node.prev = None
        node.nxt = None
    
    def insert(self, node):
        node.prev = self.mru.prev
        node.nxt = self.mru
        self.mru.prev.nxt = node
        self.mru.prev = node

    def get(self, key: int) -> int:

        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            self.hashmap[key].val = value
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
        else:
            new_node = Node(key=key, val=value)
            self.hashmap[key] = new_node

            self.insert(new_node)

            if self.capacity >= 1:
                self.capacity -= 1
            else:
                del self.hashmap[self.lru.nxt.key]
                self.remove(self.lru.nxt)
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
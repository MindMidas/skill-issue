# 460. LFU Cache
# Problem: https://leetcode.com/problems/lfu-cache/
# Submitted: 2026-10-27 15:05 EDT
# Intuition: Evict from the lowest frequency; within that group, evict the least recently used key.
# Approach: Track values and counts in a map, move keys between OrderedDict frequency bins, and maintain the minimum frequency.
# Complexity: O(1) average time per get/put; O(C + Q) worst-case space since empty bins are kept (capacity C, Q operations).

from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        
        self.bins = {} # freq bins hold ordered dict for keys
        self.cache = {} # stores val & freq 
        self.lfu = 1
        self.capacity = capacity 

    def get(self, key: int) -> int:
        
        # key doesn't exist
        if key not in self.cache:
            return -1
        
        # get value and freq 
        key_val, key_freq = self.cache[key]

        # remove from old freq
        self.bins[key_freq].pop(key)

        # check if lfu needs to be updated
        if not self.bins[key_freq] and self.lfu == key_freq:
            self.lfu += 1

        # move to new freq
        key_freq += 1
        if key_freq not in self.bins:
            self.bins[key_freq] = OrderedDict()
        self.bins[key_freq][key] = None

        # set new freq in cache
        self.cache[key] = (key_val, key_freq)

        return key_val



    def put(self, key: int, value: int) -> None:
        
        # 1) if key already exists, increment and freq, also updating lfu if needed
        if key in self.cache:
            
            # get key freq
            _, key_freq = self.cache[key]

            # increment freq in bins
            self.bins[key_freq].pop(key)

            # check if lfu needs to be updated
            if not self.bins[key_freq] and self.lfu == key_freq:
                self.lfu += 1
            
            # move to new freq
            key_freq += 1
            if key_freq not in self.bins:
                self.bins[key_freq] = OrderedDict()
            self.bins[key_freq][key] = None

            # set new freq in cache
            self.cache[key] = (value, key_freq)
            
        
        # 2) key does not exist, check capacity, remove lfu if needed (and update), insert new key
        else:
            
            # remove lfu to make space for new key
            if self.capacity == 0:
                lfu_key, _ = self.bins[self.lfu].popitem(last=False) # pop leftmost
                del self.cache[lfu_key]
            else:
                self.capacity -= 1
            
            # inserting new key sets lfu to 1
            self.lfu = 1 

            # add new key to cache and freq bin
            self.cache[key] = (value, 1)
            if 1 not in self.bins:
                self.bins[1] = OrderedDict()
            self.bins[1][key] = None
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
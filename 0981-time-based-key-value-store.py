# 981. Time Based Key-Value Store
# Problem: https://leetcode.com/problems/time-based-key-value-store/
# Submitted: 2026-08-26 21:59 EDT
# Intuition: Timestamps arrive in order, so each key's values can be binary-searched.
# Approach: Append timestamp/value pairs and find the latest timestamp not exceeding the query.
# Complexity: Average O(1) set, O(log k) get; O(N) stored space, k entries for the queried key.

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        
        left = 0
        right = len(self.store[key]) - 1

        value = ""
        
        while left <= right:

            mid = left + (right - left) // 2

            if self.store[key][mid][0] <= timestamp:
                value = self.store[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1 
        
        return value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
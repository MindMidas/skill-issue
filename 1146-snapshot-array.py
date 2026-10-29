# 1146. Snapshot Array
# Problem: https://leetcode.com/problems/snapshot-array/
# Submitted: 2026-10-29 16:58 EDT
# Intuition: Store changes for each index instead of copying the whole array for every snapshot.
# Approach: Keep (snapshot id, value) histories; overwrite within the current snapshot and binary search older values.
# Complexity: Init O(n), set O(1) amortized, snap O(1), get O(log h) time; O(n + u) total space.
# n is array length, h is the queried index's history length, and u is the number of appended changes.

class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = [[(0,0)] for _ in range(length)]
        self.id = 0

    def set(self, index: int, val: int) -> None:
        # same snapshot, overwrite the latest value
        if self.snaps[index][-1][0] == self.id:
            self.snaps[index][-1] = (self.id, val)
        # new snapshot, keep the old value and append
        else:
            self.snaps[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:

        # get history for this index
        history = self.snaps[index]
        left = 0
        right = len(history) - 1

        # find the latest change at or before the requested snapshot
        while left <= right:

            # check the middle snapshot
            mid = (left + right) // 2

            # narrow the search by snapshot id
            if history[mid][0] > snap_id:
                right = mid - 1
            elif history[mid][0] < snap_id:
                left = mid + 1
            else:
                return history[mid][1]
        
        # right points to the last change before the requested snapshot
        return history[right][1]
                

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

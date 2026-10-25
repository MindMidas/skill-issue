# 895. Maximum Frequency Stack
# Problem: https://leetcode.com/problems/maximum-frequency-stack/
# Submitted: 2026-10-25 13:33 EDT
# Intuition: Group values by frequency; a stack within each group breaks ties by most recent push.
# Approach: Track counts and frequency bins, then pop from the highest bin and lower max_freq when it empties.
# Complexity: O(1) average amortized time per push/pop, O(p) space for p total pushes.

class FreqStack:

    def __init__(self):

        self.freq = {}
        self.bins = {}
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        
        # increase freq of val
        if val not in self.freq:
            self.freq[val] = 1
        else:
            self.freq[val] += 1
        
        # update highest freq so far
        self.max_freq = max(self.max_freq, self.freq[val])

        # add val to the right bin
        if self.freq[val] not in self.bins:
            self.bins[self.freq[val]] = []
        self.bins[self.freq[val]].append(val)

    def pop(self) -> int:
        
        # pop val from bin using curr max_freq (handles ties), and decrement freq
        val = self.bins[self.max_freq].pop()
        self.freq[val] -= 1

        # only reduce highest freq if bin is empty
        if len(self.bins[self.max_freq]) == 0:
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
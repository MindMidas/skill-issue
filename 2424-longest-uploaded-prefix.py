# 2424. Longest Uploaded Prefix
# Problem: https://leetcode.com/problems/longest-uploaded-prefix/
# Submitted: 2026-11-15 13:06 EST
# Intuition: Once all videos up to an index are uploaded, the prefix cannot shrink.
# Approach: Mark uploads in a boolean array. When asked for the longest prefix,
# advance the saved prefix until the next video is missing or all are uploaded.
# Complexity: O(n) initialization and space, O(1) per upload, and O(n) worst-case
# for one longest call. Across q longest calls, the total query time is O(n + q).


class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = [False] * (n + 1)
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True

    def longest(self) -> int:
        while self.prefix + 1 < len(self.uploaded) and self.uploaded[self.prefix + 1]:
            self.prefix += 1

        return self.prefix

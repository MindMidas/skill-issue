# 609. Find Duplicate File in System
# Problem: https://leetcode.com/problems/find-duplicate-file-in-system/
# Submitted: 2026-11-11 12:05 EST
# Intuition: Files with identical contents belong to the same group, regardless of their names or directories.
# Approach: Parse each file's name and contents, group full paths by contents, and return the groups with at least two paths.
# Complexity: O(L + P) average time and O(L + P) space, where L is the total input length and P is the combined length of the constructed paths.

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        duplicate_paths = {}

        for p in paths:
            data = p.split(" ")
            directory = data[0]

            i = 1
            while i < len(data):
                file_data = data[i]
                # extract and clean name and content
                filename, content = file_data.split('(')
                content = content.rstrip(')')

                # add content path to dict
                if content not in duplicate_paths:
                    duplicate_paths[content] = []
                duplicate_paths[content].append(directory + '/' + filename)

                i += 1

        # append duplicate paths in groups to result
        dups = []
        for _, paths in duplicate_paths.items():
            if len(paths) > 1:
                dups.append(paths)

        return dups

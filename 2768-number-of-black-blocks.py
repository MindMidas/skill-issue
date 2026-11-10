# 2768. Number of Black Blocks
# Problem: https://leetcode.com/problems/number-of-black-blocks/
# Submitted: 2026-11-10 13:41 EST
# Intuition: Each black cell contributes to at most four 2x2 blocks, so only blocks touching black cells need to be tracked.
# Approach: Count black cells for every valid block top-left adjacent to each coordinate, tally blocks by count, and subtract nonempty blocks from the total to get zero-black blocks.
# Complexity: O(k) average time and O(k) space, where k is the number of black cells.

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:

        blocks = {}
        result = [0] * 5

        # iterate over coordinates
        for (x, y) in coordinates:

            # this black cell is in a block so the top left is one of these
            # find all possible blocks containing this black cell
            for i, j in [(x,y), (x-1,y), (x, y-1), (x-1,y-1)]:

                # check if the block fits inside the grid
                if 0 <= i < m-1 and 0 <= j < n-1:
                    blocks[(i, j)] = blocks.get((i, j), 0) + 1

        # count blocks with 1, 2, 3, or 4 black cells
        for count in blocks.values():
            result[count] += 1

        # total blocks minus blocks containing black cells
        result[0] = (m-1) * (n-1) - sum(result[1:])

        return result

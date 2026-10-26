# 54. Spiral Matrix
# Problem: https://leetcode.com/problems/spiral-matrix/
# Submitted: 2026-10-26 12:21 EDT
# Intuition: Keep moving in the same direction, turning right when the next cell is blocked or already visited.
# Approach: Collect each cell, mark it as 101 in place, and try moving forward or turning clockwise.
# Complexity: O(m*n) time, O(1) auxiliary space plus O(m*n) output space.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        visited = 101

        def nextMove(move, direction):

            r,c = move
            moves = [
                (r,c+1), # right
                (r+1,c), # down
                (r,c-1), # left
                (r-1,c)  # up
            ]
            
            # unpack same direction
            nr, nc = moves[direction]
            
            # try moving in same direction
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != visited:
                return (nr, nc), direction
            
            # try turning right
            else:
                # new direction
                direction = (direction + 1) % 4

                # unpack new direction
                nr, nc = moves[direction]

                # try moving in new direction
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != visited:
                    return (nr, nc), direction
                
                # no valid move
                else:
                    return None, None

        spiral = []
        direction = 0
        move = (0,0)

        # traverse the matrix in spiral order until no valid move remains
        while move is not None and direction is not None:
            # add to path
            spiral.append(matrix[move[0]][move[1]])

            # mark as visited
            matrix[move[0]][move[1]] = visited

            # get next move
            move, direction = nextMove(move,direction)
        

        return spiral
        
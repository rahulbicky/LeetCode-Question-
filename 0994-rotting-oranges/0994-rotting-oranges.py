from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        fresh_cnt = 0
        queue = deque()

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        minutes = 0

        while queue and fresh_cnt > 0:

            minutes += 1
            total_rotten = len(queue)

        
            for _ in range(total_rotten):

                i, j = queue.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                    new_i = i + dx
                    new_j = j + dy

                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                        continue

                    
                    if grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        fresh_cnt -= 1
                        queue.append((new_i, new_j))

        if fresh_cnt > 0:
            return -1

        return minutes
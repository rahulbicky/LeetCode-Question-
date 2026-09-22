from collections import deque

class Solution:
    def bfs(self, i, j, visited, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((i, j))
        visited[i][j] = 1                # mark start cell

        while len(queue) != 0:
            x, y = queue.popleft()
            # explore 4-directional neighbours
            for xx, yy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = x + xx, y + yy
                # skip out-of-bounds
                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue
                # skip water
                if grid[new_i][new_j] == "0":
                    continue
                # skip already-seen land
                if visited[new_i][new_j] == 1:
                    continue
                visited[new_i][new_j] = 1
                queue.append((new_i, new_j))

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                # new island found
                if grid[r][c] == "1" and visited[r][c] == 0:
                    count += 1
                    self.bfs(r, c, visited, grid)   # flood-fill it
        return count
        
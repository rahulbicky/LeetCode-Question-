from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        queue = deque()

        
        for r in range(rows):
            if board[r][0] == 'O':
                queue.append((r, 0))

            if board[r][cols - 1] == 'O':
                queue.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == 'O':
                queue.append((0, c))

            if board[rows - 1][c] == 'O':
                queue.append((rows - 1, c))

        
        while queue:
            r, c = queue.popleft()

            if board[r][c] != 'O':
                continue

            board[r][c] = '#'

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] == 'O'):

                    queue.append((nr, nc))

        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
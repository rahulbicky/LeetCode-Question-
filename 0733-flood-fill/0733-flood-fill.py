from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, color):

        if image[sr][sc] == color:
            return image

        rows = len(image)
        cols = len(image[0])
        initial_color = image[sr][sc]

        queue = deque([(sr, sc)])
        image[sr][sc] = color   # mark immediately

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()

            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy

                if 0 <= new_i < rows and 0 <= new_j < cols:
                    if image[new_i][new_j] == initial_color:
                        image[new_i][new_j] = color
                        queue.append((new_i, new_j))

        return image

        
        
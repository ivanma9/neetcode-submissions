from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()

        # Step 1: Add all treasures (0) to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Step 2: BFS from all treasures at once
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))

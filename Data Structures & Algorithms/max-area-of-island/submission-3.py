class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visit each island 
        # if island traverse
        # mark visited if we seen it as 0 (skippable)
        area = 0

        def dfs(x,y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            # visited.add((x,y))
            grid[x][y] = 0

            return 1 + dfs(x, y+1) + dfs(x,y-1) + dfs(x+1, y) + dfs(x-1,y)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))
        return area

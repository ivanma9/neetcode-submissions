class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        # find all the islands from 1
        # traverse thru island to see how big
        # accumulate each unvisited 1 as 
        # area return maxArea
        
        # traverse O(n^2)
        def dfs(i,j):
        #     if out of bounds or water:
            if (i < 0 or j < 0 or i == ROWS or j == COLS
                or grid[i][j] == 0):
                return 0
            #     if unvisited i:
            grid[i][j] = 0
            #         visit i 
            #         can indicate by converting to 0
            #         area +=1
            # return 1+ dfs(i,j-1) + dfs(i-1, j) + dfs(i, j+1)
            return 1 + dfs(i,j-1) + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1)
        #         traverse on 4 dir

        # go through whole grid
        #     traverse if 1 is found
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(dfs(i,j), maxArea)

        return maxArea
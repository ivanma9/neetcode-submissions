class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands= 0


        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1),(1,0), (-1,0), (0,-1)]

        def dfs(i,j):
            # process by making it zero; dont process again
            # preorder downstream (sending this is all 1 island)
            grid[i][j] = "0"

            for dx,dy in dirs:
                x = i +dx
                y = j + dy
                # if out bounds continue
                if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0":
                    continue
                dfs(x, y)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1

        return islands
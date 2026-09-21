class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m,n = len(grid), len(grid[0])

        # its job is to color as many 1 to 0
        def dfs(i,j):
            if (i < 0 or j < 0 
            or i >= m or j >= n or
            grid[i][j] == "0"):
                return
            grid[i][j] = "0" # note that it is visited
            # if want to keep intergrity
            # we could track visited set
            dfs(i,j+1)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    print("no")
                    dfs(i,j)
                    print("Kkk")
                    islands +=1
        return islands
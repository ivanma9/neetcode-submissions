class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Restate
        '''
        empty -> 0
        no islands -> 0
        all 1 island -> 1
        '''

        # count islands
        islands = 0
        m = len(grid)
        n = len(grid[0])

        # dfs
        # mark as visited by 0
        def dfs(i,j):
            grid[i][j] = "0"
            # go thru all 4 dir look for 1
            dirs = [(0,1),(1,0),(0,-1), (-1,0)]
            for x,y in dirs:
                # bounds or 0 continue
                xx = i+x
                yy = j +y
                if xx < 0 or xx >= m or yy <0 or yy >= n or grid[xx][yy] == "0":
                    continue
                dfs(xx, yy)
            




        # if 1 traverse until no more
        # dfs
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1

        return islands


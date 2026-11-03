class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Obs:
            1 land
            0 water
        goal: 
            return number of islands
            
        approach:
            find islands
            make sure to cover island so we dont double count
            count islands

            dfs until end of island
            with visited set
            count every new dfs.
            O(mn) for one island that goes through the whole
            no double count
            O(mn) space
            could do inplace spaceby marking as 0 to skip
        '''
        m,n=len(grid),len(grid[0])
        # visited = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j>=n or  grid[i][j] == "0":
                return
            grid[i][j] = "0"
            # visited.add((i,j))
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
        ct = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ct+=1

        return ct
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        '''
        -1 water
        0 start
        inf land
        multisource bfs for closest chest
        grid in place
        tie: add the same dist in there, second time we dont need to visit
        # skip if not inf
        # make change right there
        '''
        # get 0s
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        queue =deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j, 0))
        while(queue):
            nn = len(queue)
            for _ in range(nn):
                i,j,d = queue.popleft()
                for dx,dy in dirs:
                    x,y = i+dx,j+dy
                    if x < 0 or y<0 or x>=m or y>=n or grid[x][y] != 2147483647:
                        # continue
                        continue
                    queue.append((x,y,d+1))
                    grid[x][y] = d+1
                    # grid[i][j] = min(grid[i][j], d)




        


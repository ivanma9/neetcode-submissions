class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        visit=set()
        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:

                    queue.append((row,col, 0))
                    visit.add((row,col))

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        while(queue):
            qn = len(queue)
            for _ in range(qn):
                i,j, dist = queue.popleft()
                grid[i][j] = dist
                for dx,dy in dirs:
                    x,y = i+dx,j+dy
                    # unexplored
                    if x < 0 or y < 0 or x>=m or y >=n or grid[x][y] == -1 or (x,y) in visit:
                        continue
                    visit.add((x,y))
                    queue.append((x,y, dist+1))
                

                
            
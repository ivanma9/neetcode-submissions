class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = []
        for i in range(ROWS):
            for j in range(COLS):
                # add chest to queue
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        dist = 0
        visited = set()
        while(queue):
            n = len(queue)
            dist +=1

            for x in range(n):
                i, j = queue.pop(0)
                visited.add((i,j))

                directions = [(-1,0), (1,0), (0,-1), (0,1)]
                for d in directions:
                    ii, jj = i +d[0], j + d[1]
                    if not (ii < 0 or ii >= ROWS
                        or jj < 0 or jj >=COLS
                        or (ii,jj) in visited 
                        or grid[ii][jj] == -1):
                        grid[ii][jj] = dist
                        visited.add((ii,jj))
                        queue.append((ii,jj))
        



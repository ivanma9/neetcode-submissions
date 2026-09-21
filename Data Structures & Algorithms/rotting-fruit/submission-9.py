class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t= 0
        fresh = 0
        queue = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        
        while(queue and fresh > 0):
            for _ in range(len(queue)):
                # add all 4 dirs
                cur = queue.pop(0)
                xx,yy = cur
                # if in bounds and fresh fruit
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    x, y = xx + dr, yy + dc
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
                        continue
                    else:
                        queue.append((x,y))
                        grid[x][y] = 2 
                        fresh-=1
            t+=1
        return t if fresh == 0 else -1
            

        
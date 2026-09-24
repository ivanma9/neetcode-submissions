class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get all the rotten fruit as starting points
        # lets do bfs and cover all their children
        #constraints
            # if its empty just stop dont iterate more
            # if 1 fruit, turn to 2 and then add it to q
            # grid is at least size 1
        m = len(grid)
        n = len(grid[0])
        
        # count all 1s
        fruit = 0
        # make a queue from all 2
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fruit+=1
                if grid[r][c] == 2:
                    queue.append((r,c))

        t = 0
        # go through wave
        visited = set()
        while(queue):
            # for each wave
            waveN = len(queue)
            
            for _ in range(waveN):
                i,j = queue.popleft()
                # if fruit, subtract from total
                if grid[i][j] == 1:
                    fruit -=1
                grid[i][j] = 2
                if fruit == 0:
                    return t
                
                # add each children that are fruit (1)
                dirs = [(0,1),(0,-1), (1,0),(-1,0)]
                for h,v in dirs:
                    if i+h < 0 or i+h >= m or j +v <0 or j+v >= n or grid[i+h][j+v] != 1 or (i+h, j+v) in visited:
                        continue
                    queue.append((i+h, j+v))
                    visited.add((i+h, j+v))
            t+=1

        if fruit == 0:
            return t
        else:
            # some fruit unreachable
            return -1
'''
edge: unreachable orange -1y, no rotten oranges -1y, no fresh fruit 0y, neither 0y
120
022
022

t5
fresh = 0
queue []

'''

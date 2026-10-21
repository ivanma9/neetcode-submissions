class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # track time
        # every min, grows in 4 dirs from each rotten
        # edges: no rotten, no fresh, no fruit

        # add all rotten to a queue
        #bfs from each starting point at the same time.
        # increment time after all points have grown
        # once all fresh fruit are covered return time

        # note some visited, for nondupe work

        fresh = 0
        queue = deque()
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j))

        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        time=0
        # visited=set()
        while(fresh > 0 and queue):
            qn=len(queue)
            for _ in range(qn):
                cur=queue.popleft()
                i,j = cur
                # if (i,j) in visited:
                #     continue
                # visit
                # visited.add((i,j))
                for dx,dy in dirs:
                    x,y = cur[0] + dx, cur[1]+dy
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    if grid[x][y] == 1:
                        fresh-=1
                        queue.append((x,y))
                        grid[x][y] = 2

                
            time +=1
        return -1 if fresh > 0 else time

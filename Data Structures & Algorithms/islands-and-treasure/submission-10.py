class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])

        # traverse thru grid
        # start from each treasure chest and build a queue
        # bfs from the chest to all the squares, if already visited, (not inf) or -1 we skip
        q = deque()
        for i in range(m):
            for j in range(n):
                # find treasure to q
                if grid[i][j] == 0:
                    q.append((i,j))

        # to not go through a chest, if 0 or -1, or visited skip
        # visited = set()
        while(q):
            cur = q.popleft()
            i,j = cur
            
            dirs = [(0,1), (0,-1),(1,0),(-1,0) ]
            # 4 dirs
            for d in dirs:
                nx, ny = cur[0] + d[0], cur[1] + d[1]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if grid[nx][ny] == INF:
                    grid[nx][ny] = grid[i][j] + 1
                    q.append((nx,ny))
# [
# [4,-1,0,1],
# [3,2, 1,-1],
# [1,-1,2,-1],
# [0,-1,3,4]]
        
# [
# [3,-1,0,1],
# [2,2,1,-1],
# [1,-1,2,-1],
# [0,-1,3,4]]

























        
                

            
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        q = []
        # add the right treasures
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # traverse from treasures
                if (grid[i][j] == 0):
                    q.append((i,j))
                    visit.add((i,j))
                    

        def add(x, y):
            if ((x,y) in visit or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1):
                return
            visit.add((x,y))
            q.append((x,y))

        ct=0
        while(q):
            for _ in range(len(q)):
                (x,y) = q.pop(0)
                grid[x][y] = ct
                add(x+1,y)
                add(x, y+1)
                add(x-1, y)
                add(x, y-1)
            ct+=1

            


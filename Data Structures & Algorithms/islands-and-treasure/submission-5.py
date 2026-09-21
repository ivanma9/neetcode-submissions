class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # go through grid bfs via the treasures

        # must compare the current square with shortest path

        def bfs(i, j, grid):
            visited = set()

            queue = [((i,j), 0)]
            while(queue):
                (x,y), dist = queue.pop(0)
                if (x,y) in visited or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1 :
                    continue
                grid[x][y] = min(dist, grid[x][y])

                dist +=1
                
                visited.add((x,y))
                queue.append(((x+1,y), dist))
                queue.append(((x-1,y), dist))
                queue.append(((x,y-1), dist))
                queue.append(((x,y+1), dist))
                        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    bfs(row, col, grid)


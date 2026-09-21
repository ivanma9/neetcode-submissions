class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
#         '''
#         start at 0,0
#         trying to swim to n-1, n-1
#         we get blocked until t = square
#         it seems that we try to take the smallest path
#         and have to take maximum t in that path
        
#         simulate like real
#         at 0,0
#         time = 0
#         must wait for neighbors to be less  or = time
#         any paths that are less than = time
#             we can traverse to furthest node
#             maybe greedily go to closest sq to n-1, n-1
        
        
#         this could be iterated if t is the mintime
#         O(n2* t)
#         time = 0


#             '''


#         # traverse from 0,0, curtime:
#         q = [(0,0)]
#         while q:
#             i,j = heapq.heappop(q)
#             if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
#                 return
            
#             if i == len(grid) -1 and j == len(grid[0]) -1:
#                 return time
#             if 
#         #     if out of bounds:
#         #         return
#         #     if in bounds:
#         #         curtime = grid[i][j]
#         #     if i == n-1 and j == n-1 in the set:
#         #         return time
#         #     if nextsquare <= time:
#         #         # go to this square:
#         #         set this to 0
#         #     else:
#         #         must wait until time == nextsquare
#         #         choice make it time be = cursquare:
#         #         check if 
#         #         traverse(i,j+1, 0)
#         #         add to pq based on lowest times for visited and not 0

# lets think backwards
# take minimum time 8

# track visited (n-1,n-1)
# heapnode (time, (r,c) pos)
# 0, , 12, 12, 14, 15 
# dequeue 2
# if r,c == 0,0 return mintime
# if visited continue
# add children in heap
#     make sure in bounds

        m = len(grid)
        n = len(grid[0])
        min_time = grid[m-1][n-1]
        visited = set()
        visited.add((m-1,n-1))
        heap = [( grid[m-1][n-1] , (m-1,n-1))]
        while (heap):
            print(heap)
            cur, coord = heapq.heappop(heap)
            r,c = coord
            min_time = max(cur, min_time) 
            if r == 0 and c == 0:
                return min_time
            
            
            # add neighbors
            directions = [(-1,0), (0,-1), (1,0), (0,1)]
            for nx, ny in directions:
                x = r + nx
                y = c + ny
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]):
                    continue
                if (x,y) not in visited:
                    visited.add((x,y))
                    heapq.heappush(heap, (grid[x][y] , (x,y)))

        


        # '''
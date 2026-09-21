class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # go through each row and count how many servers
        # go through each column and count
        # col 1,1,2,1
        # row 2, 1,1,1

        

        # col, 2, 1
        # row, 1, 2 double counting
        m = len(grid)
        n = len(grid[0])

        rows = [0] *m
        cols = [0] *n

        for i in range((m)):
            for j in range(n):
                if grid[i][j] == 1:
                    cols[j] +=1
                    rows[i] +=1
        servers = 0
        print(rows, cols)
            
        for i in range((m)):
            for j in range(n):
                if grid[i][j] == 1 and max(rows[i], cols[j]) > 1:
                    print(i,j)
                    servers +=1

        return servers
                



        





        

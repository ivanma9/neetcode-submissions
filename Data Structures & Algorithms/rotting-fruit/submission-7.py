class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        '''
        bfs
        from each rotten orange (2)
        for each 0 stop
        for each 1 continue to bfs
        and make 1 -> 2 now rotten
        decrement fresh bananact
        if unreachable -> fresh bananas still
            r -1
        '''
        queue = []
        self.fresh_fruit_ct = 0
        m, n = len(grid), len(grid[0])
        print(m,n)
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    self.fresh_fruit_ct +=1
                if (grid[i][j] == 2):
                    # rotten
                    queue.append((i,j))
        def traverse(i,j):
            if (i < 0 or i >= m or
                j < 0 or j >=n or grid[i][j] == 0):
                return
            if grid[i][j] == 1:
                
                self.fresh_fruit_ct -= 1
                print(self.fresh_fruit_ct )
                grid[i][j] = 2
                queue.append((i,j)) # list ds


        while (self.fresh_fruit_ct > 0 and queue):
            q_len = len(queue)
            for _ in range(q_len):
                i,j = queue.pop(0)
                traverse(i+1,j)
                traverse(i-1,j)
                traverse(i,j+1)
                traverse(i,j-1)
            time +=1
    
        print(self.fresh_fruit_ct)
        return -1 if self.fresh_fruit_ct > 0 else time
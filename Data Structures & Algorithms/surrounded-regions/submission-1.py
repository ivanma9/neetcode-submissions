class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        obs:
            if region is connected to the edge,
            cant be surrounded.
            if it never touches an edge it can be surrounded,
            cannot mark as we go. only backfill once we know it can reach
            trivial go through ever square,
            and have go through every region
            if region touches an edge. every square thats a O should be an x.
            track visited
            can just label every region with an id
            if any square in region id touches edge rewrite as O
            2 pass and fill if its x or o

            O(mxn )

            start from edge, make sure to visit every possible nod possible that is a o, put into a set of do not mark these as x. keep as o. the rest of the unvisited o -> x
            dfs
            O(mxn)
            '''
        visited = set() # only Os
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >=n or (i,j) in visited or board[i][j] == 'X':
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        m,n = len(board), len(board[0])
        for i in range(n):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[m-1][i] == 'O':
                dfs(m-1,i)
        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        print(visited)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        

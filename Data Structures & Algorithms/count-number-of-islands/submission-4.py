class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            
            if grid[r][c] == '0':
                return
            
            #it's a land
            grid[r][c] = '0'

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for ar, ac in directions:
                dfs(r + ar, c + ac)
            
        
        #traverse all cells in the grids
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count

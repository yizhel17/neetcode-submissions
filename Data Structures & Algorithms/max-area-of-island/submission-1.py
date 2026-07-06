class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_a = 0

        def dfs(ro, co):
            if ro < 0 or ro >= row or co < 0 or co >= col:
                return
            if grid[ro][co] == 0:
                return
            #find another island !
            nonlocal isl
            isl += 1
            grid[ro][co] = 0

            dfs(ro-1, co)
            dfs(ro+1, co)
            dfs(ro, co-1)
            dfs(ro, co+1)
        
        #main

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                #find an island !
                isl = 0
                dfs(r, c) #going through four directions...
                max_a = max(max_a, isl)
        return max_a

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(ro, co):
            if ro < 0 or ro >= row or co < 0 or co >= col:
                return
            if grid[ro][co] == "0":
                return
            
            grid[ro][co] = "0"
            
            #根据题意, 上下左右 检查, 只要发现还是陆地,就继续; 若是海洋,就return
            dfs(ro-1, co) #上
            dfs(ro, co-1) #左
            dfs(ro+1, co) #下
            dfs(ro, co+1) #右







        #main

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "0":
                    continue
                #走到这里,说明此时位置是陆地
                count += 1
                #进行深搜
                dfs(r, c)
        
        return count
        

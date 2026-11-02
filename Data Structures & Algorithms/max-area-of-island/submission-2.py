class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1


            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ]

            for ar, ac in directions:
                area += dfs(r + ar, c + ac)
            
            return area
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area

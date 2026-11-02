from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        你这个疑问非常好，但在这段代码里，第一个 (r, c) 不会是 0，因为我们只会在外层发现陆地时调用 bfs(r, c)。
        """

        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            cur_area = 1

            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ]

            for ar, ac in directions:
                nr = r + ar
                nc = c + ac

                cur_area += dfs(nr, nc)
            
            return cur_area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area

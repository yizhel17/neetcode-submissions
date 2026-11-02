from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        你这个疑问非常好，但在这段代码里，第一个 (r, c) 不会是 0，因为我们只会在外层发现陆地时调用 bfs(r, c)。
        """

        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(r, c):
            que = deque([(r, c)])
            grid[r][c] = 0
            area = 0

            while que:
                row, col = que.popleft()
                area += 1

                directions = [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0)
                ]

                for ar, ac in directions:
                    nr = row + ar
                    nc = col + ac

                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 0
                        que.append((nr, nc))
            return area
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area

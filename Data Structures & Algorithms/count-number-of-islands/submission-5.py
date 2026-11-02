from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def bfs(r, c):
            que = deque([(r, c)])

            #一进queue就标记visited
            grid[r][c] = '0'
            
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            while que:
                row, col = que.popleft()

                for ar, ac in directions:
                    nr = row + ar
                    nc = col + ac

                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and grid[nr][nc] == '1'
                    ):
                        grid[nr][nc] = '0'
                        que.append((nr, nc))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        
        return count


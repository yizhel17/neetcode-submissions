from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])

        INF = 2147483647
        que = deque()

        #collect all treasures coordinates
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    que.append((r,c))
        
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        
        #BFS, nearest
        while que:
            
            ro, co = que.popleft()

            for dr, dc in directions:
                nr = dr + ro
                nc = dc + co

                if nr<0 or nr>=row or nc<0 or nc>=col:
                    continue

                if grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = grid[ro][co] + 1

                que.append((nr, nc))

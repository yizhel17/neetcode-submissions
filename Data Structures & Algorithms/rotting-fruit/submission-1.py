from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS: "one minute" represents "the layer will be effected"
        #BFS : 每一层扩散: queue

        queue = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        #先找到所有rotten fruits
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        #BFS: 一层BFS遍历完, 就加一分钟
        minutes = 0
        #四个方向
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]


        #一次BFS (多个起点同时扩散) Multi-source BFS
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                #扩散
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1#次数为从queue pop出来的次数

                        queue.append((nr, nc))
                
            minutes += 1

        return minutes if fresh == 0 else -1 #有可能1和2被0给隔开了




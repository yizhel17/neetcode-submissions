class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        visited = {}

        def dfs(root):
            # ① 如果已经复制过，直接返回复制好的节点
            if root in visited:
                return visited[root]

            copy = Node(root.val) #copy一个新节点

            visited[root] = copy #建立新旧节点的映射

            for nei in root.neighbors:
                copy.neighbors.append(dfs(nei))  #把neighbors也复制
            
            return copy
        
        return dfs(node)
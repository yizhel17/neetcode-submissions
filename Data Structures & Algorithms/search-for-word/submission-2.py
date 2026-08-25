from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #一看就是 graph, 想到number of islands (上下左右的neighbor)
    
        #但是有一点不同,就是word search 需要在弹栈后还原原来的字母, 而islands里不需要

        m = len(board)
        n = len(board[0])
        
        

        board_f = Counter(

            board[i][j] 
            for i in range(m) 
            for j in range(n)
        )

        word_f = Counter(cha for cha in word)

        #剪枝
        for ch in word_f:
            if word_f[ch] > board_f[ch]:
                return False
        

        #优化: 减少dfs的search起点
        # 从更稀有的字符开始搜索，减少 DFS 起点
        if board_f[word[0]] > board_f[word[-1]]:
            word = word[::-1]


        def dfs(i, j, k):
            #Base case
            if k == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            # 3. choose：暂时标记当前格子
            temp = board[i][j]
            board[i][j] = "#"

            # 4. explore 四个方向
            found = (
                dfs(i + 1, j ,k + 1) or
                dfs(i - 1, j, k + 1) or 
                dfs(i, j + 1, k + 1) or 
                dfs(i, j - 1, k + 1)
            )
            
            # 5. undo choice：恢复
            board[i][j] = temp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False

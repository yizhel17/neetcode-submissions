class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            #到这里说明可以继续往下走
            temp_cha = board[i][j]
            board[i][j] = "#"

            explore = (

                dfs(i + 1, j, k + 1) or  #往下
                dfs(i - 1, j, k + 1) or  #往上
                dfs(i, j + 1, k + 1) or  #往右
                dfs(i, j - 1, k + 1) #往左
        
            )   

            #弹栈时还原
            board[i][j] = temp_cha

            return explore

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False

class Solution:
    def climbStairs(self, n: int) -> int:
        # fir, sec = 1, 1 #bottom-up的形式, 由右到左 推进

        # for i in range(n-1): #根据推导的结论, 还要算出n-1个数,所以还需循环n-1次
        #     temp = fir
        #     fir = fir + sec
        #     sec = temp
        
        # return fir

        # fir = 1 #在第0阶
        # sec = 1 #在第1阶层

        # for i in range(2, n + 1):
        #     temp = fir
        #     fir = sec
        #     sec = temp + sec
        
        # return sec

        dp = [1] * (n + 1)

        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

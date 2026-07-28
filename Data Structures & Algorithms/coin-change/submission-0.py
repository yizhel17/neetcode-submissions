class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0 #无面值为0的硬币

        for i in range(1, amount + 1): #遍历的目标金额从1一路到amount
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1) # +1 代表选了目前这个coin
        
        return dp[amount] if dp[amount] != float('inf') else -1
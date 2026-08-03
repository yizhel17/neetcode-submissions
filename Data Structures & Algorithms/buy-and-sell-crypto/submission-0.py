class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = float("-inf")
        cur_profit = 0
        
        left = 0
        for right in range(left, len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            else:
                maxP = max(maxP, profit)
        
        return maxP

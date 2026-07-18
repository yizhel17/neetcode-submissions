class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        fir = 0  # 代表从 i+2 阶到终点的花费
        sec = 0  # 代表从 i+1 阶到终点的花费
        
        # 你的想法：从后往前倒推
        # 从最后一级台阶 (n-1) 一直倒推到第 0 阶
        for i in range(len(cost) - 1, -1, -1):
            # 离开第 i 阶到终点的总花费 = 这一阶的费用 + min(去下一阶, 去下两阶)
            cur_cost = cost[i] + min(sec, fir)
            
            # 滚动状态
            fir = sec  # 旧的 sec 变成新循环里的 i+2
            sec = cur_cost  # 当前算出的 cur_cost 变成新循环里的 i+1
            
        # 最终，我们可以从第 0 阶开始，也可以从第 1 阶开始。
        # 此时的 sec 代表从第 0 阶出发到终点的最小花费
        # 此时的 fir 代表从第 1 阶出发到终点的最小花费
        return min(sec, fir)
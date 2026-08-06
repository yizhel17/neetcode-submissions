import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-s for s in stones]

        heapq.heapify(new_stones) # In-place modification

        while len(new_stones) >= 2:
            x = heapq.heappop(new_stones)
            y = heapq.heappop(new_stones)

            if x <= y:
                new_weight = x - y # 更小的负数减去更大的负数 = 一个新的负数

                heapq.heappush(new_stones, new_weight)
        
        if new_stones:
            return -new_stones[0]
        else:
            return 0

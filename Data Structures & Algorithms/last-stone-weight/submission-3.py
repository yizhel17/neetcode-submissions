import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #maintain a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones) #heapify: O(n) time

        while len(stones) > 1:
            first_wei = -heapq.heappop(stones)
            sec_wei = -heapq.heappop(stones)

            diff = first_wei - sec_wei

            if diff:
                heapq.heappush(stones,-diff)
            
        if stones:
            return -stones[0]
        else:
            return 0

from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)

        for num in nums:
            my_map[num] += 1
        
        heap = []
        for num, count in my_map.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for count, num in heap:
            ans.append(num)
        
        return ans
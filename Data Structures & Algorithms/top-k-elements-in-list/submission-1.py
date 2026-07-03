from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        my_map = defaultdict(int)

        for num in nums:
            my_map[num] += 1
        
        heap = []
        for val, count in my_map.items():
            heapq.heappush(heap, (count, val))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for count, val in heap:
            ans.append(val)
        
        return ans
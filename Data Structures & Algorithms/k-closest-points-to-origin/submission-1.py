import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 0:
            return [[]]
        
        max_heap = []  #用大根堆
        for x, y in points:
            dist = x**2 + y**2 # sqrt会引来算力大消耗

            heapq.heappush(max_heap, (-dist, [x,y])) #因为最后不仅要知道距离,还要知道具体的坐标

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for _, point in max_heap]

            
    
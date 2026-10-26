import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #maintain a maxheap
        dis = [(x**2 + y**2, x, y)
            for x, y in points
        ]

        heapq.heapify(dis)

        ans = []

        for _ in range(k):
            distance, x, y = heapq.heappop(dis)
            ans.append([x, y])
        
        return ans

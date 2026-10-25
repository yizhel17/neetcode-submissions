import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        #add
        if self.max_heap and num > self.max_heap[0]:
            heapq.heappush(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, -num)
        
        #balance
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)
        


    def findMedian(self) -> float:
        #odd cases
        if len(self.min_heap) > len(self.max_heap):
            return -1 * self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        #even case
        else:
            return (-self.min_heap[0] + self.max_heap[0]) / 2.0

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.th = k
        # self.stream = nums
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        # self.stream.append(val)
        # self.stream.sort()
        # return self.stream[-self.th]
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

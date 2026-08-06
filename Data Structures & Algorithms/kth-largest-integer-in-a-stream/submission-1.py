class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.th = k
        # self.stream = nums
        self.th = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # self.stream.append(val)
        # self.stream.sort()
        # return self.stream[-self.th]
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.th:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

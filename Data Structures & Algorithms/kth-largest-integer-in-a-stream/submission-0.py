class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.th = k
        self.stream = nums

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        return self.stream[-self.th]
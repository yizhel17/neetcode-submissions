class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 0:
            ans = (self.arr[n // 2] + self.arr[n // 2 - 1]) / 2
        else:
            ans = self.arr[n // 2]
        
        return ans
        
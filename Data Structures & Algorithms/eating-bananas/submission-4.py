import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #brute force: time: O(m * n), m: max element of piles; n: the len(piles)
        # speed = 1

        # while True:
        #     total_time = 0

        #     for pile in piles:
        #         total_time += math.ceil(pile / speed)

        #     if total_time <= h:
        #         return speed
        #     speed += 1
        
        # return speed



        #Binary search
        # total_num = 
        # check() : _?> find the first k that makes the check() True
        def canFinish(speed):
            total_t = 0

            for pile in piles:
                total_t += math.ceil(pile / speed)
            
            return total_t <= h
    

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

        #time: O(n * logM)

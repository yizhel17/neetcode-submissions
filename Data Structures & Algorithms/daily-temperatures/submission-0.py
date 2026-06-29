class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        new_lst = [0] * len(temperatures)

        l = 0
        while l < len(temperatures):
            for r in range(l, len(temperatures)):
                if temperatures[r] > temperatures[l]:
                    new_lst[l] = r - l
                    break
            l += 1
        
        return new_lst

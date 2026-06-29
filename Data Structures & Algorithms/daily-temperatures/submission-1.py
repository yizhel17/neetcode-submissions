class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        new_lst = [0] * len(temperatures) #先要建立索引, 不然后面会有index问题

        l = 0
        while l < len(temperatures):
            for r in range(l, len(temperatures)):
                if temperatures[r] > temperatures[l]:
                    new_lst[l] = r - l
                    break
            l += 1
        
        return new_lst

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures) #先要建立索引, 不然后面会有index问题

        # l = 0
        # while l < len(temperatures):
        #     for r in range(l, len(temperatures)):
        #         if temperatures[r] > temperatures[l]:
        #             new_lst[l] = r - l
        #             break
        #     l += 1
        
        # return new_lst

        # 单调栈 optimal solution
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_i = stack.pop()
                ans[pre_i] = i - pre_i
            
            stack.append(i)
        
        return ans


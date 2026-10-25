class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = [0] * len(temperatures)

        # for i in range(len(temperatures)):
        #     cur_temp = temperatures[i]
        #     cur_ind = i
        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j - i
        #             break
                
        #         j += 1
        
        # return ans

        mono_stack = [] #存index,days -> length

        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while mono_stack and temp > temperatures[mono_stack[-1]]:
                pre_ind = mono_stack.pop()
                ans[pre_ind] = i - pre_ind
            
            mono_stack.append(i)
        
        return ans

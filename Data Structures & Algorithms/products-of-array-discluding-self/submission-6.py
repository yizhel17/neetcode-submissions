class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        mul = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                mul *= num
        
        if zero_count > 1:
            return [0] * len(nums)
        
        #zero_count 要么是0, 要么是1
        ans = [0] * len(nums)
        for i, val in enumerate(nums):
            if zero_count == 1:
                if val != 0:
                    ans[i] = 0
                else:
                    ans[i] = mul
            else:
                ans[i] = mul // val
        
        return ans

class Solution:
    def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) <= 1:
    #         return nums[0]
    #     if len(nums) <= 2:
    #         return max(nums[0], nums[1])
        
    #     def rob_I(nums):
    #         dp = [0] * len(nums)

    #         dp[0] = nums[0]
    #         dp[1] = max(nums[0], nums[1])

    #         for i in range(2, len(nums)):
    #             dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
    #         return dp[-1]
        
        # return max(rob_I(nums[0:len(nums) - 1]), rob_I(nums[1:]))

    
    #也可以通过更新变量把空间复杂度降低到O(1),请看下解
        if len(nums) == 0:
            return 0
        if len(nums) <= 1:
            return nums[0]
        if len(nums) <= 2:
            return max(nums[0], nums[1])

        def rob_I(nums):
            fir = 0
            sec = 0
            
            for num in nums:
                fir, sec = sec, max(fir + num, sec)
    
            return sec
        
        return max(rob_I(nums[:-1]), rob_I(nums[1:]))

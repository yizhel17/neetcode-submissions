class Solution:
    def rob(self, nums: List[int]) -> int:
        #First step: Define the meaning of the DP array and the index:
        dp = [0] * len(nums)
        #dp array is defined by myself. 
        #This DP array keeps track of the "Maximum" Amount of Money from the houses I can rob.
        
        #边界条件处理
        if not nums:
            return 0
        if len(nums) <= 1:
            return nums[0]
        
        # dp[i] represents the max amount I will be gained including all the houses possible
        # dp[i] has two singly status: Robbed/ Not Robbed
        
        #Status1: If it has been robbed, the amount is (dp[i-2] + nums[i])
        #Status2: If it hasn't been robbed, the amount is (dp[i-1])

        #Second Step: 推导出 递推公式
        #So the formula will be the following one (!!!Make the MAX out of two status!!!):
        #FORMULA: dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        #Third Step: 初始化DP数组及确定base case(s)
        #根据递推公式 来 DP数组初始化(initialize), confirm the base case(s), and set their values.
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        #Step 4: 确定遍历顺序, 更新DP数组 (从小到大, 这样才能确保用到我们定义的前面两个base cases)
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = nums[0]
        cur_s = 0
        
        for num in nums:
            cur_s += num

            max_s = max(max_s, cur_s)

            if cur_s < 0:
                cur_s = 0
            
        return max_s
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]

        for i in range(len(nums)):
            cur = nums[i]
            ans = max(ans, cur)

            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                ans = max(ans, cur)
        
        return ans
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []

        def bck(st, cur_sum):
            if cur_sum == target:
                ans.append(cur[:])
                return
            
            if cur_sum > target:
                return 
            
            for i in range(st, len(nums)):
                cur.append(nums[i])

                bck(i, cur_sum + nums[i])

                cur.pop()
            
        bck(0, 0)

        return ans
            
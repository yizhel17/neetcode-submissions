class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        
        def bck(start, cur_num):
            if cur_num == target:
                ans.append(cur[:])
                return
            
            if cur_num > target:
                return
            
            for i in range(start, len(nums)):
                cur.append(nums[i])
                bck(i, cur_num + nums[i])
                cur.pop()
        
        
        bck(0, 0)

        return ans
            
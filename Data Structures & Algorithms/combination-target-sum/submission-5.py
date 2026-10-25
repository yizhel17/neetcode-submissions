class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(cur_ind, cur, total):
            if total == target:
                ans.append(cur[:])
                return
            if cur_ind >= len(nums) or total > target:
                return
            
            cur.append(nums[cur_ind])
            total += nums[cur_ind]
            dfs(cur_ind, cur, total)

            cur.pop()
            total -= nums[cur_ind]

            dfs(cur_ind + 1, cur, total)
        
        dfs(0, [], 0)
        
        return ans

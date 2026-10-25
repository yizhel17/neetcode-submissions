class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(cur_ind, cur, total):
            if total == target:
                ans.append(cur[:])
                return

            
            for j in range(cur_ind, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)

        return ans

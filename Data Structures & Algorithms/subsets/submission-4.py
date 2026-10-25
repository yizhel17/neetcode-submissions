class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, cur):
            if i == len(nums):
                ans.append(cur[:])
                return
                
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()

            dfs(i + 1, cur)

        dfs(0, [])

        return ans

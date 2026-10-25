class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, cur):
            if i == len(nums):
                ans.append(cur[:])
                return
                
            #skip the cur element
            dfs(i + 1, cur)

            #Not skip
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
        
        dfs(0, [])

        return ans

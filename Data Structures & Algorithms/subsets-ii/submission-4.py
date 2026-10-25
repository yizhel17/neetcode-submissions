class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        cur = []
        nums.sort()

        def backtracking(i):
            if i >= len(nums):
                return
            
            cur.append(nums[i])
            ans.append(cur[:])

            backtracking(i + 1)

            cur.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            backtracking(i + 1)

            
        backtracking(0)

        return ans
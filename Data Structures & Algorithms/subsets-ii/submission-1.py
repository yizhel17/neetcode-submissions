class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        def backtracking(st, cur):
            ans.append(cur[:])

            for i in range(st, len(nums)):
                if i > st and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                backtracking(i + 1, cur)
                cur.pop()

            
        backtracking(0, [])

        return ans
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        def backtracking(i):
            ans.append(cur[:])

            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtracking(j+1)
                cur.pop()
        
        backtracking(0)

        return ans
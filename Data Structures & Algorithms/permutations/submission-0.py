class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        def back():
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for num in nums:
                if num not in cur:
                    cur.append(num)
                    back()
                    cur.pop()
        
        back()

        return ans

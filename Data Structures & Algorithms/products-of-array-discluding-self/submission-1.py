class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        postf = [0] * n

        pref[0] = postf[n - 1] = 1

        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1): #倒序
            postf[i] = postf[i + 1] * nums[i+1]
        for i in range(n):
            res[i] = pref[i] * postf[i]

        return res

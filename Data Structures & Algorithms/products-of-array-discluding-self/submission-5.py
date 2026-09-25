class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n
        
        # #最优解,直接在res上更新
        # prefix = 1 #可以不用数组来占用内存

        # for i in range(n):
        #     res[i] = prefix
        #     prefix *= nums[i]
        
        # postfix = 1
        # for i in range(n-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        
        # return res

        n = len(nums)
        ans = [0] * n

        #prefix, the product of the elements on the left of the self element
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        #postfix
        postfix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy: 维护目前能到的最远的index
        farthest = 0

        for i in range(len(nums)):

            #如果连index i都到不了,那么后面的index更不可能到
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])
        
        return True

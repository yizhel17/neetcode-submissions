class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            if not nums:
                return -1
            elif nums[0] == target:
                return 0
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2

            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:#说明左半边sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1 #避免卡死
            else:#右半边sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

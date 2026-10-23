class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #time: O(logN)
        #Space: O(1)

        left = 0
        right = len(nums) - 1

        while left <= right:
            # (l + r) // 2 can lead to overflow
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
 
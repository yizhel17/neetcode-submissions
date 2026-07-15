class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                ans = [l + 1, r + 1]
                return ans
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
        return ans
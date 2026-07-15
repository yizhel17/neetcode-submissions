class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0

        l = 0
        r = len(heights) - 1
        max_a = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_a = max(area, max_a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_a

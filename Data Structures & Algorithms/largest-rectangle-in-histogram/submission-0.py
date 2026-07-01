class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        #为了让 单调递增 栈 里残留的元素都可以被弹出, 不然无法进入到while中进行面积计算
        heights = heights + [0]
        #用索引更好计算宽度
        for i in range(len(heights)):
            num = heights[i]

            while stack and num < heights[stack[-1]]: #单调 递增 趋势被打破
                h = heights[stack.pop()]

                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                
                max_area = max(max_area, h * w)
            
            stack.append(i) #单增 趋势 保持
        
        return max_area

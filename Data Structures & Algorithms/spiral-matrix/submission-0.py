class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        top = 0
        left = 0
        bottom = len(matrix)
        right = len(matrix[0])

        while top < bottom and left < right:
            #left -> right
            for col in range(left, right):
                ans.append(matrix[top][col])
            top += 1

            #top -> bottom
            for row in range(top, bottom):
                ans.append(matrix[row][right - 1])
            right -= 1

            if top < bottom and left < right:

                #right -> left
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom - 1][col])
                bottom -= 1
                
                #bottom -> top
                for row in range(bottom - 1, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1
        
        return ans

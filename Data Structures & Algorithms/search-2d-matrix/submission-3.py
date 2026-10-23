class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            cur = matrix[mid // n][mid % n]

            if cur == target:
                return True
            elif cur < target:
                left += 1
            else:
                right -= 1
        
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            M = matrix[mid][0]
            if target == M:
                return True
            elif target > M:
                l = mid + 1
            else:
                r = mid - 1

        n = len(matrix[0]) - 1
        left = 0
        right = n 
        
        while left <= right:
            m = (left + right) // 2
            MID = matrix[r][m]
            if target == MID:
                return True
            elif target > MID:
                left = m + 1
            else:
                right = m - 1
        
        return False


        
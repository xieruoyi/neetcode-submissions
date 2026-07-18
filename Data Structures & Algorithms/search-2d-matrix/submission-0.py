class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = 0
        row_r = len(matrix) - 1
        group = -1
        while row_l <= row_r:
            row_m = int((row_l + row_r)/2)
            if target >= matrix[row_m][0] and target <= matrix[row_m][-1]:
                group = row_m
                break
            elif target < matrix[row_m][0]:
                row_r = row_m - 1
            elif target > matrix[row_m][-1]:
                row_l = row_m + 1

        if group == -1:
            return False
        
        l = 0
        r = len(matrix[0])-1
        while l <= r:
            mid = int((l+r)/2)
            if target == matrix[group][mid]:
                return True
            elif target > matrix[group][mid]:
                l = mid + 1
            elif target < matrix[group][mid]:
                r = mid - 1

        return False
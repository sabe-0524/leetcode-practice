from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        
        while left < right:
            middle = (left + right) // 2
            if matrix[middle][0] < target:
                left = middle + 1
            else:
                right = middle
        
        row = left
        
        left = 0
        right = len(matrix[row]) - 1
        
        while left < right:
            middle = (left + right) // 2
            if matrix[row][middle] < target:
                left = middle + 1
            else:
                right = middle
        
        return matrix[row][left] == target
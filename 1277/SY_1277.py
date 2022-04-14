class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(1, nrow):
            for j in range(1, ncol):
                matrix[i][j] = (min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1) if matrix[i][j] == 1 else 0
        
        flattened = sum(matrix, [])
        return sum(flattened)
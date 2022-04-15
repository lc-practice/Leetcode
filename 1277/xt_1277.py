class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        m = len(matrix)
        n = len(matrix[1])
        
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    if matrix[i][j] != 0:
                        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                ans += matrix[i][j]
                
        return ans

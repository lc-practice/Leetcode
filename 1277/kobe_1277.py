class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        column = len(matrix[0])
        for i in range(1,row):
            for j in range(1,column):
                if matrix[i][j] == 1:
                    if min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) > 0:
                        matrix[i][j] += min([matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]])
        return sum(map(sum,matrix))
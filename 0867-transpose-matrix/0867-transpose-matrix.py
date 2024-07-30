class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        col = len(matrix[0])
        transposed = [[0 for _ in range(rows)] for _ in range(col)]
        for i in range(0, rows):
            for j in range(0, col):
                transposed[j][i] = matrix[i][j]
        return transposed
        
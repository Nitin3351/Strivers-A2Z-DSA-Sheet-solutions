class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Find transpose of the matrix
        for i in range(n):
            for j in range(0,i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse every row of transpose matrix to get 90 degrees clockwise rotated matrix
        for i in range(n):
            matrix[i]= matrix[i][::-1]
        return

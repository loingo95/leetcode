class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # calculate sum of rows, and col
        # since this matrix only have one and zero
        # nrof ones is sum, nrof zeroes is row/col length - their sum

        import numpy as np

        grid = np.array(grid)
        rows, cols = grid.shape
        diff = np.zeros((rows, cols), dtype=int)

        rows_sum = [sum(grid[i,:]) for i in range(rows)]
        cols_sum = [sum(grid[:,j]) for j in range(cols)]

        for i in range(rows):
            for j in range(cols):
                diff[i, j] = rows_sum[i] + cols_sum[j] - (rows - rows_sum[i]) - (cols - cols_sum[j])

        return diff

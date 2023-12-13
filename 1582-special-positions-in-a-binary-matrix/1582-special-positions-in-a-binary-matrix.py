class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        import numpy

        mat = numpy.array(mat)
        rows, cols = mat.shape
        row_sum = [sum(mat[i,:]) for i in range(rows)]
        col_sum = [sum(mat[:,j]) for j in range(cols)]


        nrof_special_position = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i, j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    nrof_special_position += 1

        return nrof_special_position

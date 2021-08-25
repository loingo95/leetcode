class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        using divine and conquer: divine the matrix intro 4 sub matrix base on a pivot,
        pivot=middle point of matrix, if target == pivot -> True,
        if target < pivot then we can eliminate bottom right matrix ( which reduce the search space),
        if target > pivot then we can eliminate the top left matrix
        '''
        # print(matrix)
        total_elements = sum([len(row) for row in matrix])
        if total_elements == 0:
            return False
        elif total_elements == 1 and matrix[0][0] != target:
            return False
        
        pidx = (len(matrix)//2, len(matrix[0])//2)
        pivot = matrix[pidx[0]][pidx[1]]
        print(matrix, pidx, pivot)
        
        
        if target == pivot:
            return True
        
        if target < pivot:
            tl_matrix = [row[:pidx[1]] for row in matrix[:pidx[0]]]
            tr_matrix = [row[pidx[1]:] for row in matrix[:pidx[0]]]
            bl_matrix = [row[:pidx[1]] for row in matrix[pidx[0]:]]
            # print(tl_matrix, tr_matrix, bl_matrix)
            
            return self.searchMatrix(tl_matrix, target) \
                    or self.searchMatrix(tr_matrix, target) \
                    or self.searchMatrix(bl_matrix, target)
            
        elif target > pivot:
            tr_matrix = [row[pidx[1]:] for row in matrix[:pidx[0]]]
            bl_matrix = [row[:pidx[1]] for row in matrix[pidx[0]:]]
            br_matrix = [row[pidx[1]:] for row in matrix[pidx[0]:]]
            # print(br_matrix, tr_matrix, bl_matrix)
            
            return self.searchMatrix(br_matrix, target) \
                    or self.searchMatrix(tr_matrix, target) \
                    or self.searchMatrix(bl_matrix, target)
            
            
        
class Solution:
    pascal_triangle = []
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            if len(self.pascal_triangle) == 0:
                self.pascal_triangle.append([1])
            return self.pascal_triangle[0]
        
        self.getRow(rowIndex-1)
        
        row_val = [1]*(rowIndex+1)
        for col_idx in range(1, rowIndex):
            row_val[col_idx] = self.pascal_triangle[rowIndex-1][col_idx-1]+ \
            self.pascal_triangle[rowIndex-1][col_idx]
        
        if len(self.pascal_triangle) == rowIndex:
            self.pascal_triangle.append(row_val)

        return row_val
        
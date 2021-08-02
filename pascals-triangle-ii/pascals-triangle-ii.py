class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex - 1)
        
        row_val = [1] * (rowIndex + 1)
        for col_idx in range(1, rowIndex):
            row_val[col_idx] = prev[col_idx - 1]+ prev[col_idx]
        
        return row_val
        
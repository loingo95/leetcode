class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queens = []
        boards = []
        
        def generate_board(queens):
            board = [['.']*n for i in range(n)]
            for qrow, qcol in queens:
                board[qrow][qcol] = 'Q'
            boards.append([''.join(row) for row in board])
                
        def is_not_under_attack(row, col):
            for qrow, qcol in queens:
                if (row == qrow) or \
                   (col == qcol) or \
                   (row - col) == (qrow - qcol) or \
                   (row + col) == (qrow + qcol):
                    return False
            return True
        
        def backtracking(row):
            if row == n:
                # generate queens board
                generate_board(queens)
                return

            for col in range(n):
                if is_not_under_attack(row, col):
                    queens.append((row, col))
                    # since 1 col only allow 1 Queen, so we move to next
                    backtracking(row+1)
                    queens.pop()
                    
            
        backtracking(0)
        return boards
        
        
        
        
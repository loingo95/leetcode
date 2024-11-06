class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        max_idx = len(board)

        def place_number(board, x_idx, y_idx, num):
            board[x_idx][y_idx] = str(num)

        def remove_number(board, x_idx, y_idx):
            board[x_idx][y_idx] = '.'

        def _flat_sub_box(board, x_pos, y_pos):
            x_start = (x_pos // 3) * 3
            y_start = (y_pos // 3) * 3
            sub_box = [board[row_idx][col_idx] for row_idx in range(x_start, x_start+3) for col_idx in range(y_start, y_start+3)]
            return sub_box

        def is_valid(board, x_pos, y_pos, num):
            # Check each of the digits 1-9 must occur exactly once in each row.
            if num in board[x_pos]:
                return False
            # Check each of the digits 1-9 must occur exactly once in each col.
            if num in [board[row_idx][y_pos] for row_idx in range(max_idx)]:
                return False
            # Check each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
            if num in _flat_sub_box(board, x_pos, y_pos):
                return False

            return True

        def backtrack_sudoku(board, x_pos, y_pos):
            if x_pos == max_idx:
                return True
            if y_pos == max_idx:
                return backtrack_sudoku(board, x_pos + 1, 0)

            if board[x_pos][y_pos] == '.':
                for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if is_valid(board, x_pos, y_pos, num):
                        place_number(board, x_pos, y_pos, num)
                        if backtrack_sudoku(board, x_pos, y_pos + 1):
                            return True
                        else:
                            remove_number(board, x_pos, y_pos)
                return False
            else:
                return backtrack_sudoku(board, x_pos, y_pos + 1)


        backtrack_sudoku(board, 0, 0)
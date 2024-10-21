class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col, queens):
            for qrow, qcol in queens:
                if (row == qrow) or \
                   (col == qcol) or \
                   (row - col) == (qrow - qcol) or \
                   (row + col) == (qrow + qcol):
                    return False
            return True

        def place_queen(row, col, queens):
            queens.append((row, col))
            return queens

        def remove_queen(queens):
            queens.pop()
            return queens

        def backtrack_nqueen(row, queens, count):
            for col in range(n):
                # Check current position
                if is_not_under_attack(row, col, queens):
                    queens = place_queen(row, col, queens)
                    # Check if we reach the final row, if yes then we found a solution
                    if row + 1 == n:
                        count += 1
                    # If not, we proceed to next row
                    else:
                        count = backtrack_nqueen(row + 1, queens, count)
                    # Now after we done finding all the count above, we remove this queen so we can go to the next candidate
                    queens = remove_queen(queens)
            return count

        return backtrack_nqueen(0, [], 0)
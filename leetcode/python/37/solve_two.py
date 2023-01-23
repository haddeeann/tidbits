class Solution(object):
    def setupBoard(self, row):
        row_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for number in row:
            if number != '.':
                row_set.remove(number)
        for i, dots in enumerate(row):
            if dots == '.':
                row[i] = row_set.copy()
        return row

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i, row in enumerate(board):
            board[i] = self.setupBoard(row)

        print(board)


input = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sol = Solution()
sol.solveSudoku(input)

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

    def checkColumns(self, col, board):
        remove_list = []
        for row in range(9):
            if isinstance(board[row][col], str):
                remove_list.append(board[row][col])
        # print(remove_list)
        for row in range(9):
            if isinstance(board[row][col], set):
                for r in remove_list:
                    board[row][col].discard(r)
                # print(board[row][col])

    def checkRows(self, row, board):
        remove_list = []
        for k in range(9):
            # print(board[row][k])
            if isinstance(board[row][k], str):
                # print(board[row][k])
                remove_list.append(board[row][k])
        # print(remove_list)
        for l in range(9):
            if isinstance(board[row][l], set):
                for r in remove_list:
                    board[row][l].discard(r)

    def checkBoxes(self, left, right, top, bottom, board):
        # left and right are col, top and bottom are rows
        step_top = top
        remove_list = []
        while step_top < bottom:
            step_left = left
            while step_left < right:
                print(f"row {step_top}: {board[step_top][step_left]}")
                if isinstance(board[step_top][step_left], str):
                    remove_list.append(board[step_top][step_left])
                step_left += 1
            step_top += 1

        step_top = top
        while step_top < bottom:
            step_left = left
            while step_left < right:
                print(f"row {step_top}: {board[step_top][step_left]}")
                if isinstance(board[step_top][step_left], set):
                    for r in remove_list:
                        board[step_top][step_left].discard(r)
                step_left += 1
            step_top += 1

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i, row in enumerate(board):
            board[i] = self.setupBoard(row)

        for j in range(9):
            self.checkColumns(j, board)

        for k in range(9):
            # print(board[j])
            self.checkRows(k, board)

        left = 0
        right = 3
        top = 0
        bottom = 3
        self.checkBoxes(left, right, top, bottom, board)

        for k in range(9):
            print(board[k])


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

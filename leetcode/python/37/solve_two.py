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

    def checkColumnsRows(self, top, board):
        top_remove_list = []
        bottom_remove_list = []
        for bottom in range(9):
            if isinstance(board[bottom][top], str):
                top_remove_list.append(board[bottom][top])
            if isinstance(board[top][bottom], str):
                bottom_remove_list.append(board[top][bottom])

        for bottom in range(9):
            if isinstance(board[bottom][top], set):
                for r in top_remove_list:
                    board[bottom][top].discard(r)
                if len(board[bottom][top]) == 1:
                    board[bottom][top] = next(iter(board[bottom][top]))
            if isinstance(board[top][bottom], set):
                for r in bottom_remove_list:
                    board[top][bottom].discard(r)
                if len(board[top][bottom]) == 1:
                    board[top][bottom] = next(iter(board[top][bottom]))

    def checkBoxes(self, left, right, top, bottom, board):
        # left and right are col, top and bottom are rows
        step_top = top
        remove_list = []
        while step_top < bottom:
            step_left = left
            while step_left < right:
                if isinstance(board[step_top][step_left], str):
                    remove_list.append(board[step_top][step_left])
                step_left += 1
            step_top += 1

        step_top = top
        while step_top < bottom:
            step_left = left
            while step_left < right:
                if isinstance(board[step_top][step_left], set):
                    for r in remove_list:
                        board[step_top][step_left].discard(r)
                    if len(board[step_top][step_left]) == 1:
                        board[step_top][step_left] = next(iter(board[step_top][step_left]))

                step_left += 1
            step_top += 1

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i, row in enumerate(board):
            board[i] = self.setupBoard(row)

        solved = False

        while not solved:
            # search the columns and rows
            for j in range(9):
                self.checkColumnsRows(j, board)

            # search the grid
            top = 0
            bottom = 3
            while bottom < 10:
                left = 0
                right = 3
                while right < 10:
                    self.checkBoxes(left, right, top, bottom, board)
                    left += 3
                    right += 3
                top += 3
                bottom += 3

            solved = True
            for row in board:
                for col in row:
                    if isinstance(col, set):
                        solved = False

        for row in board:
            print(row)
        return board


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

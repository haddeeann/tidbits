class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        columns = []
        grids = []
        rows = []
        q = ["","","","","","","","",""]
        for r in range(9):
            columns.append(q.copy())
            grids.append(q.copy())
            rows.append(q.copy())
        for i, row in enumerate(board):
            temp_row = q.copy()
            row_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            row_index = []
            for j, col in enumerate(row):
                if col != ".":
                    row_set.remove(col)
                    temp_row[j] = col
                elif col == ".":
                    row_index.append(j)
            for r in row_index:
                temp_row[r] = row_set.copy()
            rows.append(temp_row)


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

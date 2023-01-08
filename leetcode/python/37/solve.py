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
            columns.append([])
            grids.append([])
        for i, row in enumerate(board):
            temp_row = q.copy()
            row_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            row_index = []
            for j, col in enumerate(row):
                if col != ".":
                    row_set.remove(col)
                    temp_row[j] = col
                    columns[j].append(col)
                    if j < 3:
                        if i < 3:
                            grids[0].append(col)
                        elif i < 6:
                            grids[1].append(col)
                        elif i < 9:
                            grids[2].append(col)
                    elif j < 6:
                        if i < 3:
                            grids[3].append(col)
                        elif i < 6:
                            grids[4].append(col)
                        elif i < 9:
                            grids[5].append(col)
                    elif j < 9:
                        if i < 3:
                            grids[6].append(col)
                        elif i < 6:
                            grids[7].append(col)
                        elif i < 9:
                            grids[8].append(col)
                elif col == ".":
                    row_index.append(j)
            for r in row_index:
                temp_row[r] = row_set.copy()
            rows.append(temp_row)
        #     print(temp_row)
        # print("------")
        # print(columns)
        # print("------")
        for r in range(9):
            for s in range(9):
                see = rows[s][r]
                if isinstance(see, set):
                    for t in columns[r]:
                        rows[s][r].discard(t)
        # for row in rows:
        #     print(row)

        print(grids)

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

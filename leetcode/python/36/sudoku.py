class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = []
        grids = []
        for r in range(9):
            columns.append([])
            grids.append([])
        for i, row in enumerate(board):
            add_row = []
            for j, col in enumerate(row):
                if col != ".":
                    if col in add_row or col in columns[j]:
                        return False

                    add_row.append(col)
                    columns[j].append(col)
                    if j < 3:
                        if i < 3:
                            if col in grids[0]:
                                return False
                            else:
                                grids[0].append(col)
                        elif i < 6:
                            if col in grids[1]:
                                return False
                            else:
                                grids[1].append(col)
                        elif i < 9:
                            if col in grids[2]:
                                return False
                            else:
                                grids[2].append(col)
                    elif j < 6:
                        if i < 3:
                            if col in grids[3]:
                                return False
                            else:
                                grids[3].append(col)
                        elif i < 6:
                            if col in grids[4]:
                                return False
                            else:
                                grids[4].append(col)
                        elif i < 9:
                            if col in grids[5]:
                                return False
                            else:
                                grids[5].append(col)
                    elif j < 9:
                        if i < 3:
                            if col in grids[6]:
                                return False
                            else:
                                grids[6].append(col)
                        elif i < 6:
                            if col in grids[7]:
                                return False
                            else:
                                grids[7].append(col)
                        elif i < 9:
                            if col in grids[8]:
                                return False
                            else:
                                grids[8].append(col)
        return True

board_a = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
tests = [{
    "input": board_a,
    "answer": True,
}]

sol = Solution()
for t in tests:
    answer = sol.isValidSudoku(t["input"])
    if answer == t["answer"]:
        print("passed the test")
    else:
        print("did not pass the test")
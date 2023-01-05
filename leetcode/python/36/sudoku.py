class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = []
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        for r in range(9):
            columns.append(letters.copy())
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                columns[j][i] = col
        print(columns)
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
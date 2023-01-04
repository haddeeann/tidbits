class Solution(object):
    def testRow(self, row):
        row_list = []
        for r in row:
            if r in row_list and r != ".":
                return False
            elif r != ".":
                row_list.append(r)
        return True


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = []
        for row in board:
            row_truth = self.testRow(row)

        for column in columns:
            print('hi')

board_a = [["5","3","5",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
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
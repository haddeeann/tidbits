class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        print(board)


tests = [{
    "input": "",
    "answer": "",
}]

sol = Solution()
for t in tests:
    sol.isValidSudoku(t["input"])
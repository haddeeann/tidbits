class Solution(object):
    def outsideIn(self, str, n, pair, l_box, r_box):
        for i in range(1):
            str += l_box
            str = self.sideBySide(str, n - 1, pair)
            str += r_box
        return str

    def sideBySide(self, str, t, pair):
        for i in range(t):
            for p in pair:
                str += p
        return str

    def innerParen(self, str, t, pair):
        for p in pair:
            for i in range(t):
                str += p
        return str

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # pairs
        l_box = "("
        r_box = ")"
        pair = [l_box, r_box]

        right = 0
        while right < n:
            c = ""
            left = n - right
            c = self.innerParen(c, left, pair)

            d = ""
            d = self.sideBySide(d, right, pair)
            print(c + d)
            if right != 0 and left != 1:
                print(d + c)
            right += 1


sol = Solution()
sol.generateParenthesis(5)
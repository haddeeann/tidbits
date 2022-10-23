class Solution(object):
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
        a = self.innerParen("", 3, pair)
        print(a)

        b = ""
        for i in range(1):
            b += l_box
            b = self.sideBySide(b, 2, pair)
            b += r_box
        print(b)

        c = ""
        c = self.innerParen(c, 2, pair)
        c = self.innerParen(c, 1, pair)
        print(c)

        d = ""
        d = self.innerParen(d, 1, pair)
        d = self.innerParen(d, 2, pair)
        print(d)



sol = Solution()
sol.generateParenthesis(3)
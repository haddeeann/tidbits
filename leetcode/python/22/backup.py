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
        # a = self.innerParen("", n, pair)
        # print(a)

        count = n
        c = ""
        c = self.innerParen(c, count, pair)
        print(c)

        # d = ""
        # count = 0
        # while count < n - 1:
        #     count += 1
        #     d = self.innerParen(d, count, pair)
        # print(d)

        # b = self.outsideIn("", n, pair, l_box, r_box)
        # print(b)



sol = Solution()
sol.generateParenthesis(2)
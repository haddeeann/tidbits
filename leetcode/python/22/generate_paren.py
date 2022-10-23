class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # pairs
        l_box = "("
        r_box = ")"
        a = ""
        pair = [l_box, r_box]
        for p in pair:
            for i in range(n):
                a += p
        print(a)
        b = ""
        for i in range(1):
            b += l_box
            for j in range(2):
                for p in pair:
                    b += p
            b += r_box
        print(b)
sol = Solution()
sol.generateParenthesis(3)
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

    def insertInner(self, outer, inner):
        half = int(len(outer) / 2)
        left = outer[:half]
        right = outer[half:]
        return left + inner + right

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # pairs
        l_box = "("
        r_box = ")"
        pair = [l_box, r_box]
        inner = n - 1
        answer = []
        while inner >= 2:
            outer = n - inner

            outer_paren = self.innerParen("", outer, pair)
            inner_paren = self.sideBySide("", inner, pair)
            e = self.insertInner(outer_paren, inner_paren)
            answer.append(e)
            inner -= 1

        right = 0
        while right < n:
            c = ""
            left = n - right
            c = self.innerParen(c, left, pair)

            d = ""
            d = self.sideBySide(d, right, pair)
            answer.append(c + d)
            if right != 0 and left != 1:
                answer.append(d + c)
            right += 1
        return answer


sol = Solution()
guess = sol.generateParenthesis(4)
print(guess)
answer = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
print(answer)
a_set = set()
for a in answer:
    found = False
    for x in guess:
        if a == x:
            found = True
    if not found:
        a_set.add(a)
print(a_set)
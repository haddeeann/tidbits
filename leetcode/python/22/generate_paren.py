class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    str_answer = "".join(A)
                    ans.append(str_answer)
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1

                if bal < 0:
                    return False
            return_balance = bal == 0
            if return_balance:
                print('hi')
            return return_balance

        ans = []
        generate()
        return ans


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
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 1*n:
                str_answer = "".join(A)
                ans.append(str_answer)
            else:
                A.append('*')
                print("append *", A)
                generate(A)
                print("gnerate ", A)
                A.pop()
                print(A, "after")
                A.append("$")
                generate(A)
                A.pop()

        ans = []
        generate()
        return ans


sol = Solution()
guess = sol.generateParenthesis(2)
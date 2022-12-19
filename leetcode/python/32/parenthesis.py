class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        c = 0
        while c < len(s):
            balance = ""
            build = ""
            splice = s[c:]
            for p in splice:
                if p == ")":
                    if balance == "":
                        break
                    else:
                        balance = balance[1:]
                        build += ")"
                        if balance == "" and len(build) > max_count:
                            max_count = len(build)
                elif p == "(":
                    balance += "("
                    build += "("
            c += 1
        return max_count


tests = [
    # {
    #     "input": ")()())",
    #     "answer": 4,
    # },
    {
        "input": "()(()",
        "answer": 2,
    },
    {
        "input": "(()",
        "answer": 2,
    },
    # {
    #     "input": ")()())",
    #     "answer": 4
    # },
    # {
    #     "input": "()(())",
    #     "answer": 6
    # },
    # {
    #     "input": "(())(",
    #     "answer": 4
    # }
]
sol = Solution()
for t in tests:
    answer = sol.longestValidParentheses(t["input"])
    if answer == t["answer"]:
        print("tests pass")
    else:
        print("FAIL", answer)
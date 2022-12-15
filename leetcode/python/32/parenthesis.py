class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        c = 0
        pending = ""
        while c < len(s):
            splice = s[c:]
            balance = 0
            build = ""
            for p in splice:
                if p == ")":
                    balance -= 1
                    if balance < 0:
                        break
                    else:
                        build += pending
                        build += ")"
                        pending = ""
                elif p == "(":
                    pending += "("
                    balance += 1
            if len(build) > max_count:
                max_count = len(build)
            c += 1
        return max_count


tests = [
    {
        "input": ")()())",
        "answer": 4,
    },
    {
        "input": "()(()",
        "answer": 2,
    },
    {
        "input": "(()",
        "answer": 2,
    },
    {
        "input": ")()())",
        "answer": 4
    },
    {
        "input": "()(())",
        "answer": 6
    },
    {
        "input": "(())(",
        "answer": 4
    }
]
sol = Solution()
for t in tests:
    answer = sol.longestValidParentheses(t["input"])
    if answer == t["answer"]:
        print("tests pass")
    else:
        print("FAIL", answer)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        c = 0
        pending_left = ""
        pending_right = ""
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
                        pending_right += ")"
                        if len(pending_left) == len(pending_right):
                            build += pending_left
                            build += pending_right
                            pending_left = ""
                            pending_right = ""
                elif p == "(":
                    pending_left += "("
                    balance += 1
            if len(build) > max_count:
                max_count = len(build)
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
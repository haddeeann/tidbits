class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        c = 0
        while c < len(s):
            splice = s[c:]
            balance = 0
            count = 0
            build = ""
            for p in splice:
                if p == ")":
                    balance -= 1
                    if balance != 0:
                        break
                    else:
                        build += ")"
                        count += 2
                        if count > max_count:
                            max_count = count
                elif p == "(":
                    build += "("
                    balance += 1
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
    }
]
sol = Solution()
for t in tests:
    answer = sol.longestValidParentheses(t["input"])
    if answer == t["answer"]:
        print("tests pass")
    else:
        print("FAIL", answer)
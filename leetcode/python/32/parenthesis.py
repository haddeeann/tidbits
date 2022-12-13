class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        build = ""
        count = 0
        max_count = 0
        for p in s:
            if p == ")":
                balance -= 1
                if balance != 0:
                    balance = 0
                    build = ""
                else:
                    build += ")"
                    count += 2
                    if count > max_count:
                        max_count = count
            elif p == "(":
                build += "("
                balance += 1
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
    }
]
sol = Solution()
for t in tests:
    answer = sol.longestValidParentheses(t["input"])
    if answer == t["answer"]:
        print("tests pass")
    else:
        print("FAIL", answer)
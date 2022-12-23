class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_length = 0
        for i, l in enumerate(s):
            if l == "(":
                stack.append(i)
            elif l == ")":
                stack.pop()
            if len(stack) == 0:
                stack.append(i)
            last = stack[len(stack) - 1]
            len_p = i - last
            if max_length < len_p:
                max_length = len_p
        print(stack)
        return max_length


tests = [
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
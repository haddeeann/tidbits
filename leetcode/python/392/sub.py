class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        r = ""
        i = 0
        last_s = len(s)
        for x in t:
            if i < last_s and x == s[i]:
                r += x
                i += 1

        return r == s


sol = Solution()
test_set = [
    {
        "no": "one",
        "input_1": "abc",
        "input_2": "ahbgdc",
        "answer": True
    },
    {
        "no": "two",
        "input_1": "",
        "input_2": "ahbgdc",
        "answer": True
    },
]
for x in test_set:
    result = sol.isSubsequence(x["input_1"], x["input_2"])
    if result == x["answer"]:
        print("correct")
    else:
        print("FAILED")
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pass


sol = Solution()

t = [
    {
        "no": "one",
        "i_one": "egg",
        "i_two": "add",
        "answer": None
    }
]

for x in test_set:
    a = sol.isIsomorphic(t["i_one"], t["i_two"])
    if a == t["answer"]:
        print(f"{no}: answer is right")
    else:
        print(f"{no}: test has FAILED")
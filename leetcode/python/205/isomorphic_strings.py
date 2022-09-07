class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_dict = {}
        s_dict = {}
        for i, l in enumerate(s):
            if t[i] not in t_dict:
                t_dict[t[i]] = l
            else:
                if t_dict[t[i]] != l:
                    return False
            if l not in s_dict:
                s_dict[l] = t[i]
            else:
                if s_dict[l] != t[i]:
                    return False

        return True


sol = Solution()

t = [
    {
        "no": "one",
        "i_one": "egg",
        "i_two": "add",
        "answer": True
    },
    {
        "no": "two",
        "i_one": "foo",
        "i_two": "bar",
        "answer": False
    },
    {
        "no": "three",
        "i_one": "paper",
        "i_two": "title",
        "answer": True
    },
    {
        "no": "four",
        "i_one": "badc",
        "i_two": "baba",
        "answer": False
    }
]
s = [

]
for x in t:
    a = sol.isIsomorphic(x["i_one"], x["i_two"])
    if a == x["answer"]:
        print(f"{x['no']}: answer is right")
    else:
        print(f"{x['no']}: test has FAILED")
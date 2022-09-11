class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        answer = ['']
        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        for s in digits:
            if s in lookup:
                build = []
                for a in answer:
                    for letter in lookup[s]:
                        build.append(a + letter)
                answer = build

        return [a for a in answer if not a == '']


sol = Solution()

test_cases = [
    {
        "no": "one",
        "input": "234",
        "answer": ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
                   "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
                   "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
    },
    {
        "no": "two",
        "input": "",
        "answer": []
    },
    {
        "no": "three",
        "input": "2",
        "answer": ["a", "b", "c"]
    }
]

for test in test_cases:
    result = sol.letterCombinations(test["input"])
    if result == test["answer"]:
        print("answer is RIGHT")
    else:
        print("failed")
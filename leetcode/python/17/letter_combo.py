class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        answer = []
        letter_combo = ''
        l = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        for x in digits:
            letters = l[x]
            n = (len(digits) - 1) * 3
            for a in range(n):
                len_answer = len(answer)
                if a < len_answer:
                    answer[a] = letters[0]
                else:
                    answer.append(letters[0])
            print(letters)


sol = Solution()

test_cases = [
    {
        "no": "one",
        "input": "23",
        "answer": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
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
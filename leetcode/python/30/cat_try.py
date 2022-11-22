from collections import deque, defaultdict


class Solution:
    def findSubstring(self, s, words):
        ori_word_dict = defaultdict(int)

        for word in words:
            ori_word_dict[word] += 1

        print(ori_word_dict)


sol = Solution()
answers = [
    {
        "string": "aaa",
        "word_list": ["a", "a"],
        "answer": [0, 1]
    },
    {
        "string": "ababababab",
        "word_list": ["ababa", "babab"],
        "answer": [0]
    },
]


for a in answers:
    sol.findSubstring(s=a["string"], words=a["word_list"])

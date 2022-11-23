from collections import deque, defaultdict


class Solution:
    def findSubstring(self, s, words):
        # original word dictionary
        ori_word_dict = defaultdict(int)
        word_len = len(words[0])
        for word in words:
            ori_word_dict[word] += 1

        print("og", sum(ori_word_dict.values()))

        for i in range(word_len):
            print(f"i {i}")
            que = deque()
            word_dict = ori_word_dict.copy()
            end_len = len(s) - word_len + 1
            for j in range(i, end_len, word_len):
                word = s[j:j + word_len]
                if word in word_dict:
                    word_dict[word] -= 1
                    que.append(word)
                    print('sum', sum(word_dict.values()))


sol = Solution()
answers = [
    # {
    #     "string": "aaa",
    #     "word_list": ["a", "a"],
    #     "answer": [0, 1]
    # },
    {
        "string": "ababababab",
        "word_list": ["ababa", "babab"],
        "answer": [0]
    },
]


for a in answers:
    sol.findSubstring(s=a["string"], words=a["word_list"])

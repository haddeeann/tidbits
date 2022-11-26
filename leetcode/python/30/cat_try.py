from collections import deque, defaultdict

class Solution:
    def findSubstring(self, s, words):
        word_len = len(words[0])
        owd = defaultdict(int)

        for word in words:
            owd[word] += 1

            all = len(words) * word_len
            result = []
            for i in range(word_len):
                que = deque()
                word_dict = owd.copy()
                for j in range(i, len(s) - word_len + 1, word_len):
                    word = s[j:j + word_len]
                    if word in word_dict:
                        word_dict[word] -= 1
                        que.append(word)
                        if sum(word_dict.values()) == 0:
                            result.append(j - all + word_len)
                            elem = que.popleft()
                            word_dict[elem] = word_dict.get(elem, 0) + 1
                    else:
                        while len(que):
                            elem = que.popleft()
                            if elem == word:
                                que.append(word)
                                break
                            else:
                                word_dict[elem] = word_dict.get(elem, 0) + 1
                                if word_dict[elem] > owd[elem]:
                                    word_dict = owd.copy()
            return result

sol = Solution()
answers = [
    # {
    #     "string": "aaa",
    #     "word_list": ["a", "a"],
    #     "answer": [0, 1]
    # },
    # {
    #     "string": "ababababab",
    #     "word_list": ["ababa","babab"],
    #     "answer": [0]
    # },
]

for a in answers:
    a["answer"].sort()
    ans = sol.findSubstring(s=a["string"], words=a["word_list"])
    ans.sort()
    if not a["answer"]:
        print("we don't know the answer just print what we get", ans)
        continue
    if len(a["answer"]) != len(ans):
        print("answer is wrong, length is not the same", ans)
        continue
    for i, b in enumerate(ans):
        if b != a["answer"][i]:
            print("answer is wrong", ans)
            continue
    print("answer is right")


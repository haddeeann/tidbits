from collections import deque, defaultdict


class Solution:
    def findSubstring(self, s, words):
        word_len = len(words[0])
        ori_word_dict = defaultdict(int)

        for word in words:
            ori_word_dict[word] += 1

        all_word_len = len(words) * word_len
        result = []
        for i in range(word_len):
            queue = deque()
            word_dict = ori_word_dict.copy()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word_dict.get(word, 0) != 0:
                    word_dict[word] -= 1
                    queue.append(word)
                    if sum(word_dict.values()) == 0:
                        result.append(j - all_word_len + word_len)
                        last_element = queue.popleft()
                        word_dict[last_element] = word_dict.get(last_element, 0) + 1
                else:
                    while len(queue):
                        last_element = queue.popleft()
                        if last_element == word:
                            queue.append(word)
                            break
                        else:
                            word_dict[last_element] = word_dict.get(last_element, 0) + 1
                            if word_dict[last_element] > ori_word_dict[last_element]:
                                word_dict = ori_word_dict.copy()

        return result

sol = Solution()
answers = [
    # {
    #     "string": "aaa",
    #     "word_list": ["a", "a"],
    #     "answer": [0, 1]
    # },
    # {
    #     "string": "12abcdefghij",
    #     "word_list": ["abcde", "fghij"],
    #     "answer": [0]
    # },
    {
        "string": "barfoothefoobarman",
        "word_list": ["foo","bar"],
        "answer": [0,9],
    }
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


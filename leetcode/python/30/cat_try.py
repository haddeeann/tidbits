from collections import deque, defaultdict


class Solution:
    def findSubstring(self, s, words):
        # original word dictionary
        ori_word_dict = defaultdict(int)
        word_len = len(words[0])
        # set up answer result and length of all words
        all_word_len = len(words) * word_len
        result = []
        # create the dict to keep track of how many words we've found
        for word in words:
            ori_word_dict[word] += 1

        for i in range(word_len):
            que = deque()
            # copy it so we start fresh with each i
            word_dict = ori_word_dict.copy()
            end_len = len(s) - word_len + 1
            # go to the end of range of words
            for j in range(i, end_len, word_len):
                word = s[j:j + word_len]
                if word in word_dict:
                    word_dict[word] -= 1
                    que.append(word)
                    # if we've found all hte words in the word dict
                    if sum(word_dict.values()) == 0:
                        # append the start of this, wonder if this wouldn't just be i?
                        result.append(j - all_word_len + word_len)
                        last_element = que.popleft()
                        word_dict[last_element] = word_dict.get(last_element, 0) + 1
                else:
                    while len(que):
                        last_element = que.popleft()
                        if last_element == word:
                            que.append(word)
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
    #     "string": "ababababab",
    #     "word_list": ["ababa", "babab"],
    #     "answer": [0]
    # },
    {
        "string": "barfoothefoobarman",
        "word_list": ["foo","bar"],
        "answer": [0,9],
    }
]


for a in answers:
    sol.findSubstring(s=a["string"], words=a["word_list"])

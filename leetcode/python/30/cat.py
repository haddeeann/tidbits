class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        found_dict = {}
        words_dict = {}
        win = len(words)
        answer = []
        for w in words:
            if w in words_dict:
                words_dict[w] += 1
            else:
                words_dict[w] = 1
            found = 0
            start = 0
            while found != -1:
                found = s.find(w, start)
                if found != -1:
                    found_dict[found] = w
                    l = len(w)
                    start = found + l
                if start == 0 or start > len(s):
                    break

        for index in found_dict:
            # can't be a set because the words need to be repeated, try a dictionary
            words_copy = words_dict.copy()
            step = index
            count = 0
            while count < len(words):
                if step in found_dict:
                    word = found_dict[step]
                    if word in words_copy and words_copy[word] > 0:
                        count += 1
                        words_copy[word] -= 1
                        step += len(word)
                    else:
                        break
                else:
                    break
            if count == win:
                answer.append(index)

        return answer


sol = Solution()
answers = [
    {
        "string": "aaa",
        "word_list": ["a", "a"],
        "answer": [0, 1]
    },
    {
        "string": "ababababab",
        "word_list": ["ababa","babab"],
        "answer": [0]
    }
]


for a in answers:
    a["answer"].sort()
    ans = sol.findSubstring(s=a["string"], words=a["word_list"])
    ans.sort()
    if len(a["answer"]) != len(ans):
        print("answer is wrong, length is not the same", ans)
        break
    for i, b in enumerate(ans):
        if b != a["answer"][i]:
            print("answer is wrong", ans)
            break
    print("answer is right")


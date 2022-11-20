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
        count = 0
        answer = []
        l = len(words[0])
        for w in words:
            if w in words_dict:
                words_dict[w] += 1
            else:
                words_dict[w] = 1
            found = 0
            start = 0
            while found != -1:
                count += 1
                found = s.find(w, start)
                if found != -1:
                    found_dict[found] = w
                    start = found + l - 1
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
        print(answer)
        return answer


sol = Solution()
string = "wordgoodgoodgoodbestword"
word_list = ["word","good","best","good"]
# string = "a"
# word_list = ["a"]
# string = "barfoothefoobarman"
# word_list = ["foo","bar"]
ans = sol.findSubstring(s=string, words=word_list)
# answer should be [8]

# time limit exceeded


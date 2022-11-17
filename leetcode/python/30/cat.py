class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        found_dict = {}
        win = len(words)
        count = 0
        answer = []
        l = len(words[0])
        for w in words:
            found = 0
            start = 0
            while found != -1:
                count += 1
                found = s.find(w, start)
                if found != -1:
                    found_dict[found] = w
                    start = found + l - 1

        for index in found_dict:
            # can't be a set because the words need to be repeated, try a dictionary
            s_set = set(words)
            step = index
            count = 0
            while len(s_set) > 0:
                if step in found_dict:
                    word = found_dict[step]
                    if word in s_set:
                        count += 1
                        s_set.remove(word)
                        word_len = len(word)
                        step = step + word_len
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

ans = sol.findSubstring(s=string, words=word_list)
# answer should be [8]

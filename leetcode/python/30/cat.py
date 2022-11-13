class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        found_dict = {}
        bar = words[0]
        count = 0
        l = len(words[0])
        for w in words:
            print(w)
            found = 0
            start = 0
            while found != -1:
                count += 1
                found = s.find(w, start)
                if found != -1:
                    found_dict[found] = w
                    start = found + l - 1
        print('count ', count)
        print('found ', found_dict)

        for index in found_dict:
            s_set = set(words)
            step = index
            while len(s_set) > 0:
                if step in found_dict:
                    word = found_dict[step]
                    s_set.remove(word)
                    word_len = len(found_dict[index])
                    step = step + word_length
                    print(step, word, word_len)


sol = Solution()
sol.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"])
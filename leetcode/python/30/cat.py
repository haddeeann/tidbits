class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        bar_list = []
        bar = words[0]
        found = 0
        index = 0
        start = 0
        l = len(words[0])
        while found != -1:
            found = s.find(bar, start)
            if found != -1:
                bar_list.append(found)
                print(found)
                start = found + l - 1


sol = Solution()
sol.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"])
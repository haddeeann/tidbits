class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif needle in haystack:
            print(haystack.index(needle))
            return haystack.index(needle)
        else:
            return -1

sol = Solution()
sol.strStr("fsadbutsad", "sad")
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start_set = {"(", "[", "{"}
        end_set = {")", "]", "}"}
        index = 0
        for l in s:
            if l in start_set and index != len(s) - 1:
                if s[index+1] in end_set:
                    index += 2
            else:
                index += 1



s = Solution()
s.isValid("()")